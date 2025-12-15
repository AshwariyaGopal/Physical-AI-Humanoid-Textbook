---
id: 012-remove-week-prefix-from-titles
title: Remove Week Prefix from Titles
stage: refactor
date: 2025-12-15
surface: agent
model: gemini-2.0-flash-exp
feature: control-theory-drl
branch: 001-name-control-theory-drl
user: user
command: remove week prefix from titles
labels: [refactor, content, docusaurus]
links: null
files_yaml:
 - docs/Module-5-Control-Theory-for-Humanoids/Week-6-Stability-WBC.md
 - docs/Module-5-Control-Theory-for-Humanoids/Week-7-DRL-Dexterity.md
tests_yaml:
 - verified frontmatter title update
prompt_text: |
 in my module 5 "Module-5: Control Theory for Humanoids" in their files "Week 6 Stability & WBC" and "Week 7 DRL Dexterity" in thier content in heading you write "Week 6 Stability & WBC" and "Week 7 DRL Dexterity" like this just remove week 6 and week 7 bcoz i dont want it in content
response_text: |
 Updated frontmatter `title` in `Week-6-Stability-WBC.md` and `Week-7-DRL-Dexterity.md` to remove "Week X" prefixes.
outcome: success
evaluation: manual_check
---

# Remove Week Prefix from Titles

## Context
User requested removal of "Week 6" and "Week 7" prefixes from the headings (interpreted as frontmatter titles) in Module 5 files.

## Changes
1.  **Week-6-Stability-WBC.md**: Changed `title: Week 6 Stability & WBC` to `title: Stability & WBC`.
2.  **Week-7-DRL-Dexterity.md**: Changed `title: Week 7 DRL Dexterity` to `title: DRL Dexterity`.

## Rationale
-   The user prefers cleaner content titles without the weekly scheduling prefix in the rendered output, while keeping the file naming and IDs (which are hidden/structural) consistent with the Week-X pattern if desired (though user didn't ask to change IDs/filenames here, just "heading content").
