---
title: "Dynamic Watermarking for Cyberphysical Security"
order: 2
summary: "Change-detection and watermarking algorithms that reveal remote attacks on networked control systems and Markov decision processes."
tags: [Security, Markov Decision Processes, Detection]
---

Networked control systems — autonomous vehicles, drones, factory floors — pull
in vast amounts of sensor data, which makes them attractive targets for remote
attackers who spoof measurements or hijack actuators.

We treat attack detection as a **statistical change-detection** problem and
design *dynamic watermarking*: the controller injects a private, random probing
signal and checks whether the system's response has the statistics it should. If
an attacker tampers with the loop, the watermark's signature breaks and the
attack is exposed.

### Highlights

- A dynamic watermarking algorithm for **finite Markov decision processes**,
  with guarantees on detecting a class of attacks.
- Model-free change-point detection for mixing processes, with unknown pre- and
  post-change kernels.
- Game-theoretic control policies against bus-off attacks in CAN networks.

Related work appears on the [Publications]({{ '/publications/' | relative_url }})
page and connects to the group's broader
[security research]({{ '/research/' | relative_url }}#security-of-cyberphysical-systems).
