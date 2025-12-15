# Data Model: Week 7 DRL & Dexterity

## Learning Object (Chapter Structure)

### 1. Introduction
*   **Goal**: Contrast classical WBC with Learning-based methods.
*   **Key Concept**: "Soft" interaction vs. "Hard" trajectory following.

### 2. Tactile & Impedance Control (Manipulation)
*   **Definition**: $F = K(x_{des} - x) + B(\'dot{x}_{des} - \dot{x})$.
*   **Use Case**: Grasping unknown objects.
*   **Diagram**: Spring-Damper system interacting with environment.

### 3. Deep Reinforcement Learning for Locomotion
*   **The MDP (Markov Decision Process)**: Tuple $(S, A, R, P, \gamma)$.
*   **State Space ($S$)**: Proprioception + IMU.
*   **Action Space ($A$)**: PD targets.
*   **Reward Function ($R$)**:
    *   $r_{vel} = \exp(-\|v - v_{cmd}\|^2)$
    *   $r_{energy} = -\|\tau\|^2$
*   **Algorithm**: PPO (Brief overview).

### 4. Sim-to-Real Transfer
*   **The Gap**: Why simulation $\neq$ reality.
*   **Domain Randomization (DR)**:
    *   Dynamics Randomization (Mass, Friction).
    *   Observation Noise.
*   **Privileged Learning**: Teacher-Student architecture (optional/advanced).

## Entities
*   **Policy ($\pi$)**: Mapping from state to action.
*   **Critic ($V$)**: Estimator of expected return.
*   **Environment**: The physics simulator (Isaac Sim).
