# Animal Simulation Game - Enhanced Operation Instructions

## Introduction

Welcome to **Animal Simulation Game**, where you can explore a dynamic ecosystem of interacting animals and enjoy learning about nature's complexity! This guide aims to provide you with detailed instructions on how to play the game, understand its controls, and enhance your simulation experience.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Game Controls](#game-controls)
    - [Step-by-Step Simulation](#step-by-step-simulation)
    - [Continuous Simulation](#continuous-simulation)
3. [What Happens in the Simulation](#what-happens-in-the-simulation)
4. [In-Game Tooltips](#in-game-tooltips)
5. [Additional Resources](#additional-resources)

---

## Getting Started

1. **Installation**:
   - Ensure you have Python installed on your system.
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the game by running:
     ```bash
     python main.py
     ```

2. **Objective**:
   - Observe and interact with a simulation of animals such as rabbits, foxes, and wolves in a dynamically evolving ecosystem.

---

## Game Controls

Here’s a detailed breakdown of how to control the simulation:

### Step-by-Step Simulation
- **Key**: Press `SPACE`
- **What It Does**: Advances the simulation by **one step**, during which:
  - Animals **move** to a new position based on their behavior and environment.
  - Predators like foxes and wolves may **hunt** nearby prey (e.g., rabbits).
  - Animals consume resources (e.g., food) and their **health** updates accordingly.
  - Reproductive events or population changes may occur depending on environmental factors.

### Continuous Simulation
- **Key**: Press `ENTER`
- **What It Does**: Runs the simulation **continuously** in real-time, where:
  - The ecosystem evolves without user intervention.
  - You can observe interactions like hunting, movement, and population dynamics seamlessly.
  - Animals will continue to move, eat, and reproduce until stopped.
- **Stop Continuous Simulation**: Press `ENTER` again to pause the simulation.

### Other Controls
- **Reset Simulation**: Press `R` to reset the game to its initial state.
- **Exit Game**: Press `ESC` to close the game.

---

## What Happens in the Simulation

Here’s what you can expect during gameplay:

- **Animal Movement**:
  - Rabbits move randomly to find food and avoid predators.
  - Foxes and wolves hunt prey, using strategic movements.
- **Hunting & Survival**:
  - Predators hunt nearby prey based on proximity and energy levels.
  - Prey animals may escape based on speed and surroundings.
- **Reproduction**:
  - Animals reproduce when conditions are favorable (e.g., sufficient food and health).
- **Population Dynamics**:
  - Watch as populations rise and fall based on the balance of predators and prey.

---

## In-Game Tooltips

To assist new players, we’ve added **in-game tooltips**:
- When you start the game, a popup explains the controls.
- Tooltips display instructions like:
  - **"Press SPACE to advance the simulation step-by-step."**
  - **"Press ENTER to run the simulation continuously."**

---

## Additional Resources

- **Video/GIF Demonstration**: Check out our [demo video](#) to see the simulation in action!
- **FAQs**:
  - What is a simulation step?
    - A single moment in time where animals act based on their programmed behaviors.
  - How do I stop a continuous simulation?
    - Press `ENTER` again to pause.

---

We hope these detailed instructions make the game more enjoyable and accessible for all players. If you have any questions or ideas, feel free to open an issue or contribute to the project!

Happy Simulating! 😊
