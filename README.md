# Predicting Emergency Medical Services Call Volume in New York City

### Collaborators
* Chris Caress
* Christina Holland
* Ashley Poon
* David Romo

## Problem Statement  

#### Can we predict emergency call volume in NYC using time, weather, and traffic data? 

While these features are beyond our control, the goal of this project is to increase preparedness for a surge in emergency services given specific conditions. Using predictive modeling, we hope to be able to provide an indication of when the city should increase staff in emergency call centers or even on response teams.

## Table of Contents

| folder | file | notes |
|---|---|---|
| | | |
| Main Directory | README.md | (current file) |
|                | [ExecSummary.md](ExecSummary.md) | Process, Summary, and Recommendations 
| | | |
| data           | hourlycalls_through2019.csv | call volume |
|                | cntrlprk_weather.csv | weather | 
|                | hourlycalls_weather.csv | call volume + weather |
|                | traffic_subsample.csv | traffic |
|                | hourlycalls_weather_traffic.csv | call volume + weather + traffic |
| | | |
| cleaning_eda   | ems_sample_year.py | sampled the full EMS calls file to make yearly files |
|                | ems_hourly_calls.py | aggregates total hourly call volume for 2010-2019 |
|                | merge_hourlycalls_weather.ipynb | merge hourly calls with weather |
|                | merge_hourlycalls_weather_traffic.ipynb | merge hourly calls + weather with traffic |
|                | feature_quartile_eda.ipynb | eda of features |
| | | |
| modeling       | hourlycalls_weather_initialmodels.ipynb | lin. regression + NN    |
|                | linreg_ensemble_models.ipynb  | lin. regression + RF              |
|                | neural_net_final.ipynb | neural net models                        |
|                | app-model.pkl | The model saved for use in the StreamLit app      |
| | | |
| app            | NYC-st-app.py | code for StreamLit app                            |
| | | |
| archive        | *multiple*    | yielded insight, but not part of the main project |


#### [Click Here for the Executive Summary](ExecSummary.md)

## Data

#### Datasets


__EMS call data: https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj__

The entire EMS call and response dataset is extremely large, so we saved it into separate files for each year, 2010-2019 for ease of manipulation. This year range was chosen to align with the weather and traffic data. The timestamp column is parsed into year, month, day, and hour, and AM/PM, and the hour column is then converted to a 24 hour clock using the hour and AM/PM values. Then, nested loops were used to go through each year (2010-2019), month (1-12), day (1-31), and hour (0-23), and calculate both the total number of EMS calls within that hour timeframe and the number of calls within each borough. If the total call volume on a given month/day/hour is zero, that row was not recorded, to prevent rows for Feb 30th and similar non-existent days.


__Weather data: https://www.ncdc.noaa.gov/cdo-web/search__

We requested daily weather data for the New York area from Jan 1, 2005 to Jan 3, 2021. We were only able to pull data for ~3 years at a time, and concatenated the individual files using pandas. The data we pulled were collected from hundreds of stations in the area, and we decided to filter for the Central Park station only as that is a good indicator of weather in New York City overall, and also had a more comprehensive dataset. 

For cleaning, we took the date column (formatted as YYYY-MM-DD) and created new columns for YEAR, MONTH, and DAY which could then be used to join with the hourly call data. We also noticed that the majority of the average temperature (TAVG) column was missing, and created a new column which calculated the average temperature based on max and min temperatures for the day.

__Traffic data:  https://data.ny.gov/Transportation/511-NY-Events-Beginning-2010/ah74-pg4w__ 

This data contains traffic incidents in New York from 2010 to 2016. We removed all incidents outside of the five boroughs (Manhattan, Queens, Brooklyn, Bronx, and Staten Island) since we’re focusing on NYC only. Similar to weather, we created YEAR, MONTH, and DAY columns, however we also created an HOUR  column to look at traffic incidents by hour.  We then used groupby to create a new dataframe with the number of traffic incidents by year, month, day, and hour to join with the hourly call + weather data. 

#### Data Dictionary for Merged Dataset:

| Column                    | Non-Null Count  | Datatype  | Notes                                         |
| ---                       | ---             | ---       | ---                                           |
| year                      | 25465 non-null  | int64     | year (2010-2019)                              |
| month                     | 25465 non-null  | int64     | month of the year (1-12)                      |
| day                       | 25465 non-null  | int64     | day of the month (1-31)                       |
| hour                      | 25465 non-null  | int64     | hour of the day (0-23)                        |
| num_calls                 | 25465 non-null  | int64     | number of total NYC EMS calls within the hour |
| BRONX                     | 25465 non-null  | int64     | number of Bronx EMS calls                     |
| BROOKLYN                  | 25465 non-null  | int64     | number of Brooklyn EMS calls                  | 
| MANHATTAN                 | 25465 non-null  | int64     | number of Manhattan EMS calls                 |
| QUEENS                    | 25465 non-null  | int64     | number of Queens EMS calls                    |
| RICHMOND / STATEN ISLAND  | 25465 non-null  | int64     | number of Richmond/Staten Island EMS calls    |
| UNKNOWN                   | 25465 non-null  | int64     | number of EMS calls from unknown borough      |
| STATION                   | 25465 non-null  | object    | weather station ID                            |
| NAME                      | 25465 non-null  | object    | weather station name                          |
| DATE                      | 25465 non-null  | object    | date                                          |
| AWND                      | 25241 non-null  | object    | average wind speed in mph                     |
| PRCP                      | 25465 non-null  | float64   | precipitation in inches                       |
| SNOW                      | 25465 non-null  | float64   | snow (falling) in inches                      |
| SNWD                      | 25465 non-null  | float64   | snow depth on ground in inches                |
| TMAX                      | 25465 non-null  | float64   | max temperature in degrees Fahrenheit         |
| TMIN                      | 25465 non-null  | float64   | min temperature in degrees Fahrenheit         |
| TAVG_CALC                 | 25465 non-null  | float64   | (max temp + min temp)/2                       |
| Incidences                | 25465 non-null  | int64     | number of traffic incidents within the hour   |


#### Software Requirements:

| Purpose                | Libraries  | Import Statements                                                                 |
| ---                    | ---        | ---                                                                               | 
| ETL                    | pandas     | import pandas as pd                                                               |
|                        | numpy      | import numpy as np                                                                |
|                        | datetime   | from datetime import timezone                                                     |
|                        |            | import datetime                                                                   |
|                        | time       | import time                                                                       |
|                        | os         | import os                                                                         |
| Plotting and EDA       | matplotlib | import matplotlib.pyplot as plt                                                   |
|                        | seaborn    | import seaborn as sns                                                             |
| Modeling               | sklearn    | from sklearn.model_selection import train_test_split, GridSearchCV                |
|                        |            | from sklearn.linear_model import LinearRegression, Lasso, Ridge, LassoCV, RidgeCV |
|                        |            | from sklearn.svm import LinearSVR                                                 |
|                        |            | from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor             |
|                        |            | from sklearn.preprocessing import StandardScaler, PolynomialFeatures              |
|                        |            | from sklearn.metrics import r2_score, mean_squared_error                          |
|                        |            | from sklearn.pipeline import Pipeline                                             |
|                        | tensorflow | from tensorflow.keras.models import Sequential                                    |
|                        |            | from tensorflow.keras.layers import Dense, Input                                  |


