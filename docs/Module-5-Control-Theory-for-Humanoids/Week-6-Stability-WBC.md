---
id: week-6-stability-wbc
title: Stability & Whole-Body Control
sidebar_label: Week 6 Stability & WBC
---

Humanoid robots, with their complex kinematics and dynamic interactions with the environment, present significant challenges in maintaining balance and achieving stable motion. This section explores fundamental concepts in dynamic stability and introduces Whole-Body Control (WBC) as a powerful framework for coordinating humanoid movements.

## 1. Dynamic Stability Models: ZMP and Capture Point

Maintaining stability is paramount for any walking robot. For humanoids, which often interact with uneven terrain or perform dynamic tasks, static stability margins are insufficient. Dynamic stability models provide crucial tools for understanding and controlling balance during motion.

### 1.1. Zero Moment Point (ZMP)

The **Zero Moment Point (ZMP)** is a key concept in humanoid robotics stability. It is defined as the point on the ground where the total moment of all active forces (gravity, inertia, contact forces) acting on the robot is zero. Intuitively, if the ZMP remains within the robot's support polygon (the convex hull of its ground contact points), the robot will maintain balance and not tip over.

*   **Definition:** The point on the ground where the net moment of all forces, including gravity and inertial forces, is zero.
*   **Importance:** For a robot to be statically or dynamically stable, its ZMP must stay within the boundaries of its support area on the ground.
*   **Limitations:** While foundational, controlling directly for ZMP can be challenging, especially during highly dynamic maneuvers, and it doesn't directly provide information about fall prediction or recovery.

### 1.2. Capture Point (CP) Theory

The **Capture Point (CP)**, also known as the Extrapolated Center of Mass (XCoM), builds upon ZMP by considering the robot's momentum. It represents the point on the ground where the robot would need to place its next footstep to come to a complete stop without falling, given its current center of mass position and velocity.

*   **Definition:** A point on the ground where if the robot were to apply an infinite impulse force, it could instantaneously stop and remain balanced. More practically, it indicates where the robot's Center of Mass (CoM) velocity would cause it to fall if contact forces were not adjusted.
*   **Relation to ZMP:** The CP is directly related to the ZMP and the robot's Center of Mass (CoM) dynamics. It provides a more intuitive understanding of dynamic balance.
*   **Benefits:** CP theory is particularly useful for planning dynamic gaits and reacting to external disturbances, as it directly informs where the next footstep should be placed to regain balance.

## 2. Whole-Body Control (WBC): A Prioritized QP Problem

**Whole-Body Control (WBC)** is an advanced control framework designed to coordinate the many degrees of freedom of humanoid robots while simultaneously satisfying multiple, often conflicting, control objectives and constraints. These objectives can include maintaining balance, achieving desired end-effector poses, avoiding joint limits, and minimizing energy consumption.

### 2.1. Formulation as a Prioritized Quadratic Programming (QP) Problem

WBC typically formulates the control problem as a **prioritized Quadratic Programming (QP) problem**. This mathematical optimization approach allows the robot to achieve as many objectives as possible, respecting a predefined hierarchy of priorities.

*   **Quadratic Programming (QP):** A type of mathematical optimization problem involving a quadratic objective function and linear constraints. In WBC, the objective function usually aims to minimize control effort or tracking errors.
*   **Prioritization:** Objectives are assigned priorities (e.g., balance stability is typically higher priority than precise end-effector tracking). The QP solver first attempts to satisfy higher-priority tasks exactly or as closely as possible. Any remaining redundancy in the robot's motion is then used to optimize lower-priority tasks.
*   **Tasks and Constraints:**
    *   **Primary Tasks (High Priority):** Often related to safety and stability, such as ZMP/CP tracking, keeping joints within limits, and maintaining ground contact.
    *   **Secondary Tasks (Lower Priority):** End-effector trajectory tracking, posture control, minimizing joint velocities, or energy optimization.
*   **Advantages:** WBC enables complex, human-like motions by intelligently distributing tasks across the robot's entire body, handling redundancy, and ensuring real-time constraint satisfaction.

## 3. The Linear Inverted Pendulum Model (LIPM) for Gait Generation

The **Linear Inverted Pendulum Model (LIPM)** is a simplified dynamic model widely used in humanoid robot locomotion and gait generation. It abstracts the complex dynamics of a humanoid robot into a single point mass (representing the robot's Center of Mass, CoM) supported by an inverted pendulum leg. The model assumes a constant height for the CoM and negligible mass for the legs.

*   **Description:** The LIPM treats the robot's CoM as a point mass, and the ankle as the pivot point of an inverted pendulum. This simplification linearizes the equations of motion, making them analytically solvable.
*   **Gait Generation:** The simplified equations allow for the analytical generation of stable walking patterns (gaits). By controlling the trajectory of the CoM relative to the support point, the LIPM can generate feasible ZMP and CP trajectories.
*   **Benefits:** Despite its simplicity, LIPM provides robust and computationally efficient methods for generating dynamic walking patterns, especially for robots moving on flat ground. It forms the basis for many real-time gait generators, which are then refined by WBC.

These concepts are foundational to understanding how humanoid robots achieve stable and dynamic locomotion, bridging the gap between theoretical control and practical robotic implementation.
