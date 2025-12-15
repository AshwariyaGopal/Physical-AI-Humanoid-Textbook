---
id: 013-rename-elsi-module-and-files
title: Rename ELSI Module and Files
stage: refactor
date: 2025-12-15
surface: agent
model: gemini-2.0-flash-exp
feature: elsi
branch: main
user: user
command: rename module and files for ELSI
labels: [refactor, docusaurus, content-structure]
links: null
files_yaml:
 - docs/Module-6-Ethical-and-Legal-Embodiment-ELSI/Week-8-Ethical-Frameworks.md
 - docs/Module-6-Ethical-and-Legal-Embodiment-ELSI/Week-9-Legal-Liability.md
 - docs/Module-6-Ethical-and-Legal-Embodiment-ELSI/_category_.json
tests_yaml:
 - manually verified empty content preservation
prompt_text: |
 i want to change my module name from "Ethical and Legal Embodiment (ELSI)" to "Module-6:Ethical and Legal        Embodiment (ELSI)" and their file name from "01_ethical_frameworks" to "Week-8:Ethical Frameworks" and from "02_legal_liability" to "Week-9:Legal Liability"
response_text: |
 Renamed "Ethical and Legal Embodiment (ELSI)" module to "Module-6-Ethical-and-Legal-Embodiment-ELSI" and its files to "Week-8-Ethical-Frameworks.md" and "Week-9-Legal-Liability.md". Updated frontmatter and added `_category_.json` with position 7.
outcome: success
evaluation: manual_check
---

# Rename ELSI Module and Files

## Context
User requested to rename the "Ethical and Legal Embodiment (ELSI)" module directory and its associated markdown files to follow the "Module-X" and "Week-Y" naming conventions. Also requested specific `id` and `title` and `sidebar_label` in the frontmatter, and correct sidebar positioning.

## Changes
1.  **Renamed Directory**: `docs/Ethical and Legal Embodiment (ELSI)` to `docs/Module-6-Ethical-and-Legal-Embodiment-ELSI` (sanitized name).
2.  **Renamed Files**:
    *   `01_ethical_frameworks.md` to `Week-8-Ethical-Frameworks.md`.
    *   `02_legal_liability.md` to `Week-9-Legal-Liability.md`.
3.  **Updated Frontmatter**:
    *   For `Week-8-Ethical-Frameworks.md`: `id: week-8-ethical-frameworks`, `title: Week 8 Ethical Frameworks`, `sidebar_label: Week 8 Ethical Frameworks`.
    *   For `Week-9-Legal-Liability.md`: `id: week-9-legal-liability`, `title: Week 9 Legal Liability`, `sidebar_label: Week 9 Legal Liability`.
4.  **Created `_category_.json`**: `docs/Module-6-Ethical-and-Legal-Embodiment-ELSI/_category_.json` with `label: "Module-6: Ethical and Legal Embodiment (ELSI)"` and `position: 7`.
5.  **Content Preservation**: Original empty content of files was preserved.

## Rationale
-   Aligned module and file naming with the established "Module-X" and "Week-Y" curriculum structure.
-   Ensured filesystem compatibility by sanitizing directory and file names.
-   Updated Docusaurus frontmatter (`id`, `title`, `sidebar_label`) for proper document identification, display, and sidebar navigation.
-   Used `_category_.json` to correctly position "Module-6" in the sidebar after "Module-5".
