import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from math import sqrt


# app title
st.title('NYC Emergency Call Volume Estimator')

# About Section
st.write('''Can we predict emergency call volume in NYC using time, weather, and traffic data? While these features are beyond our control, the goal of this project is to increase preparedness for a surge in emergency services given specific conditions. Using predictive modeling, we hope to be able to provide an indication of when the city should increase staff in emergency call centers or even on response teams.
___
### Data Dictionary:

| Feature                   | Notes                                         |
| ---                       | ---                                           |
| Hour                      | Hour of the day (0-23)                        |
| Temp (F)                  | Temperature in Fahrenheit                     |
| Incidences                | Number of traffic incidents within the hour   | 
| Day                       | Day of the month (1-31)                       |
| Month                     | Month of the year (1-12)                      |
| Precipitation             | Precipitation by intensity (1-3 : L,M,H)      |
| Snow Depth                | Snow depth on ground in inches                |
___
### Datasets:

[EMS](https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj) | [Weather](https://www.ncdc.noaa.gov/cdo-web/search) | [Traffic](https://data.ny.gov/Transportation/511-NY-Events-Beginning-2010/ah74-pg4w)

### Contributors:
[Chris Caress](https://www.linkedin.com/in/chris-caress-4245a51b5/) | [Christina Holland](https://www.linkedin.com/in/christina-holland-7400a1140/) | [Ashley Poon](https://www.linkedin.com/in/ashley-poon-y95/) | [David Romo](https://www.linkedin.com/in/daromo/)

''')


# sliders for each model param:
st.sidebar.write('## Use the sliders to predict the EMS Call Volume in NYC.')

hour = st.sidebar.slider('Hour',0,23)

TAVG_CALC = st.sidebar.slider('Temp (F)',0,105)

Traffic_Incidents = st.sidebar.slider('Traffic Incidents',0,53) #get actual range for this

day = st.sidebar.slider('Day',1,31)

month = st.sidebar.slider('Month',1,12)

PRCP = st.sidebar.slider('Precipitation',0,2)

year = 2016 

SNWD = st.sidebar.slider('Snow Depth (inches)',0,24)

AWND = 5.349867675607344

SNOW = 0.08702925584135096

TMAX = 65.41562929511093

TMIN = 50.76893775770666

params = [[hour, TAVG_CALC, Traffic_Incidents, day, month, PRCP, year, SNWD, AWND, # slider params
           SNOW, TMAX, TMIN ]] # hard-coded params

# import  model
loaded_model_h5 = tf.keras.models.load_model('./resources/NYC-st-app-model_h5')

# scale params
ss = StandardScaler()
stand_scalar =  ss.fit(params)     
results = stand_scalar.transform(params)

# # params = ss.fit(params)
# params = ss.fit_transform(params)

# make prediction
prediction = loaded_model_h5.predict(params)
    
st.sidebar.write(f'Call volume is predicted to be **{int(sqrt(prediction))}** calls for specified hour.')
