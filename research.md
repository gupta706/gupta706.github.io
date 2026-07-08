---
layout: page
title: Research
kicker: What I work on
lede: >-
  My group studies the theory and applications of dynamic optimization and
  reinforcement learning — and puts it to work in AI, security, energy, and
  transportation.
---

# Theory

## Approximate dynamic programming

Major innovations in IoT let us capture rich datasets for real-time decision and
control. Most hardware today runs rule-based control algorithms over data from
rich sensors. We are transforming this paradigm by developing fast approximate
dynamic programming algorithms for real-time decision making in
information-rich environments. Toward this end, we have developed rollout
algorithms for optimizing the fuel efficiency of autonomous vehicles and for
building energy management.

## Reinforcement learning

In many high-dimensional stochastic optimal control problems — even with known
models, noise statistics, and cost functions — value functions are very hard to
compute because of continuous state and action spaces and state-dependent action
sets. We developed a theory of empirical dynamic programming for such problems
and a general framework for establishing consistency of the algorithm as sample
size and the size of the function-approximating class grow. More recently, we
derived a sample-complexity bound for offline reinforcement learning with an
i.i.d. data-collection process and continuous state and action spaces.

## Mechanism design and pricing algorithms

We are developing auction theory for single and multiple goods that are produced
randomly but cannot be stored — renewable energy, time (idle time on cloud
machines), and human attention. We are building a new theory of menu auctions
for such settings, modeled as a Stackelberg game between consumers (followers)
and producers (leaders), and using it to derive menus of items and the
corresponding pricing algorithms.

## Game theory

In bimatrix games, a long-standing open problem is to characterize the games
solvable in polynomial time. Rank-0 and rank-1 games are solvable with linear
programs, but rank-2 and higher games are PPAD-complete. We completely
characterized a class of games that are strategically equivalent to rank-0 or
rank-1 games, and consequently characterized the class of polynomially solvable
games. We further proposed the notion of a best-response bijection and derived
an algorithm to compute an approximate Nash equilibrium of general games using
linear programs.

## Applied probability theory for learning theory

Many algorithms in machine learning and reinforcement learning can be viewed as
iterated random operators applied to an initial point in a Polish space. We have
developed a unified framework to characterize the convergence and consistency of
such algorithms by extending the theory of iterated random operators. Along the
way we introduced the notion of a **Wasserstein divergence** between measures
over Polish spaces, identified sufficient conditions under which contraction
operators under this divergence have a limit, and substantially generalized the
convergence properties of optimization algorithms to infinite-dimensional
settings.

# Applications

## Security of cyberphysical systems

Cyberphysical systems couple networked computers with physical systems —
autonomous vehicles, drones, advanced manufacturing, and more. Because they
acquire so much information from their environment, they are susceptible to
remote attacks. We use the statistical theory of change detection to derive new
algorithms for attack detection, including a dynamic watermarking algorithm for
finite Markov decision problems.

## Transportation markets

Transportation is growing through shared mobility, connectivity, and
electrification, but the industry is fragmented. We identify the best business
models and pricing mechanisms for delivering seamless service to passengers. We
have proposed frameworks for fair pricing in ridehailing systems and for
designing multimodal transportation systems, and we are actively working on
scheduling electric-vehicle charging with renewable energy and on pricing for
battery-swapping.

## Electricity markets

We design market mechanisms that let generators and load-serving entities bid
profitably and mitigate risk under deep renewable integration.

![Electricity market under deep renewable integration]({{ '/assets/images/electricity_market_dakhil.png' | relative_url }})

Renewable energy is a clean, economical alternative to traditional generation,
but integrating it into the existing grid introduces new challenges. Existing
markets are designed for dispatchable fossil and nuclear generation and can
absorb small amounts of renewables — but when random renewable sources supply a
substantial share of demand, the market structure must change to keep the grid
reliable. Our research designs innovative market mechanisms that account for the
stochastic nature of renewable generation and mitigate the high imbalance costs
that come with deeper integration. Using stochastic programming and auction
theory, a generator can compensate any shortfall in generation and still make a
positive payoff: the optimal contracted amount turns out to be a function of the
inverse CDF of the renewable energy, and this allocation together with a
Myerson payment rule elicits truthful bidding from buyers.

## Energy optimization of connected autonomous vehicles

We design reinforcement-learning methods for optimizing the fuel consumption of
autonomous vehicles, exploiting V2V and V2I information to compute the
best velocity profile.
