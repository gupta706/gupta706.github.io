---
layout: page
title: Research
kicker: What I work on
lede: >-
  My group studies the foundational theory of dynamic optimization, reinforcement
  learning, and game theory. We leverage these theoretical breakthroughs to shape
  the future of technology—optimizing autonomous systems, securing cyberphysical
  infrastructure, and designing efficient markets for energy and transportation.
---

# Theoretical Foundations

Expanding the boundaries of decision making and control theory.

## Reinforcement Learning & Stochastic Control

![Reinforcement Learning & Stochastic Control]({{ '/assets/images/reinforcement_learning_theory.jpg' | relative_url }})

In complex, non-stationary environments, traditional control often falls short. We are pushing the theoretical limits of reinforcement learning (RL) and approximate dynamic programming. Our work on **offline reinforcement learning** establishes finite sample-complexity bounds for continuous state and action spaces. We have also pioneered the **probabilistic contraction analysis of iterated random operators** using Wasserstein divergence, providing a unified framework for the convergence of stochastic algorithms. These breakthroughs enable scalable, robust AI that can make safe decisions in high-dimensional stochastic optimal control problems.

## Game Theory & Multi-Agent Systems

![Game Theory & Multi-Agent Systems]({{ '/assets/images/game_theory_agents.jpg' | relative_url }})

Many real-world systems are decentralized and involve multiple agents with asymmetric information. We develop computationally tractable solutions for multi-agent interactions. Our research characterizes the class of **polynomially solvable bimatrix games** using rank reduction and explores the existence of team-optimal strategies in stochastic teams. This theoretical foundation is crucial for coordinating agents in decentralized systems, from multi-robot navigation to communication link elimination in LQG teams.

## Mechanism Design & Pricing Algorithms

![Mechanism Design & Pricing Algorithms]({{ '/assets/images/mechanism_design_pricing.jpg' | relative_url }})

As resources become more stochastic—such as renewable energy generation or idle cloud computing time—traditional pricing models fail. We are developing novel auction theory for single and multiple goods that are produced randomly and cannot be stored. By modeling these as Stackelberg games, we design menus of items and dynamic pricing algorithms that elicit truthful bidding and ensure fair resource allocation.

# Transforming the Future of Technology

Applying mathematical theory to solve high-impact, real-world challenges.

## Cyberphysical Security

![Cyberphysical Security and Smart Grids]({{ '/assets/images/cyberphysical_security_grid.jpg' | relative_url }})

Cyberphysical systems—from advanced manufacturing to the power grid—rely on networked sensors, making them vulnerable to remote attacks. We utilize the statistical theory of change detection and dynamic games to secure these systems. By developing **dynamic watermarking algorithms for finite Markov decision problems** and modeling defense strategies as **Colonel Blotto games**, we design Nash equilibrium control policies that protect networks (like CAN bus networks in vehicles) against intelligent adversaries.

## Intelligent Transportation & Autonomous Vehicles

![AI and Autonomous Systems]({{ '/assets/images/autonomous_systems_network.jpg' | relative_url }})

Transportation is undergoing a massive shift towards shared mobility, connectivity, and electrification. We apply deep reinforcement learning and approximate dynamic programming to **eco-driving in connected and automated hybrid electric vehicles**, exploiting vehicle-to-everything (V2X) data to optimize fuel consumption and velocity profiles. At the macro level, we design fair pricing mechanisms and multi-objective fleet sizing algorithms for ridehailing and multi-modal transportation networks, paving the way for sustainable and congestion-free mobility.

## Next-Generation Energy Grids

![Electricity market under deep renewable integration]({{ '/assets/images/electricity_market_dakhil.png' | relative_url }})

Integrating intermittent renewable energy into the traditional power grid introduces high imbalance costs. Our research designs innovative market mechanisms that accommodate deep renewable integration. Using stochastic programming and auction theory, we have developed models where generators can sell renewable energy with a **penalty for shortfall**, ensuring the grid remains reliable while keeping bidding truthful and profitable. Furthermore, we develop preemptive scheduling algorithms for electric vehicle (EV) charging to provide robust demand response services.
