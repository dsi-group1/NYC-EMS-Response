# Predicting Emergency Medical Services Call Volume in New York City

### DSI 2-22-E Project 5, Group 1
* Chris Caress
* Christina Holland
* Ashley Poon
* David Romo

## Executive Summary  

### Prologue: Evolution of the Problem Statement

Original Problem Statement: What is the relationship between EMS response time and weather, special events, and traffic?  While there are plenty of factors outside a person’s circle of control it is still reasonable to think that we can have plans in place to counteract the unexpected.  Using predictive modelling we hope to be able to provide guidance on how best to account for uncontrolled events to improve EMS response times.  

The dataset (especially after merging EMS with weather data) was very feature rich and had many obervations. In order to be able to work with the data, we subsampled it at every 1000th row. After data cleaning, we had 20026 rows (each row is a unique EMS call) and 847 columns, with no NULL values remaining.
 
Modeling was done on this data to try to predict the response time, as defined by the time between making the 911 call and responders arriving at the scene. We used a variety of models, from linear regression to neural nets, and we were able to capture 58% of the variance (R2=0.58) on unseen data, with an RMS of 5.3 minutes. This does beat the NULL model, which captures 0% of the variance and has an RMS error of 8.1 minutes on unseen data. However, we decided that the bias in our models was still too high to be truly useful, and that the data we were able to find would not be able to significantly improve this, so we shifted to a new problem statement:

### New problem statement: 

Can we predict emergency call volume in NYC using time, weather, and traffic data? While these features are beyond our control, the goal of this project is to increase preparedness for a surge in emergency services given specific conditions. Using predictive modeling, we hope to be able to provide an indication of when the city should increase staff in emergency call centers or even on response teams.

### Cleaning & Pre-processing:

The EMS call data was agregated into call volume per hour for every hour between Jan 1, 2010 and December 31, 2019, and merged with daily temperature and precipitation data from a Central Park weather station and hourly traffic incidence numbers for New York city.

We removed any unnecessary columns including Unnamed: 0, STATION, NAME, and Date, as well as AWND which has null values. We also removed any correlated columns including all the boroughs which add up to num_calls and TMAX / TMIN which was used to calculate TAVG.
We set X to all the remaining features and y to num_calls, train/test split the data, and then scaled the train and test Xs.

### Modeling:

#### Baseline:

The baseline model is that the call volume is always equal to the mean call volume of the train set. The R2 of the baseline is 0 for train, -1.8x10-5 for test (so the baseline accounts for 0% of the variance). The RMS of the baseline is 54.2 calls/hour for the train, and 54.3 calls/hour for the test.

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

needs to be added

### Streamlit app

needs to be added