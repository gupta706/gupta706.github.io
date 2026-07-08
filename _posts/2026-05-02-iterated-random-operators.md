---
title: "Iterated random operators: a lens on learning algorithms"
date: 2026-05-02
author: Abhishek Gupta
math: true
tags: [research, reinforcement-learning, probability]
excerpt: "Many learning and RL algorithms are just a random operator applied over and over. That viewpoint buys you clean convergence guarantees."
---

A surprising number of algorithms in machine learning and reinforcement learning
have the same skeleton: start somewhere, then apply a **random operator** again
and again. Stochastic approximation, empirical value iteration, and many
sampling-based dynamic programming schemes all fit this mold.

Write the update as

$$ x_{k+1} = T_k(x_k), $$

where each $T_k$ is a random operator drawn from some distribution, acting on a
point $x_k$ in a Polish space $\mathcal{X}$. In the ideal, noiseless world we
would iterate a single deterministic contraction $T$ with a unique fixed point
$x^\star$. The question is whether the *random* iteration stays close to that
ideal as we collect more data.

### Why the standard toolkit isn't enough

The usual Banach fixed-point argument wants a metric under which $T$ contracts.
But for several algorithms of interest, the natural notion of "getting closer" is
measured by a **divergence**, not a metric — it need not be symmetric and need
not satisfy the triangle inequality. To handle this we introduced a
*Wasserstein divergence* between probability measures over $\mathcal{X}$ and gave
sufficient conditions under which contraction under this divergence still yields
a limit.

### The payoff

With that machinery, you can treat the algorithm's iterates as a Markov chain
and ask about its limiting behavior directly:

1. Does the distribution of $x_k$ converge as $k \to \infty$?
2. Does that limit concentrate near the true fixed point $x^\star$ as the sample
   budget grows?

Answering these gives **consistency** results for a whole family of algorithms
at once, including settings with continuous state and action spaces where
classical guarantees are hard to come by.

If you want the details, the relevant papers are on the
[Publications]({{ '/publications/' | relative_url }}) page — look for
*probabilistic contraction analysis of iterated random operators* and
*convergence of recursive stochastic algorithms using Wasserstein divergence*.
