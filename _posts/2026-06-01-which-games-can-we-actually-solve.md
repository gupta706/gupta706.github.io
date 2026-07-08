---
title: "Which games can we actually solve?"
date: 2026-06-01
author: Abhishek Gupta
tags: [game-theory, computation, optimization]
math: true
excerpt: "Finding a Nash equilibrium is, in general, believed to be intractable. So the useful question is: which games are the easy ones — and can we make a hard game look easy?"
---

Game theory tells us equilibria *exist*. Computer science adds an unsettling
footnote: **finding** one can be intractable. Computing a Nash equilibrium of a
general two-player game is PPAD-complete — strong evidence that no efficient
algorithm exists in the worst case. That gap between "exists" and "can be
computed" is where a lot of my group's work lives, because it decides whether
game theory is a practical tool or just a beautiful theory.

## The frontier runs along "rank"

For bimatrix games, tractability tracks a quantity called the **rank** of the
game (roughly, the rank of the sum of the two payoff matrices). Rank-0 (zero-sum)
and rank-1 games are solvable with linear programming; from rank-2 upward, the
problem is PPAD-hard. So the natural question is: *how many games are secretly
easy?*

Our answer is **strategic equivalence**. Two games are strategically equivalent
if they have the same best-response structure — and therefore the same equilibria
— even if their payoff matrices look different. In *Rank reduction in bimatrix
games* (2023) and *A fast algorithm to reduce $2\times n$ bimatrix games to
rank-1 games* (2019), we show that many apparently hard, high-rank games are
strategically equivalent to a rank-1 game, and can therefore be **solved with a
linear program**. This effectively enlarges the class of games we know how to
solve efficiently.

When exact solutions are out of reach, approximation takes over: *Two Algorithms
for Computing Exact and Approximate Nash Equilibria in Bimatrix Games* (2021)
gives practical methods, built on the idea of a **best-response bijection**.

## Information changes the game

Equilibria depend not just on payoffs but on *who knows what*. In *Information
structures and values in zero-sum stochastic games* (2017) we study how the value
of a game shifts as you change the players' information — a bridge between the
game-theory and team-theory threads of my work.

## Why it matters

If you cannot compute an equilibrium, you cannot use it — to predict behavior, to
design a mechanism, or to train an agent. Mapping the boundary between tractable
and intractable games, and finding transformations that move a problem to the
easy side of that boundary, is what makes game theory *operational*.

## What it means for AI

Multi-agent systems are having a moment. RL agents are trained against each other;
autonomous systems negotiate for bandwidth, road space, and compute; LLM agents
increasingly interact strategically. Under the hood, all of this is **equilibrium
computation** — and the PPAD wall is real. The practical path forward is exactly
the one this work explores: identify the structure that makes *your* game
tractable, or transform it until that structure appears. As we build economies of
interacting AI agents, knowing which games we can actually solve stops being an
academic curiosity and becomes an engineering constraint.

---

**Papers behind this post:** *Rank reduction in bimatrix games* (2023) · *A fast
algorithm to reduce $2\times n$ bimatrix games to rank-1 games* (2019) · *Two
Algorithms for Computing Exact and Approximate Nash Equilibria in Bimatrix Games*
(2021) · *Information structures and values in zero-sum stochastic games* (2017).
See them on the [Publications]({{ '/publications/' | relative_url }}) page.
