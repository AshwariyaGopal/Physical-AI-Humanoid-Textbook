---
sidebar_position: 1
title: LLM Cognitive Planning
---

# LLM Cognitive Planning

This section delves into the theoretical underpinnings and practical application of using Large Language Models (LLMs) as cognitive planners within the Vision-Language-Action (VLA) paradigm for robotics. We explore how LLMs, traditionally used for text generation and understanding, can be leveraged to translate high-level natural language commands into a sequence of low-level, executable robot actions.

## LLM Planning Theory: Zero-Shot, Few-Shot, and Chain-of-Thought

The ability of LLMs to perform complex reasoning and planning stems from their training on vast datasets, allowing them to infer relationships and patterns without explicit programming for every scenario.

### Zero-Shot Planning

In zero-shot planning, the LLM is given a natural language command and directly asked to generate a plan without any prior examples. The model relies solely on its pre-trained knowledge to understand the intent and formulate a sequence of actions.

```
**Prompt Example (Zero-Shot):**
"Translate 'Go to the kitchen and pick up the apple' into a sequence of ROS 2 actions using Nav2 and Grasp actions.
Expected output format: YAML list of actions, each with 'action' and 'parameters' fields.
Available actions:
- nav2_action_server/NavigateToPose: parameters (x: float, y: float, theta: float, frame_id: string)
- grasp_action_server/GraspObject: parameters (object_id: string, grip_force: float)
- grasp_action_server/PlaceObject: parameters (object_id: string, placement_location: {x: float, y: float, z: float})
"
```

### Few-Shot Planning

Few-shot planning involves providing the LLM with a few examples of natural language commands paired with their corresponding action sequences. This helps guide the model towards the desired output format and style, especially for complex or domain-specific tasks. The examples serve as in-context learning.

### Chain-of-Thought (CoT) Planning

Chain-of-Thought prompting encourages the LLM to explain its reasoning process step-by-step before arriving at a final answer. This technique has shown to significantly improve the performance of LLMs on complex reasoning tasks, including planning. By asking the LLM to "think step by step," we can often achieve more coherent and accurate action sequences.

## Case Study: Prompt-to-YAML Conversion

Let's consider a complex natural language instruction and observe how an LLM cognitive planner translates it into a structured YAML sequence of ROS 2 actions.

**Natural Language Instruction:**
"Find the water bottle on the desk and place it on the shelf."

This seemingly simple command requires a robot to perform a series of navigation, perception (implicitly, to find the bottle), grasping, navigation again, and placing actions.

**LLM Cognitive Planning Process (Conceptual):**

1.  **Interpret Intent**: Understand the core goal: move an object from one location to another.
2.  **Break Down into Sub-goals**:
    *   Go to the desk.
    *   Identify and grasp the water bottle.
    *   Go to the shelf.
    *   Place the water bottle on the shelf.
3.  **Map Sub-goals to ROS 2 Actions**: Select appropriate low-level actions (`NavigateToPose`, `GraspObject`, `PlaceObject`) and infer parameters (coordinates, object IDs).
4.  **Sequence Actions**: Determine the correct order of execution.

**Structured YAML Output Code Block:**

```yaml
- action: nav2_action_server/NavigateToPose
  parameters:
    x: 2.5
    y: 1.0
    theta: 0.0
    frame_id: "map"
- action: grasp_action_server/GraspObject
  parameters:
    object_id: "water_bottle"
    grip_force: 0.7
- action: nav2_action_server/NavigateToPose
  parameters:
    x: 1.0
    y: 3.0
    theta: 1.57
    frame_id: "map"
- action: grasp_action_server/PlaceObject
  parameters:
    object_id: "water_bottle"
    placement_location: {x: 1.1, y: 3.0, z: 0.8}
```

This YAML output can then be directly consumed by a ROS 2 system, which orchestrates the execution of these low-level actions by the robot. The LLM acts as the intelligent bridge, converting abstract human commands into concrete, robot-executable instructions.
