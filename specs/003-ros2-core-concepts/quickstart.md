# Quickstart: Implementing the ROS 2 Core Concepts Chapter

**Created**: 2025-12-10

This guide outlines the steps to implement the "ROS 2 Core Concepts" chapter based on the provided specification and plan.

## 1. Goal

The goal is to generate the full Markdown content for the textbook chapter and place it in the correct location within the Docusaurus project.

## 2. Key Artifacts

-   **Specification**: [`spec.md`](./spec.md) - Defines **what** the chapter must contain.
-   **Plan**: [`plan.md`](./plan.md) - Outlines the content structure and design decisions.
-   **Research**: [`research.md`](./research.md) - Contains decisions on analogies and code examples.

## 3. Implementation Steps

The implementation will be performed by an AI agent using the `/sp.implement` command.

1.  **Command**: `/sp.implement`
2.  **Input Prompt**: "Using the plan, spec, and research files, generate the full Markdown content for the 'ROS 2 Core Concepts' chapter. Ensure the content is technically accurate, follows the defined outline, uses the chosen analogies, includes the complete `rclpy` code example, and adheres to all Docusaurus formatting standards."
3.  **Expected Output**: A single Markdown file located at `docs/01-ros2-fundamentals/01_core_concepts.md`.

## 4. Validation

After generation, the content of the file should be manually reviewed against the following criteria:
-   Does it meet all functional requirements from `spec.md`?
-   Is the content structure identical to the outline in `plan.md`?
-   Is the code example runnable and correct as per `research.md`?
-   Is the Markdown formatting clean and correct for Docusaurus?