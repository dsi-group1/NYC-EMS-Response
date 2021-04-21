import streamlit as st
import pickle

# TO DO:
# - pickle final working model

# app title
st.title('NYC EMS Call Volume')

# About Section
about = ''
st.write(f'{about}')

# Model Section
st.write('Predict the EMS Call Volume in NYC:')

# sliders for each model param:

hour = st.slider('Hour',0,24)

temp = st.slider('Temp (F)',0,105)

incidences = st.slider('Incidences',0,53) #get actual range for this

day = st.slider('Day',1,31)

month = st.slider('Month',1,12)

year = 2017

prcp = st.slider('Percipitation',1,6)

snwd = st.slider('Snow Depth (inches)',1,24)

snow = st.slider('Snow (inches)',1,36)

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