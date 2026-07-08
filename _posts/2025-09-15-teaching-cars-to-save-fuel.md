---
title: "Teaching cars to save fuel: reinforcement learning on the road"
date: 2025-09-15
author: Abhishek Gupta
tags: [reinforcement-learning, energy, autonomous-vehicles, sustainability]
excerpt: "A connected car can see the traffic light before you can. Used well, that foresight turns into real fuel savings — and a case study in reinforcement learning that has to run in milliseconds."
---

Transportation is responsible for a large slice of global carbon emissions, and
most of that energy is wasted in the small decisions: braking a little too late,
accelerating toward a light that is about to turn red, holding a speed that the
road ahead does not reward. A **connected and automated vehicle** has information
a human driver does not — the state of the traffic signal, the speed of the car
three vehicles ahead, the grade of the hill coming up. The question my group has
worked on is deceptively simple: *given all that foresight, what is the most
fuel-efficient way to drive?*

## The idea

We frame eco-driving as a stochastic optimal control problem and solve it with
reinforcement learning tailored to the powertrain. In
*A deep reinforcement learning framework for eco-driving in connected and
automated hybrid electric vehicles* (2023), we learn a velocity and
power-split policy that exploits vehicle-to-vehicle and vehicle-to-infrastructure
signals. Because a mistake in a real vehicle is expensive — and unsafe — we
followed up with *Safe Model-based Off-policy Reinforcement Learning for
Eco-Driving* (2022), which keeps the learned policy inside hard safety and
powertrain constraints. And in *Real-Time Ecodriving Control … Using Approximate
Dynamic Programming* (2022) we showed the whole thing can run **on-board, in real
time**, rather than as an offline planner. The same instinct shows up even at the
routing level in *Traffic-Aware Adaptive Routing for Minimizing Fuel Consumption*
(2019): sometimes the greenest route is not the fastest one.

## Why it matters

The impact here is unusually concrete. These are not marginal academic gains —
fuel and emissions are saved on every trip, with **no new hardware**, just better
use of information the vehicle already has. Three things make the work matter
beyond a single demo:

- **It respects reality.** Safety and actuator constraints are treated as hard
  limits, not soft penalties. That is the difference between a paper and
  something an automaker can ship.
- **It runs in real time.** A controller that needs a data center is useless in a
  car; one that runs on an embedded chip is deployable.
- **It generalizes.** Hybrid powertrains today, but the pattern — turn foresight
  into an optimized control policy — applies to trucks, drones, and buildings.

## What it means going forward

We are entering a world of **embodied AI**: systems that don't just predict but
*act* in the physical world under energy and safety budgets. Eco-driving is a
clean microcosm of that world. The lesson that transfers is that raw predictive
power is not enough — the value comes from converting predictions into decisions
that honor physical constraints and a real-time compute budget. As electric and
autonomous fleets scale, control policies like these compound: a few percent per
vehicle, across millions of vehicles, is a meaningful dent in the transport
sector's emissions.

---

**Papers behind this post:** *A deep reinforcement learning framework for
eco-driving in connected and automated hybrid electric vehicles* (2023) · *Safe
Model-based Off-policy Reinforcement Learning for Eco-Driving* (2022) ·
*Real-Time Ecodriving Control in Electrified Connected and Autonomous Vehicles
Using Approximate Dynamic Programming* (2022) · *Traffic-Aware Adaptive Routing
for Minimizing Fuel Consumption* (2019). See them on the
[Publications]({{ '/publications/' | relative_url }}) page, or the
[eco-driving project]({{ '/projects/eco-driving/' | relative_url }}).
