---
title: "Eco-Driving for Connected & Automated Vehicles"
order: 1
summary: "Reinforcement learning and approximate dynamic programming that cut fuel use in hybrid-electric vehicles by exploiting V2V and V2I information."
tags: [Reinforcement Learning, Energy, Autonomous Vehicles]
---

Connected and automated vehicles can see far beyond their own bumper. By fusing
vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) signals — the speed
of the car ahead, the timing of the next traffic light — a controller can plan a
velocity profile that reaches the destination on time while burning far less
fuel.

We develop **real-time approximate dynamic programming** and **safe
model-based reinforcement learning** methods for this problem in hybrid-electric
powertrains. The core challenge is computational: the value function lives over
continuous state and action spaces with hard constraints, so we design rollout
and warm-start schemes that re-solve the perturbed program fast enough to run
on-board.

### Highlights

- A deep reinforcement learning framework for eco-driving in connected and
  automated hybrid-electric vehicles.
- Safe, model-based off-policy RL that respects powertrain and safety
  constraints.
- Approximate dynamic programming that warm-starts from a previously solved
  program to meet real-time budgets.

See the related papers on the [Publications]({{ '/publications/' | relative_url }})
page (filter by *Journal*).
