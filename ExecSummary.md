# Predicting Emergency Medical Services Call Volume in New York City

### DSI 2-22-E Project 5, Group 1
* Chris Caress
* Christina Holland
* Ashley Poon
* David Romo

## Executive Summary  

### Background

We are interested in helping NYC officials respond more successfully to the emergency calls that come in.

The aspects of the NYC EMS response we were interested in initially were (a) the factors impacting response time after an EMS call, and (b) predicting the volume of calls that come in to the call centers.

We used a variety of models, from linear regression to neural nets, to attempt to predict the response time. We were able to capture 58% of the variance (R2=0.58) on unseen data, with an RMSE of 5.3 minutes. This does beat the NULL model, which captures 0% of the variance and has an RMSE of 8.1 minutes on unseen data. However, with the data currently available, the bias in our models was still too high to be truly useful. We did find that travel time was the majority of the response time in almost every call, but additional data (particularly related to traffic patterns) is needed to fully address this aspect of the problem.

For the current project, then, we will focus on examining and predicting call volume.

### Problem Statement 

Can we predict emergency call volume in NYC using time, weather, and traffic data? While these features are beyond our control, the goal of this project is to increase preparedness for a surge in emergency services given specific conditions. Using predictive modeling, we hope to be able to provide an indication of when the city should increase staff in emergency call centers or even on response teams.

### Cleaning & Pre-processing

The EMS call data was aggregated into call volume per hour for every hour between Jan 1, 2010 and December 31, 2019, and merged with daily temperature and precipitation data from a Central Park weather station and hourly traffic incidents for New York City.

We removed any unnecessary columns including Unnamed: 0, STATION, NAME, and DATE, as well as AWND which has null values. We also removed any correlated columns including all the boroughs which add up to num_calls and TMAX / TMIN which was used to calculate TAVG.

We set X to all the remaining features and y to num_calls, train/test split the data, and then scaled the train and test Xs.

### Modeling

#### Baseline:

The baseline model is that the call volume is always equal to the mean call volume of the train set. The R2 of the baseline is 0 for train, -1.8x10-5 for test (so the baseline accounts for 0% of the variance). The RMSE of the baseline is 54.2 calls/hour for the train, and 54.3 calls/hour for the test.

#### Initial: Linear regression model

We first fit a basic linear regression model with default parameters. The model had a train r2 score of 0.51 and a test r2 score of 0.52. While there is no overfitting, this was not a strong model. We used this model to take an initial look at the coefficients and which features had the greatest impact on the number of calls. 

| features                        | coefs     |
|---                              | ---       |
| hour (0-23)                     | 34.665246 |
| Incidences (traffic)            | 10.747473 |
| TAVG_CALC (Average temperature) | 3.471342  |
| SNWD (snow depth)               | 1.585477  |
| month (1-12)                    | 0.925722  |
| year (2010-2019)                | 0.690116  |
| SNOW (snowfall)                 | 0.458211  |
| PRCP (precipitation)            | -0.606640 |
| day (1-31)                      | -1.185278 |

#### Random forest model & feature importances

Next, we ran a gridsearch with a random forest model and various n_estimators and max_depth parameters. The best performing model was a random forest with a max_depth of  5 and n_estimators of 250.  The model had train and test r2 scores of 0.81 and a RMSE of 24 calls. Overall, this model had a relatively high score with no overfitting. We then looked at the feature importances which were similar to what we saw with the coefficients in the linear regression.

| features                        | importance|
|---                              | ---       |
| hour (0-23)                     | 0.787306  |
| TAVG_CALC (Average temperature) | 0.054226  |
| Incidences (traffic)            | 0.043073  |
| day (1-31)                      | 0.040666  |
| month (1-12)                    | 0.026652  |
| year (2010-2019)                | 0.024473  |
| PRCP (precipitation)            | 0.017919  |
| SNWD (snow depth)               | 0.004524  |
| SNOW (snowfall)                 | 0.00116  |

#### Neural net & predictive power

We wanted to see if we could improve upon the predictive power of the Random Forest model, and so we built a Neural Net with 3 dense layers to produce a prediction as close as possible to the actual call volume.  The batch_size was kept relatively small at 100 compared to the full data set to give the model ample ability to re-train on enough batches.  Epochs certainly hit a point of diminishing returns since an increase from 100 to 250 only produced a change of 0.01 increase in r2 score.  This is still an improvement and we kept epochs at 250. 

Below is a quick summary showing performance between the train and test datasets.

| Model Type       | Metric    | Train   | Test     |
|---               |---        |---      |---       |
| Dense Neural Net | R2        |0.85637  | 0.84209  |
| Dense Neural Net | RMSE      |20.54    | 21.59    |
| Dense Neural Net | MAE       |15.9181  | 16.7103  |
| Dense Neural Net | Loss(MSE) |436.0501 | 466.2715 |

In addition the minimum, quartile 1, median, and quartile 3 are close between the actual test call volume and the neural net predictions. There is a small difference in the minimum, but it is less than the RMSE.  Where we start to get more inaccurate is at the top end of our data where call volume far exceeds what we would normally see.  In this case the true number of calls doubles from the 3rd to 4th quartile, and the model does not predict these outlying values. 

With this neural net model, we can account for about 84% of variance. This is encouraging when it comes to forecasting call volumes. While we would like to reach or surpass 85% of the variance, we appear to be hitting about the limit of our available data (based on multiple types of models).

### Streamlit App

It is also useful to be able to predict call volume based on specific values of the relevant features. For that purpose, we have created a Streamlit app to allow any user to input hour, day, month, traffic incidents, average temperature, and precipitation and obtain a prediction of the expected NYC EMS hourly call volume. For this app, we used the neural net model, since it has the greatest predictive power.

### Summary

Our neural net model is well aligned with the expected outcome, except at the extreme of call volume seen in the data set.  There will always be emergency situations (natural weather events, national emergency situations, etc.) that cannot be properly accounted for, but that is beyond the scope of the current project. Our goal is to help NYC Emergency Management predict normal variability in EMS call volume, and make sure that staff is allocated effectively.  This model is not designed for interpretability because there is no control that can really be had over the inputs.  Weather cannot be controlled, traffic is very difficult to control, and until further breakthroughs occur in science, we cannot control time either. 

For NYC Emergency Management, we do not need interpretability. The predictive power of the neural net model has been input into the StreamLit app, ready for immediate use.

The Random Forest model R2 and RMSE scores were not quite as good as the neural net, it nevertheless explains 81% of the variance in hourly call volume, and gives us interpretability. This is important as it helps guide our next steps. 

### Recommendations

* __Immediate Use:__  Using weather forecasts and our model, create a 'heat map' of staff needed and schedule people accordingly.  If number of calls are known then it is a quick jump to use that for staffing projections.  This will help to prevent having people on duty when they are not needed and avoid the reverse situation.  If implemented well this should help to avoid preventable deaths.

* __Further research:__  We do have a few areas we would like to look into in the future:
    1. __Historical traffic density and traffic incident type:__  As it is right now, we know how many incidents happen but not the severity or the overall effect these have on traffic.  Using traffic density and type we believe we can improve on our models predictability and cut down on the RMSE. It might also help us approach the 'response time' prediction aspect of improving NYC EMS response.
    2. __Research into ‘average handling times’ for EMS:__  This would help the model to be a little better on predicting how much staff is needed since it doesn’t need to be a 1:1 staff to emergency ratio. 