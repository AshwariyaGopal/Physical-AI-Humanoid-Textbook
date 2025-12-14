---
id: 4
title: Generate and Integrate "Explore All Modules" Section
stage: implement
date: 2025-12-14
surface: agent
model: gemini-1.5-flash
feature: homepage-content
branch: main
user: user
command: Generate an "Explore All Modules" section for my educational website.
labels:
  - content
  - homepage
  - modules
  - docusaurus
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - src/components/ModuleCards/index.tsx
  - src/components/ModuleCards/styles.module.css
  - src/pages/index.tsx
tests_yaml: []
prompt_text: |-
  You are a curriculum UI content generator.

  Task:
  Generate an "Explore All Modules" section for my educational website.

  Context:
  This website is a Physical AI & Humanoid Robotics textbook.

  My Modules:
  1. ROS 2 Foundations
  2. Simulation & Digital Twins
  3. Isaac ROS and Hardware-Accelerated Visual SLAM (VSLAM)
  4. Vision-Language-Action (VLA)
  5. Control Theory for Humanoids
  6. Ethical and Legal Embodiment (ELSI)
  7. Appendix

  Requirements:
  - Add a section heading: "Explore All Modules"
  - Create a clean card-based layout
  - For EACH module:
    - Module title
    - 1 short professional description (2–3 lines max)
    - A CTA text: "Open Module →" (Appendix should use "Open Appendix →")
  - Tone: professional, modern, educational
  - Keep descriptions aligned with real robotics/AI curriculum
  - Do NOT use emojis
  - Do NOT mention Gemini or AI
  - Do NOT add explanations
response_text: |-
  I have generated and integrated the "Explore All Modules" section with a card-based layout.
---
