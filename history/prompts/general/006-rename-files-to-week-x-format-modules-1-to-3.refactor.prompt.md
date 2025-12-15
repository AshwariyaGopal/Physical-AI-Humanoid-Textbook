---
id: 006-rename-files-to-week-x-format-modules-1-to-3
title: Rename Files to Week X Format Modules 1 to 3
stage: refactor
date: 2025-12-15
surface: agent
model: gemini-2.0-flash-exp
feature: content-structure
branch: main
user: user
command: rename files and update frontmatter
labels: [refactor, docusaurus, content-structure]
links: null
files_yaml:
 - docs/Module-1-The-Robotic-Nervous-System-ROS-2/Week-1-ROS2-Core-Concepts.md
 - docs/Module-1-The-Robotic-Nervous-System-ROS-2/Week-2-URDF-Description.md
 - docs/Module-2-The-Digital-Twin-Gazebo-Unity/Week-3-Physics-Sensors.md
 - docs/Module-3-The-AI-Robot-Brain-NVIDIA-Isaac/Week-4-Perception-Pipeline.md
tests_yaml:
 - manually verified content preservation
prompt_text: |
 perfect but now chnage thier files name but dont change their content
response_text: |
 Renamed files in Modules 1, 2, and 3 to follow the "Week-X-Topic" convention.
 Updated frontmatter (ID and Title) to match filenames and sequence (Week 1-4).
 Preserved all body content.
outcome: success
evaluation: manual_check
---

# Rename Files to Week X Format Modules 1 to 3

## Context
User requested to rename the files within Modules 1, 2, and 3 to follow the same convention as Module 4 ("Week-X" style), without modifying the educational content, but ensuring ID/Title consistency.

## Changes
1.  **Module 1**:
    *   `01_core_concepts.md` -> `Week-1-ROS2-Core-Concepts.md`
    *   `02_urdf_description.md` -> `Week-2-URDF-Description.md`
2.  **Module 2**:
    *   `01_physics_sensors.md` -> `Week-3-Physics-Sensors.md`
3.  **Module 3**:
    *   `01_perception_pipeline.md` -> `Week-4-Perception-Pipeline.md`

## Rationale
-   Standardized the curriculum structure into a "Week-based" progression (Week 1-5).
-   Updated `id` and `title` in frontmatter to ensure Docusaurus generates correct metadata and headers.
-   Preserved original markdown content to ensure no information was lost.
