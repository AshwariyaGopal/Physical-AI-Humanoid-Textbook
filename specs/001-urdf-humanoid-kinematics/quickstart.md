# Quickstart: Implementing the URDF for Humanoid Bipedal Kinematics Chapter

**Created**: 2025-12-10

This guide outlines the steps to implement the "URDF for Humanoid Bipedal Kinematics" chapter based on the provided specification and plan.

## 1. Goal

The goal is to generate the full Markdown content for the textbook chapter and place it in the correct location within the Docusaurus project.

## 2. Key Artifacts

-   **Specification**: [`spec.md`](./spec.md) - Defines **what** the chapter must contain.
-   **Plan**: [`plan.md`](./plan.md) - Outlines the content structure and design decisions.
-   **Research**: [`research.md`](./research.md) - Contains decisions on key constraints and URDF/SDF comparison.

## 3. Implementation Steps

The implementation will be performed by an AI agent using the `/sp.implement` command.

1.  **Command**: `/sp.implement`
2.  **Input Prompt**: "Using the plan, spec, and research files, generate the full Markdown content for the 'URDF for Humanoid Bipedal Kinematics' chapter. Ensure the content is technically accurate, follows the defined outline, includes explanations of URDF links/joints, humanoid bipedal kinematics, and a detailed URDF vs SDF comparison for Gazebo, adhering to all Docusaurus formatting standards."
3.  **Expected Output**: A single Markdown file located at `docs/01-ros2-fundamentals/02_urdf_description.md`.

## 4. Validation

After generation, the content of the file should be manually reviewed against the following criteria:
-   Does it meet all functional requirements from `spec.md`?
-   Is the content structure identical to the outline in `plan.md`?
-   Is the URDF/SDF comparison accurate and insightful as per `research.md`?
-   Is the Markdown formatting clean and correct for Docusaurus?
