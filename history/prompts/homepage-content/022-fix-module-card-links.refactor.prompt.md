---
id: 022-fix-module-card-links
title: Fix Module Card Links
stage: refactor
date: 2025-12-15
surface: agent
model: gemini-2.0-flash-exp
feature: homepage-content
branch: main
user: user
command: fix broken links
labels: [fix, broken-links, docusaurus]
links: null
files_yaml:
 - src/components/ModuleCards/index.tsx
tests_yaml:
 - manual verification on website
prompt_text: |
 in my explore all modules section when i clicking on any module they are not going on that module page they are givng page not found
response_text: |
 Updated hardcoded module links in `src/components/ModuleCards/index.tsx` to reflect the new directory and file names.
outcome: success
evaluation: manual_check
---

# Fix Module Card Links

## Context
User reported that links in the "Explore All Modules" section were broken, resulting in "page not found" errors, due to previous directory and file renamings.

## Changes
Modified `src/components/ModuleCards/index.tsx` to update the `link` property for each `ModuleItem` in the `ModuleList` array. The links now point to the correct, newly renamed module and file paths.

## Rationale
The previous renaming operations (e.g., `01-ros2-fundamentals` to `Module-1-...`, `01_core_concepts.md` to `Week-1-...`) caused the hardcoded links in the `ModuleCards` component to become invalid. This change directly addresses the broken links, ensuring that clicking on a module card navigates to the correct documentation page.
