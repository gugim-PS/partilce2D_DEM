# Particle Collision Simulation using DEM (Discrete Element Method)

This project simulates the motion of particles under the influence of gravity, taking into account particle-particle collisions, wall collisions, and floor collisions. The simulation uses the Discrete Element Method (DEM) and is visualized using Matplotlib.

## Features:
- **Gravity Effect**: Each particle is affected by gravity, causing it to fall downwards.
- **Elastic Collisions**: Particles collide with each other and the walls, with a coefficient of restitution determining how elastic the collisions are.
- **Damping**: After each collision, a damping factor is applied to reduce the particle velocity, simulating energy loss.
- **Particle Dynamics**: The simulation updates the positions and velocities of the particles over time and displays the results using an animation.

## Equations:

### 1. Distance Between Particles:
The distance between two particles \(i\) and \(j\) is calculated as the Euclidean distance:
```math
\text{Distance} = ||\mathbf{r}_i - \mathbf{r}_j||
```

Where
```math
\( \mathbf{r}_i \) and \( \mathbf{r}_j \) are the positions of particles \(i\) and \(j\), respectively.
```

### 2. Velocity Update After Collision:
The relative velocity along the normal direction (line connecting the particles) is calculated as:
$$
\mathbf{v}_{\text{along normal}} = (\mathbf{v}_i - \mathbf{v}_j) \cdot \hat{n}
$$
Where:
- \( \mathbf{v}_i \) and \( \mathbf{v}_j \) are the velocities of particles \(i\) and \(j\),
- \( \hat{n} \) is the unit vector along the collision normal (the direction of the collision).

After the collision, the velocities of the particles are updated as:
$$
\mathbf{v}_i' = \mathbf{v}_i - \text{impulse} \times \hat{n}
$$
$$
\mathbf{v}_j' = \mathbf{v}_j + \text{impulse} \times \hat{n}
$$
Where the impulse is calculated by:
$$
\text{impulse} = \frac{2 \cdot (\mathbf{v}_i - \mathbf{v}_j) \cdot \hat{n}}{m_i + m_j}
$$
Where \( m_i \) and \( m_j \) are the masses of particles \(i\) and \(j\).

### 3. Gravity Effect:
The effect of gravity on the particles' velocities in the y-direction is modeled by:
$$
v_y = v_y - g \cdot dt
$$
Where:
- \( g \) is the acceleration due to gravity (9.81 m/s\(^2\)),
- \( dt \) is the time step of the simulation.

### 4. Damping Effect:
After each collision, the velocity of particles is reduced by a damping factor:
$$
\mathbf{v}_i = \mathbf{v}_i \cdot \text{damping\_factor}
$$
$$
\mathbf{v}_j = \mathbf{v}_j \cdot \text{damping\_factor}
$$
Where the damping factor is typically a value less than 1 to simulate energy loss due to inelastic collisions.

## Requirements:
- Python 3.x
- NumPy
- Matplotlib

## Running the Simulation:
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
