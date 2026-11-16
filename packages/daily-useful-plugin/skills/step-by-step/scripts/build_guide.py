#!/usr/bin/env python3
"""Build a dependency-free inline guide from validated plain-text JSON."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

IDENTIFIER = re.compile(r'^[a-z0-9][a-z0-9-]{0,63}$')

def text(value, name, limit=2000):
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ValueError(f'{name} must be nonempty text, at most {limit} characters')

def identifier(value, name):
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        raise ValueError(f'{name} must use 1–64 lowercase letters, digits, or hyphens')

def validate(flow):
    if not isinstance(flow, dict):
        raise ValueError('Guide must be an object')
    for field in ('id', 'revision'):
        identifier(flow.get(field), field)
    text(flow.get('title'), 'title', 160)
    steps = flow.get('steps')
    if not isinstance(steps, list) or not 1 <= len(steps) <= 30:
        raise ValueError('steps must contain 1–30 entries')
    seen = {}
    for step in steps:
        if not isinstance(step, dict):
            raise ValueError('Each step must be an object')
        identifier(step.get('id'), 'step.id')
        if step['id'] in seen:
            raise ValueError('Step IDs must be unique')
        text(step.get('title'), 'step.title', 160)
        text(step.get('instruction'), 'step.instruction')
        for field in ('expected', 'detail'):
            if field in step:
                text(step[field], f'step.{field}')
        if 'choices' in step:
            choices = step['choices']
            if not isinstance(choices, list) or not 2 <= len(choices) <= 8:
                raise ValueError('choices must contain 2–8 entries')
            values = set()
            for choice in choices:
                if not isinstance(choice, dict):
                    raise ValueError('Choices must be objects')
                identifier(choice.get('value'), 'choice.value')
                text(choice.get('label'), 'choice.label', 160)
                if choice['value'] in values:
                    raise ValueError('Choice values must be unique within a step')
                values.add(choice['value'])
        if 'showIf' in step:
            condition = step['showIf']
            if not isinstance(condition, dict):
                raise ValueError('showIf must be an object')
            source = seen.get(condition.get('step'))
            if not source or not any(choice['value'] == condition.get('equals') for choice in source.get('choices', [])):
                raise ValueError('showIf must reference an existing choice on a preceding step')
        links = step.get('links', [])
        if not isinstance(links, list) or len(links) > 5:
            raise ValueError('links must be an array of at most 5 entries')
        for link in links:
            if not isinstance(link, dict):
                raise ValueError('Links must be objects')
            text(link.get('label'), 'link.label', 160)
            text(link.get('url'), 'link.url', 2048)
            url = urlsplit(link['url'])
            if url.scheme not in ('https', 'http') or not url.hostname or url.username or url.password or any(ch.isspace() for ch in link['url']):
                raise ValueError('Links must be absolute HTTP(S) URLs without credentials or whitespace')
        seen[step['id']] = step
    if 'resume' in flow and not isinstance(flow['resume'], dict):
        raise ValueError('resume must be an object')
    if len(json.dumps(flow).encode('utf-8')) > 150000:
        raise ValueError('Guide data exceeds 150 KB')
    return flow

def build(flow, host_bridge=True):
    validate(flow)
    assets = Path(__file__).resolve().parent.parent / 'assets'
    canonical = json.dumps(flow, sort_keys=True, ensure_ascii=False)
    key = hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:16]
    data = json.dumps({'flow': flow, 'key': key, 'hostBridge': host_bridge}, ensure_ascii=False)
    # Escape HTML-parser delimiters even inside a nonexecuting JSON script element.
    data = data.replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    values = {'__ROOT__': f'guide-{flow["id"]}-{key}', '__DATA__': data, '__MACHINE__': (assets / 'wizard-state.js').read_text()}
    return re.sub(r'__ROOT__|__DATA__|__MACHINE__', lambda match: values[match.group()], (assets / 'wizard.html').read_text())

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--no-host-bridge', action='store_true')
    args = parser.parse_args()
    try:
        result = build(json.loads(args.input.read_text()), not args.no_host_bridge)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result)
    except (OSError, ValueError, TypeError) as error:
        parser.error(str(error))
    print(args.output.resolve())

if __name__ == '__main__':
    main()
