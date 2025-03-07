# Particle Collision Simulation using DEM (Discrete Element Method)

This project simulates the motion of particles under the influence of gravity, taking into account particle-particle collisions, wall collisions, and floor collisions. The simulation uses the Discrete Element Method (DEM) and is visualized using Matplotlib.

## Features:
- **Gravity Effect**: Each particle is affected by gravity, causing it to fall downwards.
- **Elastic Collisions**: Particles collide with each other and the walls, with a coefficient of restitution determining how elastic the collisions are.
- **Damping**: After each collision, a damping factor is applied to reduce the particle velocity, simulating energy loss.
- **Particle Dynamics**: The simulation updates the positions and velocities of the particles over time and displays the results using an animation.

## Equations:
1. **Distance Between Particles**:
   \[
   \text{Distance} = ||r_i - r_j||
   \]
   Where \( r_i \) and \( r_j \) are the positions of particles \( i \) and \( j \).

2. **Velocity Update After Collision**:
   \[
   v_{\text{along normal}} = \text{dot}(v_i - v_j, \text{normal})
   \]
   After the collision:
   \[
   v_i' = v_i - \text{impulse} \times \text{normal}
   \]
   \[
   v_j' = v_j + \text{impulse} \times \text{normal}
   \]

3. **Gravity Effect**:
   \[
   v_y = v_y - g \times dt
   \]
   Where \( g \) is the acceleration due to gravity, and \( dt \) is the time step.

4. **Damping Effect**:
   After a collision, velocities are reduced by a damping factor:
   \[
   v_i = v_i \times \text{damping\_factor}
   \]
   \[
   v_j = v_j \times \text{damping\_factor}
   \]

## Requirements:
- Python 3.x
- NumPy
- Matplotlib

## Running the Simulation:
1. Clone this repository.
2. Install the required dependencies:
