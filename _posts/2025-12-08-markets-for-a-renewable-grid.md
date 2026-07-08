---
title: "Designing markets for a grid that runs on weather"
date: 2025-12-08
author: Abhishek Gupta
tags: [mechanism-design, energy, electricity-markets, sustainability]
math: true
excerpt: "Today's electricity markets were built for generators you can switch on. Wind and solar answer to the weather instead — so the market itself has to be redesigned."
---

The electricity market is one of the most consequential mechanisms humans have
ever built, and it was designed for a world that is disappearing. Its assumptions
— that generation is *dispatchable*, that you can promise a megawatt and deliver
it — hold for coal, gas, and nuclear. They do not hold for wind and solar, whose
output answers to the weather. A grid with deep renewable penetration needs a
market that **prices uncertainty**, not one that pretends it away.

## The idea: pay for what you can actually deliver

Our starting point was auction design. In *Auctioning electricity under deep
renewable integration using a penalty for shortfall* (2019) and its predecessor
*Selling Renewable Generation with a Penalty for Shortfall* (2018), a renewable
generator sells energy it *might* produce, backed by a penalty if it falls short.
Using stochastic programming and auction theory, we found something clean: the
optimal contracted quantity is a function of the **inverse CDF** of the renewable
supply,

$$ q^\star = F^{-1}(\cdot), $$

and pairing that allocation with a Myerson-style payment rule makes **truthful
bidding** the buyers' best strategy. In other words, you can design the market so
that honesty is optimal even when supply is random.

The theme continues in *Equilibria in two-stage electricity markets* (2015) and
*Dynamic Economic Dispatch … under Ramping Constraints and Uncertain Demand*
(2018), which study how prices and dispatch evolve when both supply and demand
are uncertain and generators can't ramp instantly.

## Demand can flex, too

The other half of the answer is that demand no longer has to be passive.
Electric-vehicle charging is a huge, *flexible* load — it mostly cares that the
car is charged by morning, not about the exact hour. In *Scheduling EV charging
having demand with different reliability constraints* (2023) and *Preemptive
scheduling of EV charging for providing demand response services* (2023), we
schedule that flexibility to soak up renewable energy when it's abundant, turning
millions of cars into a grid-stabilizing resource. The idea goes back to
*Scheduling, pricing, and efficiency of non-preemptive flexible loads* (2015).

## Why it matters

Decarbonizing the grid is not only a hardware problem — it's a **market design**
problem. Panels and turbines are necessary; mechanisms that make variable supply
and flexible demand meet efficiently are what make them usable at scale. Good
mechanism design here is worth gigawatts.

## What it means going forward

As renewables become the cheapest generation on Earth, the binding constraint
shifts from cost to **coordination**: matching stochastic supply with shiftable
demand, moment to moment, without blackouts or waste. The principles compound
into the near future:

- **EV fleets and batteries** become active market participants, bidding
  flexibility the way generators bid capacity.
- **Truthful, uncertainty-aware mechanisms** matter more as the share of variable
  generation grows — the penalty-for-shortfall idea is one template.
- **AI-driven forecasting and bidding** will sit on top of these markets; the
  market rules decide whether that intelligence produces reliability or chaos.

Getting the rules right is quietly one of the highest-leverage things we can do
for the energy transition.

---

**Papers behind this post:** *Auctioning electricity under deep renewable
integration using a penalty for shortfall* (2019) · *Selling Renewable Generation
with a Penalty for Shortfall* (2018) · *Equilibria in two-stage electricity
markets* (2015) · *Dynamic Economic Dispatch … under Ramping Constraints and
Uncertain Demand* (2018) · *Scheduling EV charging having demand with different
reliability constraints* (2023) · *Preemptive scheduling of EV charging* (2023).
See them on the [Publications]({{ '/publications/' | relative_url }}) page and the
[renewable-markets project]({{ '/projects/renewable-markets/' | relative_url }}).
