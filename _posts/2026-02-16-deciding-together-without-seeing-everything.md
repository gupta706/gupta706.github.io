---
title: "Deciding together without seeing everything"
date: 2026-02-16
author: Abhishek Gupta
tags: [team-theory, decentralized-control, game-theory, optimization]
math: true
excerpt: "When many agents share a goal but each sees only part of the world, when does an optimal joint strategy even exist? Team theory answers that — and it's quietly the math behind multi-agent AI."
---

Picture a fleet of drones, a network of sensors, or a set of traders in a market.
Each one observes only a sliver of the world and must act on that sliver — yet
their actions combine into a shared outcome. This is the world of **decentralized
decision-making**, and it hides a question that is subtle even before you ask for
a good strategy: *does an optimal joint strategy exist at all?* Infinite spaces
and information split across agents can make the answer surprisingly delicate.

## Existence first, then optimization

A recurring thread of my work establishes when team-optimal strategies exist. In
*On the existence of optimal policies for a class of static and sequential
dynamic teams* (2015) and *Existence of Team-Optimal Solutions in Static Teams
with Common Information* (2020), we develop a **topology-of-information** approach:
treat each agent's strategy as shaping a probability measure and study continuity
in the right topology. That machinery rests on a genuinely foundational result —
*The topology of information on the space of probability measures over Polish
spaces* (2014) — and extends to *Teams with Countable Observation Spaces* (2021).
Existence sounds abstract, but without it, "find the optimal decentralized policy"
is not even a well-posed request.

## Common information: taming asymmetry

When agents know *different* things, equilibria are hard to compute. The **common
information approach** cuts through this: reformulate the problem around what
everyone knows in common, and a coordinator's problem emerges that is tractable.
We used it to characterize *Common information based Markov perfect equilibria*
for linear-Gaussian games (2014) and for finite games (2014), and to design
incentives in *Dynamic incentive design in multi-stage linear-Gaussian games with
asymmetric information* (2014).

## Communication is not free

If agents can talk, which links actually matter? In *Sketching for Elimination of
Communication Links in LQG Teams* (2021) and *Communication Link Elimination in
Static LQG Teams* (2018) we ask when a communication channel can be removed with
negligible loss — a direct handle on the trade-off between **coordination and
bandwidth**.

## Why it matters

Any system where autonomy is distributed lives here: you cannot centralize every
decision, so agents must act locally toward a global goal. The results say *when*
that is possible, *how* to structure the reasoning (around common information),
and *which* communication is worth its cost.

## What it means for multi-agent AI

We are building multi-agent systems at speed — swarms of robots, fleets of
autonomous vehicles, and now **teams of LLM-based agents** collaborating on tasks.
Every one of them faces the team-theory questions in disguise:

- What is the *common knowledge* the agents can coordinate around, and what stays
  private?
- How much *communication* is actually necessary, versus expensive overhead?
- Does a coherent joint strategy even *exist* under their information structure?

Decades before "agentic AI" was a phrase, decentralized control was working out
its foundations. As we hand more collective decisions to machines that each see
only part of the picture, that foundation is exactly what keeps the picture
coherent.

---

**Papers behind this post:** *On the existence of optimal policies for a class of
static and sequential dynamic teams* (2015) · *Existence of Team-Optimal Solutions
in Static Teams with Common Information* (2020) · *Existence of Team-Optimal
Strategies in Teams with Countable Observation Spaces* (2021) · *Common
information based Markov perfect equilibria for linear-Gaussian games* (2014) ·
*The topology of information on the space of probability measures over Polish
spaces* (2014) · *Sketching for Elimination of Communication Links in LQG Teams*
(2021). See the [Publications]({{ '/publications/' | relative_url }}) page.
