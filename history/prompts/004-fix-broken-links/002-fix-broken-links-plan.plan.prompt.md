---
id: 002
title: Fix Broken Links Plan
stage: plan
date: 2025-12-16
surface: agent
model: gemini
feature: fix-broken-links
branch: 004-fix-broken-links
user: user
command: /sp.plan
labels: ["plan", "fix", "links", "docusaurus"]
links:
  spec: specs/004-fix-broken-links/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/004-fix-broken-links/plan.md
tests:
  null
---

## Prompt

(User reported Vercel build error with broken links list)
Fix broken links causing Vercel build failures.

## Response snapshot

Created implementation plan identifying the root cause as a mismatch between filename-based links and `id`-based routes in Docusaurus.
Plan: Update `src/components/ModuleCards/index.tsx` and `docusaurus.config.ts` to use lowercase route paths matching the markdown `id` frontmatter.

## Outcome

- ✅ Impact: Identified root cause (case sensitivity/ID mismatch).
- 🧪 Tests: `npm run build`
- 📁 Files: Plan created.
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: Classic Docusaurus routing issue.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): None
