# Predicting Emergency Medical Services Call Volume in New York City

### DSI 2-22-E Project 5, Group 1
* Chris Caress
* Christina Holland
* Ashley Poon
* David Romo

## Executive Summary  

* Original Problem Statement: What is the relationship between EMS response time and weather, special events, and traffic?  While there are plenty of factors outside a person’s circle of control it is still reasonable to think that we can have plans in place to counteract the unexpected.  Using predictive modelling we hope to be able to provide guidance on how best to account for uncontrolled events to improve EMS response times.  

* The dataset (especially after merging EMS with weather data) was very feature rich and had many obervations. In order to be able to work with the data, we subsampled it at every 1000th row. After data cleaning, we had 20026 rows (each row is a unique EMS call) and 847 columns, with no NULL values remaining.
 
* Modeling was done on this data to try to predict the response time, as defined by the time between making the 911 call and responders arriving at the scene. We used a variety of models, from linear regression to neural nets, and we were able to capture 58% of the variance (R2=0.58) on unseen data, with an RMS of 5.3 minutes. This does beat the NULL model, which captures 0% of the variance and has an RMS error of 8.1 minutes on unseen data. However, we decided that the bias in our models was still too high to be truly useful, and that the data we were able to find would not be able to significantly improve this, so we shifted to a new problem statement:

* New problem statement: Can we predict emergency call volume in NYC using time, weather, and traffic data? While these features are beyond our control, the goal of this project is to increase preparedness for a surge in emergency services given specific conditions. Using predictive modeling, we hope to be able to provide an indication of when the city should increase staff in emergency call centers or even on response teams.

* The EMS call data was agregated into call volume per hour for every hour between Jan 1, 2010 and December 31, 2019, and merged with daily temperature and precipitation data from a Central Park weather station and hourly traffic incidence numbers for New York city.

* Modeling .....

* Results ..... Model performance and important features

* Results ..... Streamlit app
