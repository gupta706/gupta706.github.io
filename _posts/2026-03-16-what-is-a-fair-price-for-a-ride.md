---
title: "What is a fair price for a ride?"
date: 2026-03-16
author: Abhishek Gupta
tags: [transportation, pricing, game-theory, reinforcement-learning]
excerpt: "Ridehailing turned pricing into an algorithm that runs millions of times a day. Whose interests does that algorithm serve — and can 'fair' be made precise?"
---

Every time you open a ride app, an algorithm sets a price, matches you to a
driver, and decides where idle cars should wait. Those decisions, repeated
millions of times a day, quietly shape a city's mobility — and a lot of people's
incomes. My group has spent years asking what it means for that machinery to be
not just *efficient* but **fair**, and whether fairness can be written down
precisely enough to optimize.

## Fair pricing, made precise

Demand in a city is lopsided: some neighborhoods and some hours generate far more
trips, and travel times are asymmetric. Naïve dynamic pricing can entrench those
asymmetries. In *Fair Pricing of Ridehailing Services with Asymmetric Demand and
Travel Time* (2021) we formalize fairness constraints and derive prices that
respect them, showing you don't have to throw away efficiency to get there. The
point is that "fair" stops being a slogan and becomes a **constraint you can
design around**.

## Getting operators to cooperate

Seamless mobility usually requires several operators — a rideshare company, a
transit agency, a bike network — to cooperate, and each is out for itself. In
*Incentive design and profit sharing in multi-modal transportation networks*
(2022) we design the incentives and profit-sharing rules that make cooperation
each operator's best move, so a rider can go door-to-door across modes that would
otherwise never coordinate.

## Keeping the fleet where it's needed

Cars drift to where the last trips ended, not where the next ones will start. In
*Multi-objective vehicle rebalancing for ridehailing systems using a
reinforcement learning approach* (2022) we learn where to reposition idle
vehicles, balancing competing objectives — rider wait time, driver earnings,
efficiency. And in *Fleet sizing and charger allocation in electric vehicle
sharing systems* (2022) we plan the harder, slower decisions: how many electric
vehicles, and where to put the chargers.

## Why it matters

Mobility is being rewritten by software, and the rules encoded in that software
have real distributional consequences — for riders in underserved areas and for
drivers whose livelihoods depend on the matching and pricing logic. Making
fairness a *formal* objective, rather than an afterthought, is how you keep those
consequences from being accidental.

## What it means for the cities we're building

Three shifts make this work more relevant, not less:

- **Electrification** ties mobility to the grid — fleets become flexible demand,
  and charging logistics become part of the pricing problem.
- **Multimodal "mobility-as-a-service"** only works if independent operators are
  incentivized to interoperate; that is a mechanism-design problem, not an app
  feature.
- **The gig economy** has made algorithmic fairness a matter of livelihoods, which
  raises the stakes on getting the objective right.

As transportation, energy, and labor markets fuse into one algorithmic system,
the question "what is a fair price for a ride?" turns out to be a question about
what kind of city we want the algorithms to build.

---

**Papers behind this post:** *Fair Pricing of Ridehailing Services with Asymmetric
Demand and Travel Time* (2021) · *Incentive design and profit sharing in
multi-modal transportation networks* (2022) · *Multi-objective vehicle rebalancing
for ridehailing system using a reinforcement learning approach* (2022) · *Fleet
sizing and charger allocation in electric vehicle sharing systems* (2022). See
them on the [Publications]({{ '/publications/' | relative_url }}) page and the
[transportation-markets project]({{ '/projects/transportation-markets/' | relative_url }}).
