# 2025-MCM/ICM competition (Problem C: Olympic medal table model)

### Our solution
- For Task 1, we developed a Zero-Inflated Negative Binomial Model. This model utilizes a
 logistic regression-based zero-inflation mechanism, coupled with a short-term dynamic feature-driven
 negative binomial count distribution. By integrating Monte Carlo simulations and adaptive adjustment
 strategies, we predict and differentiate countries that have never won a medal from those that have.
 Moreover, we estimate the probabilities of each outcome along with the confidence intervals for the
 predictions.
- For Task 2, we quantified the relationship between the number or type of events and medal out
comes using a panel regression model. Next, we employed the dynamic Herfindahl-Hirschman In
dex (HHI) to quantify the significance of specific events to the countries involved and identified the
 core global events that have the most widespread impact. Finally, a Difference-in-Differences (DID)
 model was used to estimate the effects of hosting country status and the number of events on medal
 outcomes.
- For Task3, weproposedanARIMAX-XGBoosthybridresidualregressionmodel. Thisapproach
 combines linear time series modeling with nonlinear feature learning to predict Olympic medal distri
butions. We innovatively constructed an exogenous variable prediction mechanism using a sliding
 window to address the data gap caused by the four-year Olympic cycle. The model’s robustness was
 enhanced through a dual regularization framework, and dynamic confidence intervals were constructed
 by using Bootstrap resampling.
- For Task 4, we began by defining events that could potentially produce a ”Great Coach” effect.
 Wethen employed a mixed-effects model to quantify the impact of this effect. Initially, we established
 a baseline model excluding the ”Great Coach” variable. We then introduced the ”Great Coach” effect
 into the model and applied a Likelihood Ratio Test (LRT) to compare the performance of the model
 with and without the ”Great Coach” variable.

