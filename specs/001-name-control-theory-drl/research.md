# Research & Content Strategy: DRL & Dexterity

## Content Decisions

### 1. Tactile & Impedance Control
*   **Decision**: Focus on **Impedance Control** (regulating the relationship between force and motion) rather than pure Force Control.
*   **Rationale**: Impedance control is safer for interaction and more robust to geometric uncertainties, which is critical for humanoid grasping.
*   **Key Concepts to Cover**:
    *   Stiffness/Damping matrices.
    *   Virtual spring-damper analogy.
    *   Integration with tactile sensors (closing the force loop).

### 2. DRL for Locomotion
*   **Algorithm**: **PPO (Proximal Policy Optimization)**.
    *   *Why*: Industry standard, stable, easier to tune than off-policy methods for continuous control.
*   **Observation Space (State)**:
    *   Proprioception: Joint positions ($q$), velocities ($\dot{q}$).
    *   Base state: Linear/Angular velocity, projected gravity vector (orientation).
    *   History: Last actions (for smoothness).
*   **Action Space**:
    *   PD joint position targets (residual control is popular but pure position targets are simpler for explanation).
*   **Reward Function**:
    *   *Positive*: Linear velocity tracking error minimization.
    *   *Negative*: Energy consumption (torques), large accelerations (jerk), falling (termination).

### 3. Sim-to-Real Transfer
*   **Primary Strategy**: **Domain Randomization**.
    *   *Why*: Proven effectiveness without requiring perfect system identification.
    *   *Parameters*: Link masses, friction coefficients, motor gains, sensor noise, control latency.
*   **Advanced Strategy**: **Privileged Learning (Teacher-Student)**.
    *   *Why*: Briefly mention this as the state-of-the-art for traversing difficult terrain (blind student learns from perceptive teacher).

## Technical Context (Simulation)
*   **Simulator**: NVIDIA Isaac Sim (aligned with Module 3).
*   **Framework**: Isaac Lab (formerly Orbit) or IsaacGymEnvs. We will generally refer to "Isaac Sim" to remain framework-agnostic in high-level theory.
