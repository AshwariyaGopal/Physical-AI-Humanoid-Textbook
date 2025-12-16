# Feature Specification: Fix Broken Links & Build Errors

**Feature Branch**: `004-fix-broken-links`  
**Created**: 2025-12-16  
**Status**: Draft  
**Input**: User description: "Fix broken links causing Vercel build failures in Docusaurus project."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Fix Critical Module Links (Priority: P1)

The build is failing because specific links to course modules are incorrect. Fixing these is the top priority to unblock deployment.

**Why this priority**: These are the explicit errors causing the Vercel build failure. Without fixing them, the site cannot be updated.

**Independent Test**: Run `npm run build` locally. It should proceed further than before (or pass completely if these were the only errors).

**Acceptance Scenarios**:

1. **Given** the current broken state, **When** I run `npm run build`, **Then** it fails with "Broken links found" errors for the 6 specific module paths.
2. **Given** the fixed links, **When** I run `npm run build`, **Then** it DOES NOT report errors for:
   - `/docs/Module-1-The-Robotic-Nervous-System-ROS-2/Week-1-ROS2-Core-Concepts`
   - `/docs/Module-2-The-Digital-Twin-Gazebo-Unity/Week-3-Physics-Sensors`
   - `/docs/Module-3-The-AI-Robot-Brain-NVIDIA-Isaac/Week-4-Perception-Pipeline`
   - `/docs/Module-4-Vision-Language-Action/Week-5-LLM-Cognitive-Planning`
   - `/docs/Module-5-Control-Theory-for-Humanoids/Week-6-Stability-WBC`
   - `/docs/Module-6-Ethical-and-Legal-Embodiment-ELSI/Week-8-Ethical-Frameworks`

---

### User Story 2 - Site-Wide Link Integrity & Case Sensitivity (Priority: P2)

Ensure all other links in the homepage, navbar, and sidebar are correct and respect case-sensitivity (crucial for Linux/Vercel environments).

**Why this priority**: Even if the explicit errors are fixed, other hidden broken links or case-mismatches will fail the build on strict mode or on Vercel's Linux environment.

**Independent Test**: Navigate through the homepage, navbar, and sidebar in a local dev server (`npm start`). All links should load the correct page without 404s.

**Acceptance Scenarios**:

1. **Given** the homepage, **When** I click on any module card or button, **Then** it takes me to the correct existing documentation page.
2. **Given** the navbar and footer, **When** I click links, **Then** they resolve to valid pages.
3. **Given** file paths on disk (e.g., `Module-1...`), **When** links are defined in `docusaurus.config.js` or `index.tsx`, **Then** they MUST match the on-disk capitalization exactly.

---

### User Story 3 - Build Validation & Configuration (Priority: P3)

Verify the final build artifact and optionally adjust configuration if strict mode is too blocking (though fixing is preferred).

**Why this priority**: Final confirmation that the fix works for production.

**Independent Test**: Execute `npm run build` and ensure it completes with exit code 0.

**Acceptance Scenarios**:

1. **Given** all link fixes, **When** `npm run build` is executed, **Then** it completes successfully.
2. **Given** the `docusaurus.config.js` file, **When** examined, **Then** `onBrokenLinks` should preferably remain 'throw' (or 'warn' only if absolutely necessary and agreed upon).

---

### Edge Cases

- **Missing Files**: If a referenced file does not exist, the build MUST fail (unless configured to warn) or the link must be removed.
- **Case Mismatch**: On Windows (case-insensitive), the build might pass even with wrong casing, but it MUST fail on Vercel (Linux). Verification MUST consider strict casing.
- **Circular Redirects**: Ensure no links create infinite redirect loops.

## Assumptions

- The project follows a standard Docusaurus directory structure.
- The user has local node environment set up to run builds.
- The `docs` folder structure corresponds to the module names but might have minor naming discrepancies to be resolved.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST have correct internal links for all 6 core modules in `src/pages/index.tsx` (or wherever defined).
- **FR-002**: All internal links in `docusaurus.config.ts` (navbar, footer) MUST point to existing files.
- **FR-003**: File path references MUST match the exact case of the directory structure on disk.
- **FR-004**: The project MUST build successfully using `npm run build` without broken link errors.

### Key Entities

- **Docs Directory**: `docs/` containing the source Markdown files.
- **Config**: `docusaurus.config.ts` defining global links.
- **Homepage**: `src/pages/index.tsx` defining entry point links.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `npm run build` exits with code 0 (success) on the local machine.
- **SC-002**: 0 broken links reported during the Docusaurus build process.
- **SC-003**: All 6 specific module paths identified in the problem statement resolve correctly to their target pages.