import streamlit as st
import pickle

# TO DO:
# - pickle final working model

# app title
st.title('NYC EMS Call Volume Estimator')

# About Section
about = ''
st.write(f'{about}')

# Model Section
st.write('''Can we predict emergency call volume in NYC using time, weather, and traffic data? While these features are beyond our control, the goal of this project is to increase preparedness for a surge in emergency services given specific conditions. Using predictive modeling, we hope to be able to provide an indication of when the city should increase staff in emergency call centers or even on response teams.

Experiment the paramaters on the left to understand how features impact call volume.''')


# sliders for each model param:
st.sidebar.write('Use the sliders to predict the EMS Call Volume in NYC.')
hour = st.sidebar.slider('Hour',0,24)

temp = st.sidebar.slider('Temp (F)',0,105)

incidences = st.sidebar.slider('Incidences',0,53) #get actual range for this

day = st.sidebar.slider('Day',1,31)

month = st.sidebar.slider('Month',1,12)

year = 2017

prcp = st.sidebar.slider('Percipitation',1,6)

snwd = st.sidebar.slider('Snow Depth (inches)',1,24)

snow = st.sidebar.slider('Snow (inches)',1,36)

params = [[hour, temp, incidences, day, month, year, prcp, snwd, snow]]

# import pickled model
model = pickle.load(open('../modeling/app-model.pkl', 'rb'))

# make prediction
prediction = model.predict(params)

if prediction > 0 and prediction < 105:
    level = 'LOW'

if prediction > 106 and prediction < 326:
    level = 'AVERAGE'
    
if prediction > 326:
    level = 'HIGH'
    
st.write(f'Call volume is predicted to be: {int(prediction)}')
st.write(f'This is {level} for NYC.')