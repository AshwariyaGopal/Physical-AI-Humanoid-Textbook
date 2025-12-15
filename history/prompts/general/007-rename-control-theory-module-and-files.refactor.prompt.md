---
id: 007-rename-control-theory-module-and-files
title: Rename Control Theory Module and Files
stage: refactor
date: 2025-12-15
surface: agent
model: gemini-2.0-flash-exp
feature: content-structure
branch: main
user: user
command: rename module and files for Control Theory
labels: [refactor, docusaurus, content-structure]
links: null
files_yaml:
 - docs/Module-5-Control-Theory-for-Humanoids/Week-6-Stability-WBC.md
 - docs/Module-5-Control-Theory-for-Humanoids/Week-7-DRL-Dexterity.md
 - docs/Module-5-Control-Theory-for-Humanoids/_category_.json
tests_yaml:
 - manually verified content preservation
prompt_text: |
 now i want to chnage my module name from "Control Theory for Humanoids" to "Module-5:Control Theory for Humanoids" and change their file name from "01_stability_wbc" to "Week-6:Stability & WBC" but dont chnage their content just chnage names and also provide id and title like this refernce is id: week-2-URDF-Unified-Robot-Description-Format
 title: Week 2 URDF (Unified Robot Description Format)
 ---
response_text: |
 Renamed "Control Theory for Humanoids" module to "Module-5-Control-Theory-for-Humanoids" and its files to "Week-6-Stability-WBC.md" and "Week-7-DRL-Dexterity.md". Updated frontmatter and added `_category_.json` with position 6.
outcome: success
evaluation: manual_check
---

# Rename Control Theory Module and Files

## Context
User requested to rename the "Control Theory for Humanoids" module directory and its associated markdown files to follow the "Module-X" and "Week-Y" naming conventions. Also requested specific `id` and `title` in the frontmatter and correct sidebar positioning.

## Changes
1.  **Renamed Directory**: `docs/Control Theory for Humanoids` to `docs/Module-5-Control-Theory-for-Humanoids` (sanitized name).
2.  **Renamed Files**:
    *   `01_stability_wbc.md` to `Week-6-Stability-WBC.md`.
    *   `02_drl_dexterity.md` to `Week-7-DRL-Dexterity.md`.
3.  **Updated Frontmatter**:
    *   For `Week-6-Stability-WBC.md`: `id: week-6-stability-wbc`, `title: Week 6 Stability & WBC`.
    *   For `Week-7-DRL-Dexterity.md`: `id: week-7-drl-dexterity`, `title: Week 7 DRL Dexterity`.
4.  **Created `_category_.json`**: `docs/Module-5-Control-Theory-for-Humanoids/_category_.json` with `label: "Module-5: Control Theory for Humanoids"` and `position: 6`.
5.  **Content Preservation**: Original content of files was preserved.

## Rationale
-   Aligned module and file naming with the established "Module-X" and "Week-Y" curriculum structure.
-   Ensured filesystem compatibility by sanitizing directory and file names (e.g., replacing spaces and special characters with hyphens).
-   Updated Docusaurus frontmatter (`id` and `title`) for proper document identification and display.
-   Used `_category_.json` to correctly position "Module-5" in the sidebar after "Module-4".
