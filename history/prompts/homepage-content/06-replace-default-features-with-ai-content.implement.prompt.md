---
id: 6
title: Replace Default Features with AI-Focused Content
stage: implement
date: 2025-12-14
surface: agent
model: gemini-1.5-flash
feature: homepage-content
branch: main
user: user
command: Replace default Docusaurus feature section with AI-focused content
labels:
  - content
  - homepage
  - features
  - docusaurus
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - src/components/HomepageFeatures/index.tsx
tests_yaml: []
prompt_text: |-
  You are an educational UI content writer.

  Task:
  Replace the default Docusaurus feature section with AI-focused content
  for my book website: "Physical AI & Humanoid Robotics Textbook".

  Requirements:
  - Generate EXACTLY 3 feature cards
  - Each card must have:
    - Short title (2–4 words)
    - One clear paragraph (2–3 lines)
  - Content must align with:
    - Physical AI
    - Humanoid robotics
    - Embodied intelligence
    - AI-native engineering
  - Tone: professional, modern, academic
  - Beginner-friendly but technically correct
  - Do NOT mention Docusaurus, React, or frameworks
  - Do NOT use emojis
  - Do NOT add explanations

  Suggested Themes (use your own wording):
  1. Physical / Embodied AI
  2. Simulation to Real Robots
  3. Vision, Language & Action systems
response_text: |-
  I have updated the `FeatureList` in `src/components/HomepageFeatures/index.tsx` with the new AI-focused content.
---
