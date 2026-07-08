---
title: "Learning at the edge: fast, distributed, and under attack"
date: 2026-07-06
author: Abhishek Gupta
tags: [reinforcement-learning, federated-learning, bandits, security]
excerpt: "Learning is leaving the data center — spreading across phones, sensors, and servers that are slow, unreliable, and sometimes hostile. That changes what a good algorithm has to survive."
---

For a decade, "training a model" meant one big machine, or a tightly-coupled
cluster, chewing through a clean dataset. That era is ending. Learning is moving
**to the edge** — across phones, vehicles, sensors, and geographically scattered
servers that are slow, intermittently connected, resource-starved, and sometimes
actively malicious. My group has studied what it takes to learn well under those
conditions.

## Robustness when some participants lie

In distributed and federated learning, many workers contribute updates and a
server aggregates them. What if some workers are compromised and send poisoned
updates? Naïve averaging fails badly — a few bad actors can wreck the model. In
*Byzantine Resilience With Reputation Scores* (2022) we defend by having the
system *learn whom to trust*: workers accrue reputation, and the aggregate
discounts the untrustworthy. Robustness becomes something the system infers over
time, not a fixed assumption.

## Learning despite lag

Distributed training is also plagued by **asynchrony** — workers finish at
different times, so updates arrive stale. It's tempting to think this must hurt
generalization. In *Distributed SGD Generalizes Well Under Asynchrony* (2019) we
showed the opposite can hold: done right, asynchronous training still generalizes,
which is what makes large-scale distributed learning practical.

## Bandits: learning while you act

At the edge you often can't separate "collect data" from "make decisions" — you
must learn *while acting*, paying for every mistake. That's the **bandit**
setting, and it shows up everywhere once you look:

- *Maximizing success rate of payment routing using non-stationary bandits*
  (2023) — routing each transaction to succeed, in a world whose statistics
  drift.
- *Interference constrained beam alignment for time-varying channels via
  kernelized bandits* (2022) — pointing a wireless beam correctly as the channel
  changes.
- *Weighted Gaussian process bandits for non-stationary environments* (2022) — the
  common thread: learn fast, but **forget** at the right rate when the world
  moves.

That last point matters. At the edge, the environment is rarely stationary, so a
good learner has to weigh fresh evidence against stale.

## Why it matters

The systems we increasingly rely on — recommendation, payments, wireless,
federated models trained on our devices — are distributed, adversarial, and
non-stationary by nature. Algorithms that assume clean, centralized, i.i.d. data
quietly fail in exactly the places they're deployed. Designing for
untrustworthiness, lag, and drift is not hardening an ideal system; it's building
the *real* one.

## What it means going forward

Three forces make edge learning central to the next decade:

- **Privacy and data gravity** push training toward the data — onto devices —
  rather than hauling data to a central store.
- **Adversaries are now assumed**, not hypothetical; poisoning and manipulation
  are part of the threat model for any open learning system.
- **Non-stationarity is the norm** as models learn continuously from a world that
  won't hold still.

The through-line across all of this — and across much of my group's theory, from
[iterated random operators]({{ '/blog/2026/05/02/iterated-random-operators/' | relative_url }})
to the convergence guarantees underneath these algorithms — is asking not just
*does it work?* but *does it still work when the setting is distributed,
adversarial, and drifting?* Increasingly, that is the only question that matters.

---

**Papers behind this post:** *Byzantine Resilience With Reputation Scores* (2022) ·
*Distributed SGD Generalizes Well Under Asynchrony* (2019) · *Maximizing success
rate of payment routing using non-stationary bandits* (2023) · *Interference
constrained beam alignment … via kernelized bandits* (2022) · *Weighted Gaussian
process bandits for non-stationary environments* (2022). See the
[Publications]({{ '/publications/' | relative_url }}) page.
