---
id: 10
title: Refactor Homepage Features to Use Image Tags
stage: implement
date: 2025-12-14
surface: agent
model: gemini-1.5-flash
feature: homepage-content
branch: main
user: user
command: Refactor image display in HomepageFeatures
labels:
  - refactor
  - homepage
  - images
  - docusaurus
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - src/components/HomepageFeatures/index.tsx
  - src/components/HomepageFeatures/styles.module.css
tests_yaml: []
prompt_text: |-
  The error message `Failed to execute 'createElement' on 'Document': The tag name provided ('/assets/images/EMBODIED_AI-fa9850e70d319914580486a40d02d8ef.jpeg') is not a valid name` indicates that the browser is trying to interpret the image path as an HTML tag. This happens because the `Svg` property in `FeatureItem` expects a React component (like an SVG component), but it's receiving a string path to a JPEG image.

  When I updated the `FeatureList` in `src/components/HomepageFeatures/index.tsx`, I replaced `Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default` with `Svg: require('@site/static/img/EMBODIED_AI.jpeg').default`.

  The original `Svg` property was correctly importing an SVG file as a React component. However, when I changed it to import a JPEG, the `require('...').default` part still treats it as an import for a component, but a JPEG file doesn't export a React component. Docusaurus's `Feature` component expects `Svg` to be a React component, not a direct image URL for `img` tag.

  To fix this, I need to change how the images are rendered. Instead of passing the image path to the `Svg` prop, which is then rendered as `<Svg />`, I should introduce an `img` tag and use the `src` attribute with the image path.

  Here's the plan:
  1.  **Modify `src/components/HomepageFeatures/index.tsx`:**
      *   Change the `FeatureItem` type to include an `imgPath` (string) instead of `Svg` (React component).
      *   Update the `FeatureList` to use the `imgPath` for the images.
      *   Modify the `Feature` component to render an `<img>` tag using `imgPath` instead of `<Svg />`.
  2.  **Add `featureImg` to `styles.module.css`:** Define a new class `featureImg` in `src/components/HomepageFeatures/styles.module.css` for image styling, similar to how `featureSvg` was handled.
  I have successfully modified `src/components/HomepageFeatures/index.tsx`. Now I need to update `src/components/HomepageFeatures/styles.module.css` to define the `featureImg` class and remove the `featureSvg` class.
response_text: |-
  I have updated the `src/components/HomepageFeatures/styles.module.css` with the `featureImg` class and removed `featureSvg`.
---
