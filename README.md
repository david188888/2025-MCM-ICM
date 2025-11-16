# 2025 MCM/ICM — Problem C: Olympic Medal Table Model

## Overview
This repository contains code and written solutions for the 2025 Mathematical Contest in Modeling (MCM) / Interdisciplinary Contest in Modeling (ICM), Problem C: modeling Olympic medal distributions and related analyses.

## Our Approach

### Task 1 — Zero‑Inflated Count Model
We developed a Zero‑Inflated Negative Binomial model with a logistic regression-based zero‑inflation component and a dynamic feature-driven negative binomial count distribution. Monte Carlo simulations and adaptive adjustment strategies were used to separate countries that have never won medals from those that have, and to estimate outcome probabilities with confidence intervals.

### Task 2 — Panel Regression & HHI
We quantified the relationship between the number/type of events and medal outcomes using panel regression. A dynamic Herfindahl‑Hirschman Index (HHI) was applied to measure event concentration and to identify core events with broad global impact. A Difference‑in‑Differences (DID) model was used to estimate the effects of host‑country status and event counts on medal outcomes.

### Task 3 — ARIMAX + XGBoost Hybrid
We propose an ARIMAX–XGBoost hybrid residual regression model that combines linear time‑series modeling with nonlinear feature learning to predict medal distributions. An exogenous variable prediction mechanism based on a sliding window handles the four‑year Olympic cycle data gap. Robustness is enhanced through dual regularization and bootstrap resampling is used to produce dynamic confidence intervals.

### Task 4 — "Great Coach" Mixed‑Effects Analysis
We defined candidate events likely to generate a "Great Coach" effect and used mixed‑effects modeling to quantify this impact. A baseline model (without the "Great Coach" variable) was compared to an extended model including the effect, and a Likelihood Ratio Test (LRT) was used to assess statistical significance.


## Awards
- Honorable Mention (H Award) — 2025 MCM/ICM
