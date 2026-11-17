---
name: guiding-questions
description: Before building something open-ended — a skill, feature, doc, plan, config — or fixing something whose intent is unclear, ask the user short rounds of multiple-choice questions to pin down what they mean instead of guessing. Use when a request has several valid shapes and a wrong guess would be costly. Skip when the request is already specific.
---

# Guiding questions

A wrong guess costs a full rebuild; a round of questions costs a minute. Find the real forks, ask about them with concrete options, then build.

## When

- **Open-ended builds**: a new skill, feature, doc, plan or config with several valid shapes.
- **Ambiguous fixes**: a bug or edit where what the user wants is unclear.
- **Skip** when the request is already specific. Build it and state your assumptions in a line.

## Before asking

Read the relevant files, skills, recent diffs and session first. Never ask what the code or conversation already answers.

## Rounds

1. **Ask** with the AskUserQuestion tool: up to 4 questions, 2-4 options each, `multiSelect` when answers aren't exclusive. More than 4 forks? Split them across rounds.
2. **Fold in the answers.**
   - "Other" (free text): restate how you read it in one line, and carry it into later questions.
   - Vague or conflicting answers: turn them into a concrete multiple-choice question in the next round.
3. **Ask to continue** with a separate one-question prompt: "Another round or build now?", naming what the next round would cover. Recommend building once another round wouldn't change what gets built.

## Good questions

- **Rooted in the user's work.** Options use their real files, names and recent examples (`acceptInviteToken.ts`, "the invitee spec"), not placeholders.
- **Recommendation first.** Your pick is the first option, marked "(Recommended)".
- **Real alternatives.** Each option is a shape someone could reasonably want. No leading questions: not one right answer and three strawmen.
- **Short.** Header of 1-2 words, label of 1-5 words, a one-line description of what choosing it means.

## Build

1. **Summarize** the decisions as a short list.
2. **Draft right away** and show the full result in chat, not just a path. The user corrects on the draft.
