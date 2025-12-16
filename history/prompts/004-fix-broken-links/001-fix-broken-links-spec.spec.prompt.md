---
id: 001
title: Fix Broken Links Spec
stage: spec
date: 2025-12-16
surface: agent
model: gemini
feature: fix-broken-links
branch: 004-fix-broken-links
user: user
command: /sp.specify
labels: ["spec", "fix", "docusaurus", "links"]
links:
  spec: specs/004-fix-broken-links/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/004-fix-broken-links/spec.md
  - specs/004-fix-broken-links/checklists/requirements.md
tests:
  null
---

## Prompt

Project: Docusaurus 3 documentation website hosted on Vercel
Problem: Vercel build fails due to broken links in homepage and docs.
Exact errors:
- /docs/Module-1-The-Robotic-Nervous-System-ROS-2/Week-1-ROS2-Core-Concepts
- /docs/Module-2-The-Digital-Twin-Gazebo-Unity/Week-3-Physics-Sensors
- /docs/Module-3-The-AI-Robot-Brain-NVIDIA-Isaac/Week-4-Perception-Pipeline
- /docs/Module-4-Vision-Language-Action/Week-5-LLM-Cognitive-Planning
- /docs/Module-5-Control-Theory-for-Humanoids/Week-6-Stability-WBC
- /docs/Module-6-Ethical-and-Legal-Embodiment-ELSI/Week-8-Ethical-Frameworks
Task for AI:
1. Scan all docs folder files and match them with homepage and sidebar links.
2. Fix any broken or misnamed links in homepage, navbar, and sidebar config so that all links point to existing Markdown files.
3. Ensure file paths are **case-sensitive** and correct for Docusaurus.
4. Optionally, update `docusaurus.config.js` to ignore broken links if any links cannot be fixed immediately.
5. Make sure project builds successfully locally with `npm run build` and passes Vercel build.
Output:
- Corrected files with fixed links
- Short instructions for any manual confirmation needed

## Response snapshot

Created feature specification for fixing broken links.
- Branch: `004-fix-broken-links`
- Short Name: `fix-broken-links`
- Spec File: `specs/004-fix-broken-links/spec.md`
- Validation: Passed quality checklist.

## Outcome

- ✅ Impact: Created comprehensive spec to address build failures.
- 🧪 Tests: N/A
- 📁 Files: Spec and Checklist created.
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Straightforward maintenance task spec.

## Evaluation notes (flywheel)

- Failure modes observed: Script parameter issue (workaround used).
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): Fix script parameter parsing.
