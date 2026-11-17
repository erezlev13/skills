# Guiding Questions

Before building something open-ended (a skill, feature, doc, plan, or an unclear fix), the assistant asks short rounds of multiple-choice questions instead of guessing.

## Try it

“Use guiding-questions to help me design a skill for code reviews.”

Each round has up to four questions with two to four concrete options drawn from your own files and examples. The recommended option comes first. Answer with your picks or write your own; free-text answers are restated in one line. After each round, choose another round or build now. The assistant then lists the decisions and shows the full draft for you to correct. Specific requests skip the questions.

## Install and compatibility

Use the **Daily Useful** plugin package; see its included README for installation. For Codex, copy this complete skill folder to your configured skills directory. Updating repository files alone does not update an installed plugin.

When the host has a multiple-choice question tool, the skill uses it; otherwise questions appear as a numbered list in chat, answered like `1a 2c`. No scripts, credentials, or additional service are required.
