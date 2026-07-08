---
title: "Optimizing in real time: don't re-solve, warm-start"
date: 2026-04-13
author: Abhishek Gupta
tags: [optimization, dynamic-programming, control]
math: true
excerpt: "The world changes faster than you can re-solve a hard optimization from scratch. Perturbation theory says: reuse the solution you already have."
---

There is a gap between optimization on paper and optimization in a running system.
On paper, you solve the problem once. In a car, a factory, or a power system, the
problem is *always slightly changing* — a new constraint, a shifted parameter, an
updated forecast — and you have milliseconds to react. Re-solving a hard dynamic
program from scratch, over and over, is a non-starter. So my group has worked on a
different discipline: **perturbation theory for dynamic programs** — how to update
a solution instead of recomputing it.

## Warm-starting perturbed programs

The core idea: if you've already solved a dynamic program, and the new one is a
small perturbation of it, your old solution is a great starting point. In *An
Algorithm to Warm Start Perturbed (WASP) Constrained Dynamic Programs* (2022) we
make that precise for *constrained* problems, and in *A Computationally Efficient
Algorithm for Perturbed Dynamic Programs (A-PDP)* (2022) we push the efficiency
further. Informally, if the optimal value function is $V^\star$ and the problem
shifts by a small $\varepsilon$, you want the cost of finding the new
$V^\star_\varepsilon$ to scale with $\varepsilon$ — **not** with the cost of
solving from scratch. That is the difference between an algorithm that runs
on-board and one that doesn't.

## When "small" hides a hard problem

Some systems have dynamics on two very different timescales — fast electrical
transients riding under slow mechanical motion. Naïvely these *singularly
perturbed* problems are stiff and hard. In *Discrete-time finite-horizon
optimization of singularly perturbed nonlinear control systems with state-action
constraints* (2023) we exploit that timescale separation instead of fighting it,
turning one intractable problem into two tractable ones.

## From theory to the dashboard

This is not abstract. The real-time eco-driving controller I've written about
elsewhere — *Real-Time Ecodriving Control … Using Approximate Dynamic Programming*
(2022) — is exactly this philosophy in a vehicle: the driving problem changes
every second as traffic evolves, and warm-starting is what lets the optimizer keep
up on embedded hardware.

## Why it matters

The bottleneck in deploying optimal control is rarely the math of the optimum — it
is the **compute budget** for re-deriving it as conditions change. Perturbation
methods attack that bottleneck directly, and they do it with guarantees on how the
solution changes, not just heuristics.

## What it means as the world gets more "live"

Everything is trending toward continuous, real-time optimization under changing
conditions:

- **Digital twins** re-optimize a physical asset as its live sensor data updates —
  a perpetual sequence of perturbed problems.
- **Edge and embedded AI** must re-plan locally, without a round trip to the
  cloud, on tiny power budgets.
- **Model predictive control** re-solves an optimization at every step by design;
  warm-starting is what makes that loop fast enough to close.

The quiet lesson is that in a live system, the valuable skill isn't solving the
problem — it's **cheaply updating** the solution you already have.

---

**Papers behind this post:** *An Algorithm to Warm Start Perturbed (WASP)
Constrained Dynamic Programs* (2022) · *A Computationally Efficient Algorithm for
Perturbed Dynamic Programs (A-PDP)* (2022) · *Discrete-time finite-horizon
optimization of singularly perturbed nonlinear control systems* (2023) ·
*Real-Time Ecodriving Control … Using Approximate Dynamic Programming* (2022). See
the [Publications]({{ '/publications/' | relative_url }}) page.
