# Research: URDF for Humanoid Bipedal Kinematics

**Created**: 2025-12-10

This document summarizes the research and key decisions made for the "URDF for Humanoid Bipedal Kinematics" textbook chapter.

## 1. Humanoid Bipedal Kinematic Constraints in URDF

### Decision
The chapter will emphasize:
-   **Joint Limits**: Crucial for preventing unnatural poses and ensuring stability.
-   **Collision Models**: Essential for realistic interaction within the simulation, especially for self-collisions during bipedal movement.
-   **Inertial Properties**: Accurate mass and inertia tensors for links are fundamental for dynamic simulations, especially for balance.
-   **Degrees of Freedom (DoF)**: Discussion on managing the high DoF in humanoids and its impact on control.
-   **Kinematic Chains**: How the leg, torso, and arm kinematic chains are typically defined and linked.

### Rationale
These aspects are critical for both the definition and realistic simulation of humanoid bipedal robots. Proper definition of these elements in URDF directly impacts the robot's behavior in a physics simulator like Gazebo.

### Alternatives Considered
-   Focusing on a full humanoid URDF example: Deemed too complex for an introductory chapter. A conceptual breakdown is more effective.
-   Detailed control strategies: Beyond the scope of URDF definition; will be covered in later control theory chapters.

## 2. URDF vs. SDF for Dynamic Physics Simulation in Gazebo

### Decision
The comparison will highlight that URDF is primarily for kinematic and visual descriptions of a single robot, while SDF is a more comprehensive format that can describe a robot, its environment, sensors, and dynamic properties within a simulation. For dynamic physics simulation in Gazebo, SDF is generally more capable due to its richer set of tags for physics properties, sensors, and world elements.

### Rationale
This distinction is fundamental for developers choosing the appropriate format for their simulation needs. While URDF can be converted to SDF, understanding the native strengths of each avoids common pitfalls in complex simulations.

### Alternatives Considered
-   Only focusing on the differences without use-case context: Less practical for the target audience.
-   Ignoring the conversion possibility (URDF to SDF): Important to acknowledge for practical workflows.

### Comparison Points to Emphasize (Table structure in chapter)

| Feature / Property        | URDF Capability                                    | SDF Capability                                                           | Suitability for Gazebo Physics Simulation                                   |
| :------------------------ | :------------------------------------------------- | :----------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Robot Kinematics**      | Excellent for defining links and joints            | Excellent; can also define nested models                                 | Both good for kinematics; SDF better for complex hierarchies.               |
| **Visuals**               | Comprehensive visual tags                          | Comprehensive visual tags                                                | Both handle visuals well.                                                   |
| **Collisions**            | Basic collision shapes                             | More complex collision geometries (e.g., concave shapes, heightmaps)     | SDF offers more detailed collision modeling.                                |
| **Dynamic Properties**    | Limited (mass, inertia)                            | Comprehensive (friction, damping, restitution, ODE/bullet/dart-specific) | **SDF is significantly better** for fine-tuning physics interactions.       |
| **Sensors**               | Limited (joint and link specific)                  | Comprehensive (camera, lidar, IMU, contact, custom sensor plugins)       | **SDF is superior** for defining and configuring various sensors.           |
| **Joint Loops**           | Not directly supported; requires complex workarounds | Directly supported through `<joint>` tag with specific types (e.g., fixed, revolute) | **SDF handles joint loops natively**, simplifying mechanisms like parallel linkages. |
| **World Description**     | Describes a single robot                           | Describes entire simulation environments (lights, terrain, static objects) | **SDF is essential** for defining the full simulation world in Gazebo.      |
| **Nesting/Modularization**| Requires Xacro extension                           | Natively supports nesting of models                                      | SDF offers better modularity for complex robots/worlds.                     |
