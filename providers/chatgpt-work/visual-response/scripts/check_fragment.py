#!/usr/bin/env python3
"""Check portable inline-fragment invariants, not rendering or UI correctness."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re


class FragmentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.ids = set()
        self.root_id = False
        self.saw_element = False

    def handle_decl(self, declaration):
        if declaration.lower().startswith("doctype"):
            self.errors.append("Use an HTML fragment, not a doctype/document.")

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if not self.saw_element and tag not in {"style", "script"}:
            self.saw_element = True
            self.root_id = bool(values.get("id"))
        if tag in {"html", "head", "body"}:
            self.errors.append(f"Document wrapper <{tag}> is not an inline fragment.")
        value = values.get("id")
        if value:
            if value in self.ids:
                self.errors.append(f"Duplicate element ID: {value}")
            self.ids.add(value)
        for name, value in attrs:
            if name in {"href", "src"} and value and value.strip().lower().startswith("javascript:"):
                self.errors.append("JavaScript URLs are not supported.")


def check(path):
    raw = path.read_bytes()
    if len(raw) >= 1_000_000:
        return ["Fragment must be smaller than 1 MB."]
    source = raw.decode("utf-8")
    parser = FragmentParser()
    parser.feed(source)
    errors = parser.errors
    if not parser.saw_element or not parser.root_id:
        errors.append("Give the first content element a unique root ID.")
    if re.search(r"<[^>]*\\\"", source):
        errors.append("Markup contains escaped quotes; write literal HTML.")
    return errors


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("fragment", type=Path)
    args = cli.parse_args()
    try:
        errors = check(args.fragment)
    except (OSError, UnicodeError) as exc:
        cli.exit(1, f"Cannot read UTF-8 fragment: {exc}\n")
    if errors:
        cli.exit(1, "\n".join(errors) + "\n")
    print("Basic fragment checks passed; runtime, layout, and host delivery are not verified.")


if __name__ == "__main__":
    main()
