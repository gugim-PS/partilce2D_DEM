import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.81  # Gravitational acceleration (m/s^2)
dt = 0.05  # Time step (s)
radius = 0.05  # Particle radius (m)
restitution = 0.4  # Coefficient of restitution (elasticity, 1 is perfect elastic collision)
damping_factor = 0.4  # Damping factor (retains 40% of velocity after collision)
num_particles = 100  # Number of particles
width = 10.0  # Width of the simulation box (m)
height = 5.0  # Height of the simulation box (m)

# Initialize particles
positions = np.random.rand(num_particles, 2) * np.array([width, height])  # Initial positions (random)
velocities = np.random.randn(num_particles, 2) * 2  # Initial velocities (mean 0, std deviation 2)

# Visualization setup
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=50)

# Particle collision handling function
def check_collisions(positions, velocities, radius, restitution, damping_factor):
    num_particles = len(positions)
    
    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            # Calculate the distance between particles
            delta_pos = 2 * (positions[i] - positions[j])
            distance = np.linalg.norm(delta_pos)  # Distance between two particles
            
            # Collision condition: if the distance between particles is less than the sum of their radii
            if distance < 2 * radius:
                # Calculate collision vector (velocity vector of two particles)
                normal = delta_pos / distance  # Normal vector
                relative_velocity = velocities[i] - velocities[j]
                velocity_along_normal = np.dot(relative_velocity, normal)  # Velocity along collision direction
                
                # Update velocity after collision
                if velocity_along_normal < 0:  # Only react if the particles are moving towards each other
                    impulse = (2 * velocity_along_normal) / 2  # Calculate the impulse
                    velocities[i] -= impulse * normal  # Update particle i's velocity
                    velocities[j] += impulse * normal  # Update particle j's velocity

                    # Apply damping effect: slightly decrease speed
                    velocities[i] *= damping_factor
                    velocities[j] *= damping_factor
    
    return velocities

# Wall and floor collision handling function
def handle_wall_collisions(positions, velocities, width, height, radius, restitution):
    # Floor collision handling
    below_ground = positions[:, 1] < radius  # Check if particle is below the floor
    velocities[below_ground, 1] *= -restitution  # Reflect velocity, reverse direction

    # Side wall collision handling
    left_wall = positions[:, 0] < radius  # Check if particle is at the left wall
    right_wall = positions[:, 0] > width - radius  # Check if particle is at the right wall
    velocities[left_wall, 0] *= -restitution  # Reflect velocity at the left wall
    velocities[right_wall, 0] *= -restitution  # Reflect velocity at the right wall
    
    # Limit particle positions so they do not move outside the walls
    positions[:, 0] = np.clip(positions[:, 0], radius, width - radius)  # Limit x position to the wall
    positions[:, 1] = np.clip(positions[:, 1], radius, height - radius)  # Limit y position to the floor
    
    return velocities, positions

# Gravity and particle collision handling function
def update(frame):
    global positions, velocities

    # Apply gravity (in the y-direction)
    velocities[:, 1] -= g * dt  # Change in velocity due to gravity

    # Update positions
    positions += velocities * dt

    # Handle wall and floor collisions
    velocities, positions = handle_wall_collisions(positions, velocities, width, height, radius, restitution)

    # Handle particle collisions
    velocities = check_collisions(positions, velocities, radius, restitution, damping_factor)

    # Update particle positions
    scatter.set_offsets(positions)
    return scatter,

# Create animation
from matplotlib.animation import FuncAnimation
ani = FuncAnimation(fig, update, frames=200, interval=dt * 1000, blit=True)

plt.show()
