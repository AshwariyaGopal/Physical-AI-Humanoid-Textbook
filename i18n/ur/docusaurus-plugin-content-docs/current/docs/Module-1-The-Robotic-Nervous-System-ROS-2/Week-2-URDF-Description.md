---
id: week-2-urdf-description
title: Week 2 URDF Description
---

## URDF vs. SDF: Robot Description for Simulation

When working with robot simulations, particularly in environments like Gazebo, understanding the differences between **URDF (Unified Robot Description Format)** and **SDF (Simulation Description Format)** is crucial. While both are XML formats used to describe robots, they serve different primary purposes and offer varying levels of detail, especially concerning dynamic physics simulation.

**URDF** is fundamentally designed to describe the kinematic and visual properties of a single robot. It defines the robot's structure (links and joints), its visual appearance, and its collision geometry. It is extensible (e.g., via Xacro) but is limited in its ability to specify complex physical properties or environmental interactions directly.

**SDF**, on the other hand, is a more comprehensive format capable of describing not just a robot, but an entire simulation environment including static objects, lights, terrains, and advanced sensor definitions. It is specifically designed to work with physics engines like those in Gazebo, offering a richer set of tags for dynamic properties and interactive elements.

Here's a comparison highlighting their suitability for dynamic physics simulation:

| Feature / Property        | URDF Capability                                    | SDF Capability                                                           | Suitability for Gazebo Physics Simulation                                   |
| :------------------------ | :------------------------------------------------- | :----------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Robot Kinematics**      | Excellent for defining links and joints            | Excellent; can also define nested models                                 | Both good for kinematics; SDF better for complex hierarchies.               |
| **Visuals**               | Comprehensive visual tags                          | Comprehensive visual tags                                                | Both handle visuals well.                                                   |
| **Collisions**            | Basic collision shapes                             | More complex collision geometries (e.g., concave shapes, heightmaps)     | SDF offers more detailed collision modeling.                                |
| **Dynamic Properties**    | Limited (mass, inertia)                            | Comprehensive (friction, damping, restitution, restitution, ODE/bullet/dart-specific) | **SDF is significantly better** for fine-tuning physics interactions.       |
| **Sensors**               | Limited (joint and link specific)                  | Comprehensive (camera, lidar, IMU, contact, custom sensor plugins)       | **SDF is superior** for defining and configuring various sensors.           |
| **Joint Loops**           | Not directly supported; requires complex workarounds | Directly supported through `<joint>` tag with specific types (e.g., fixed, revolute) | **SDF handles joint loops natively**, simplifying mechanisms like parallel linkages. |
| **World Description**     | Describes a single robot                           | Describes entire simulation environments (lights, terrain, static objects) | **SDF is essential** for defining the full simulation world in Gazebo.      |
| **Nesting/Modularization**| Requires Xacro extension                           | Natively supports nesting of models                                      | SDF offers better modularity for complex robots/worlds.                     |

### Example: Simple URDF for Two Links and a Revolute Joint

Below is a basic URDF example demonstrating two links (`link1`, `link2`) connected by a `revolute` joint, similar to a knee or hip. This illustrates the fundamental structure for defining kinematic chains.

```xml
<?xml version="1.0"?>
<robot name="simple_arm">
  <!-- Link 1 -->
  <link name="link1">
    <visual>
      <geometry>
        <cylinder length="0.2" radius="0.05"/>
      </geometry>
      <material name="blue">
        <color rgba="0 0 0.8 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <cylinder length="0.2" radius="0.05"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.5"/>
      <inertia ixx="0.001" ixy="0" ixz="0" iyy="0.001" iyz="0" izz="0.001"/>
    </inertial>
  </link>

  <!-- Joint 1 (revolute between link1 and link2) -->
  <joint name="joint1" type="revolute">
    <parent link="link1"/>
    <child link="link2"/>
    <origin xyz="0 0 0.1" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
    <limit lower="-1.57" upper="1.57" effort="10" velocity="0.5"/>
  </joint>

  <!-- Link 2 -->
  <link name="link2">
    <visual>
      <geometry>
        <cylinder length="0.2" radius="0.05"/>
      </geometry>
      <material name="red">
        <color rgba="0.8 0 0 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <cylinder length="0.2" radius="0.05"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.5"/>
      <inertia ixx="0.001" ixy="0" ixz="0" iyy="0.001" iyz="0" izz="0.001"/>
    </inertial>
  </link>
</robot>
