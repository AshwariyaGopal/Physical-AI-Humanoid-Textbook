---
id: 023-fix-language-button-onclick-error
title: Fix Language Button onClick Error
stage: fix
date: 2025-12-15
surface: agent
model: gemini-2.0-flash-exp
feature: internationalization
branch: main
user: user
command: fix language button error
labels: [fix, docusaurus, i18n]
links: null
files_yaml:
 - docusaurus.config.ts
tests_yaml:
 - manual verification on website
prompt_text: |
 when i am clicking language button and selct urdu so they are givin this Uncaught runtime errors:
 ×
 ERROR
 Expected `onClick` listener to be a function, instead got a value of `string` type.
     at getListener (webpack-internal:///./node_modules/react-dom/cjs/react-dom-client.development.js:3306:15)
     at eval (webpack-internal:///./node_modules/react-dom/cjs/react-dom-client.development.js:19430:32)
     at batchedUpdates$1 (webpack-internal:///./node_modules/react-dom/cjs/react-dom-client.development.js:3254:40)
     at dispatchEventForPluginEventSystem (webpack-internal:///./node_modules/react-dom/cjs/react-dom-client.development.js:19319:7)
     at dispatchEvent (webpack-internal:///./node_modules/react-dom/cjs/react-dom-client.development.js:23584:11)
     at dispatchDiscreteEvent (webpack-internal:///./node_modules/react-dom/cjs/react-dom-client.development.js:23552:11)
response_text: |
 Fixed the `onClick` runtime error by replacing the custom language dropdown configuration in `docusaurus.config.ts` with Docusaurus's built-in `localeDropdown` type. This ensures correct handling of language switching.
outcome: success
evaluation: manual_check
---

# Fix Language Button onClick Error

## Context
User reported a runtime error (`Expected `onClick` listener to be a function, instead got a value of `string` type`) when clicking the language button and selecting "Urdu". This indicated an incorrect setup for the language dropdown in Docusaurus.

## Changes
Modified `docusaurus.config.ts` to replace the manually defined language dropdown with `type: 'localeDropdown'`.

## Rationale
The Docusaurus `navbar.items` configuration expects an `onClick` handler to be a function reference for custom dropdown items, not a string of JavaScript code. The built-in `localeDropdown` type handles all the intricacies of language switching correctly, automatically generating the appropriate links and event handlers based on the `i18n` configuration in `docusaurus.config.ts`. This resolves the `onClick` type error and provides native Docusaurus internationalization functionality.
