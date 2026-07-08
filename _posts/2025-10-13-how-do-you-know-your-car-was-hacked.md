---
title: "How do you know your self-driving car hasn't been hacked?"
date: 2025-10-13
author: Abhishek Gupta
tags: [security, cyberphysical-systems, detection, reinforcement-learning]
excerpt: "A hijacked sensor doesn't announce itself. The defense is statistical: make the system's own behavior betray the intruder."
---

A modern vehicle, drone, or factory line is a **cyberphysical system** — networked
computers steering physical machinery, fed by a flood of sensor data. That data
firehose is exactly what makes these systems vulnerable: an attacker who can
spoof a measurement or replay an old one can quietly steer the system toward
failure, and nothing on the dashboard lights up. So the defensive question is not
"can we build a wall?" but "**can we notice, from the data alone, that something
has changed?**"

## The idea: make the system tell on the intruder

One answer is *dynamic watermarking*. The controller injects a private, random
probing signal into its actions and then checks whether the system's response
carries the statistical signature it should. Tamper with the loop and the
signature breaks. In *Dynamic Watermarking Algorithm for Finite Markov Decision
Processes* (2025) we extended this idea from linear systems to the far more
general setting of finite MDPs, where the "physics" is a Markov kernel rather
than a tidy equation.

The deeper tool underneath is **statistical change detection** — deciding, as
fast as possible, that the process generating your data has shifted. That is hard
when you don't know the "after" distribution, or even the "before." We tackled
exactly this in *Change Detection of Markov Kernels with Unknown Pre and Post
Change Kernel* (2022) and *Model-free change point detection for mixing
processes* (2024), which drops the assumption that you have a clean model of
normal behavior at all. And in *Nash equilibrium control policy against bus-off
attacks in CAN networks* (2022) we looked at a real automotive attack — knocking
a node off the CAN bus — as a game between attacker and defender.

## Why it matters

Detection is the unglamorous foundation of security. You cannot respond to an
attack you cannot see. What makes this line of work useful in practice:

- **It needs no extra sensors** — the watermark rides on the control signal the
  system already sends.
- **It degrades gracefully** — the model-free variants keep working when your
  assumptions about "normal" are wrong, which they always partly are.
- **It comes with guarantees** — not "it worked in our test," but bounds on what
  classes of attacks are detectable and how quickly.

## What it means in a world full of autonomy

As we hand more decisions to autonomous systems — cars, delivery drones, grid
controllers, and increasingly **learning-based agents** — the attack surface
grows and the stakes rise. Two implications stand out. First, security has to be
designed *into the control loop*, not bolted on afterward; a watermark is part of
how the controller acts. Second, as the "system" becomes an ML policy whose
behavior we don't fully understand, change-detection methods that are
**model-free** become essential: they watch for the statistical fingerprint of
tampering without needing a perfect model of the thing they're protecting. That
is a good template for monitoring AI agents in general.

---

**Papers behind this post:** *Dynamic Watermarking Algorithm for Finite Markov
Decision Processes* (2025) · *Model-free change point detection for mixing
processes* (2024) · *Change Detection of Markov Kernels with Unknown Pre and Post
Change Kernel* (2022) · *Nash equilibrium control policy against bus-off attacks
in CAN networks* (2022). Explore them on the
[Publications]({{ '/publications/' | relative_url }}) page and the
[dynamic-watermarking project]({{ '/projects/dynamic-watermarking/' | relative_url }}).
