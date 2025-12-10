# Data Model: Vision-Language-Action (VLA) LLM Cognitive Planning

## Entities

### Natural Language Command

Represents the free-form text input provided by a robotics engineer to instruct the robot.

-   **command**: (string) - The user's instruction in natural language.

### Cognitive Plan

Represents the high-level interpretation and sequencing of tasks derived from the natural language command by the LLM. This is an internal representation of the LLM's thought process or derived plan before translation to executable actions.

-   **high_level_plan**: (string) - Textual description of the LLM's cognitive steps.
-   **derived_intent**: (string) - The primary goal or intent extracted from the natural language command.
-   **confidence_score**: (float) - A measure of the LLM's confidence in its interpretation (optional, for advanced error handling).

### Low-Level ROS 2 Action

Represents a granular, executable operation that a robot can perform. This is the atomic unit of robot behavior.

-   **type**: (string) - The ROS 2 action name or identifier (e.g., `nav2_action_server/NavigateToPose`, `grasp_action_server/GraspObject`).
-   **parameters**: (map/dictionary) - A collection of key-value pairs representing the arguments required for the specific ROS 2 action (e.g., `x`, `y`, `theta` for Nav2, `object_id`, `gripper_force` for Grasp).

### ROS 2 Action Sequence (YAML)

Represents a structured YAML document containing an ordered list of Low-Level ROS 2 Actions. This is the primary output of the system, intended for execution by a ROS 2 system.

-   **actions**: (list of Low-Level ROS 2 Action) - An ordered collection of actions to be executed.
-   **format**: (string) - Always "YAML" for this feature.

## Relationships

-   A **Natural Language Command** is processed to generate a **Cognitive Plan**.
-   A **Cognitive Plan** is translated into a **ROS 2 Action Sequence (YAML)**.
-   A **ROS 2 Action Sequence (YAML)** is composed of an ordered list of **Low-Level ROS 2 Actions**.

## Validation Rules

-   **Natural Language Command**: Must be a non-empty string.
-   **Low-Level ROS 2 Action**:
    -   `type` must be one of the pre-defined supported actions (initially `nav2_action_server/NavigateToPose`, `grasp_action_server/GraspObject`).
    -   `parameters` must include all required parameters for the specified `type` and their values must conform to expected data types and ranges.
-   **ROS 2 Action Sequence (YAML)**: Must be a valid YAML document and contain at least one valid **Low-Level ROS 2 Action**.
