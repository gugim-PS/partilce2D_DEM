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
   \text{Distance} = ||\mathbf{r}_i - \mathbf{r}_j||
   \]
   Where \( \mathbf{r}_i \) and \( \mathbf{r}_j \) are the positions of particles \( i \) and \( j \), respectively.

2. **Velocity Update After Collision**:
   \[
   \mathbf{v}_{\text{along normal}} = \mathbf{v}_i - \mathbf{v}_j \cdot \hat{n}
   \]
   Where:
   - \( \mathbf{v}_i \) and \( \mathbf{v}_j \) are the velocities of particles \( i \) and \( j \),
   - \( \hat{n} \) is the unit vector along the collision normal (the direction of the collision).
   
   After the collision, the velocity update equations are:
   \[
   \mathbf{v}_i' = \mathbf{v}_i - \text{impulse} \times \hat{n}
   \]
   \[
   \mathbf{v}_j' = \mathbf{v}_j + \text{impulse} \times \hat{n}
   \]
   The impulse is calculated as:
   \[
   \text{impulse} = \frac{2 \cdot (\mathbf{v}_i - \mathbf{v}_j) \cdot \hat{n}}{m_i + m_j}
   \]
   where \( m_i \) and \( m_j \) are the masses of particles \( i \) and \( j \).

3. **Gravity Effect**:
   \[
   v_y = v_y - g \cdot dt
   \]
   Where:
   - \( g \) is the acceleration due to gravity (9.81 m/s\(^2\)),
   - \( dt \) is the time step of the simulation.

4. **Damping Effect**:
   After a collision, the velocities are reduced by a damping factor:
   \[
   \mathbf{v}_i = \mathbf{v}_i \cdot \text{damping\_factor}
   \]
   \[
   \mathbf{v}_j = \mathbf{v}_j \cdot \text{damping\_factor}
   \]
   Where the damping factor is typically a value less than 1 to simulate energy loss.

## Requirements:
- Python 3.x
- NumPy
- Matplotlib

## Running the Simulation:
1. Clone this repository.
2. Install the required dependencies:
