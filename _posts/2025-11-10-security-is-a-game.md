---
title: "Security is a game: strategy against an intelligent adversary"
date: 2025-11-10
author: Abhishek Gupta
tags: [game-theory, security, privacy]
math: true
excerpt: "A smart attacker reasons about your defense. That single fact turns security from an engineering problem into a game — and game theory tells you how much information to give away, and how to spread thin resources."
---

There is a fundamental difference between defending against *noise* and defending
against an *adversary*. Noise is indifferent; an adversary reasons about what you
will do and best-responds to it. The moment your opponent is strategic, security
stops being pure engineering and becomes **game theory**. Much of my earlier work
lives in this space, and its lessons have aged well.

## Spreading resources thin: the Colonel Blotto problem

The classic model of allocating limited resources across many contested fronts is
the *Colonel Blotto* game. We used it as a lens on cyberphysical security in
*A Three-Stage Colonel Blotto Game with Applications to Cyber-Physical Security*
(2014) and its companions. A striking, counter-intuitive result runs through this
work — captured in the title *When to provide more information to an adversary*
(2014): sometimes **revealing** information is the optimal move, because it
shapes the attacker's incentives in your favor. Later, in *Colonel Blotto Game
with Coalition Formation for Sharing Resources* (2018), we asked when defenders
should pool resources at all.

## Jamming, control, and asymmetric information

A related thread treats communication and control under attack as a dynamic game.
Across *Optimal control in the presence of an intelligent jammer* (2010),
*One-stage control over an adversarial channel* (2011), *A dynamic
transmitter-jammer game with asymmetric information* (2012), and *Jamming in
mobile networks* (2013), the recurring theme is **asymmetric information**: the
two sides know different things, and the equilibrium hinges on who knows what.
That culminated in *Dynamic Games With Asymmetric Information and Resource
Constrained Players With Applications to Security of Cyberphysical Systems*
(2017).

## Privacy is an adversarial game too

The same framing illuminates privacy. In *Privacy-aware stochastic control with a
"snoopy" adversary* (2016), a controller must accomplish its task while an
eavesdropper tries to infer private state from observable behavior. The tension
is exactly a game: every action leaks a little information, so the optimal policy
trades performance against how much it reveals.

## Why it matters, now more than ever

Three implications carry into today's world:

- **Disclosure is a decision.** In an era of disinformation and cyber conflict,
  the counter-intuitive lesson — that sometimes you *should* reveal information —
  is a real strategic tool, not a paradox.
- **Adversarial ML is a security game.** Attacks that craft inputs to fool a
  model are strategic best-responses; defenses that assume random perturbations
  miss the point. The asymmetric-information framing is the right one.
- **Privacy leaks through behavior.** As systems act on our data, the "snoopy
  adversary" model — inferring secrets from what a system *does* — describes
  everything from smart-meter surveillance to fingerprinting a user by their app
  usage.

The unifying idea is simple to state and hard to internalize: **design against
the best response, not the average case.** $\max_{\text{defense}}
\min_{\text{attack}}$ is a better mental model for security than any fixed
threat list.

---

**Papers behind this post:** *Dynamic Games With Asymmetric Information … Security
of Cyberphysical Systems* (2017) · *A Three-Stage Colonel Blotto Game … Cyber-Physical
Security* (2014) · *… When to provide more information to an adversary* (2014) ·
*Colonel Blotto Game with Coalition Formation* (2018) · *Privacy-aware stochastic
control with a "snoopy" adversary* (2016) · the jammer-game series (2010–2013).
Browse them on the [Publications]({{ '/publications/' | relative_url }}) page.
