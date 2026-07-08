---
title: "Reinforcement learning where the state space never ends"
date: 2026-01-19
author: Abhishek Gupta
tags: [reinforcement-learning, theory, optimization]
math: true
excerpt: "Textbook RL lives in small, tidy worlds. The real one is continuous, constrained, and only lets you learn from data you already collected. Here's some of what it takes to bridge that gap."
---

Reinforcement learning looks solved in the textbook: enumerate the states, fill
in a table, iterate. The real world is not a table. Its state and action spaces
are **continuous**, the set of legal actions *depends on where you are*, you often
can't experiment freely, and "optimal on average" is not good enough when the
downside is catastrophic. A lot of my group's theory work is about closing that
gap between the clean algorithm and the messy problem.

## Continuous spaces and state-dependent actions

When states and actions form a continuum, value iteration becomes an
approximation problem. In *Fitted Value Iteration in Continuous MDPs With State
Dependent Action Sets* (2021) we handle a wrinkle most treatments ignore: the
feasible actions change with the state — a car near a wall simply cannot turn as
hard. Earlier, *An empirical relative value learning algorithm for
non-parametric MDPs with continuous state space* (2019) and *An empirical
algorithm for relative value iteration for average-cost MDPs* (2015) built
*empirical dynamic programming*: replace exact expectations with samples and ask
when the sampled algorithm still converges to the truth as data grows.

## Learning from data you already have

Increasingly you can't explore — you have a fixed log of past behavior and must
learn a good policy from it. That's **offline RL**, and it's fragile: the policy
wants to try actions the data never covered. In *Finite sample analysis of a
minmax variant of offline reinforcement learning for general MDPs* (2022) we gave
finite-sample guarantees — not "it worked," but bounds on how much data buys how
much performance.

## Constraints and risk

Two more gaps between theory and deployment:

- **Constraints.** Real agents must satisfy budgets, safety limits, service
  levels. *Learning in Constrained Markov Decision Processes* (2022) studies
  learning when the problem itself is a constrained MDP.
- **Risk.** Optimizing the *average* can be reckless. *Robustness to Modeling
  Errors in Risk-Sensitive Markov Decision Problems with Markov Risk Measures*
  (2025) asks for policies that stay good even when your model is a little wrong
  and you care about the tail, not the mean: roughly,

  $$ \min_\pi \; \rho\big(\text{cost}\big) \quad\text{subject to model error},$$

  where $\rho$ is a risk measure rather than an expectation.

## Why it matters

These are the exact failure modes that separate a benchmark score from a
deployable system. Continuous dynamics, offline data, hard constraints, and tail
risk are not edge cases — they are what "the real world" *means* for a
decision-making agent.

## What it means for modern AI

The most consequential RL today trains large language models from **logged human
feedback** — an offline RL problem with an enormous action space, wrapped in
safety constraints, where average-case tuning can hide rare but serious failures.
The questions we've studied in control-theoretic clothing — *when does learning
from fixed data generalize? how do you respect constraints while learning? how do
you guard against model error and the tail?* — are precisely the questions facing
anyone deploying a learning agent that acts in the world. The vocabulary differs;
the mathematics is the same.

---

**Papers behind this post:** *Fitted Value Iteration in Continuous MDPs With State
Dependent Action Sets* (2021) · *Finite sample analysis of minmax variant of
offline reinforcement learning for general MDPs* (2022) · *Learning in Constrained
Markov Decision Processes* (2022) · *Robustness to Modeling Errors in
Risk-Sensitive Markov Decision Problems* (2025) · *An empirical relative value
learning algorithm for non-parametric MDPs* (2019). See the
[Publications]({{ '/publications/' | relative_url }}) page.
