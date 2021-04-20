import streamlit as st
import pickle

# TO DO:
# - link sliders w/ model input params
# - pickle final working model
# - map (if time)

# app title
st.title('NYC EMS Call Volume')

# About Section
about = ''
st.write(f'{about}')

# Model Section
st.write('Predict the EMS Call Volume in NYC:')

# set equal to filename of pickled (saved) model
# p_file = 'MODEL_NAME.pkl'

# open pickle w/ f-string
# with open(f'../models/{p_file}', mode='rb') as pickle_in:
#     pipe = pickle.load(pickle_in)

# model = pipe.predict()

# # sidebar constructor
# page = st.sidebar.selectbox(
# 'Select a page:',
# ('Page 1', 'Page 2')
# )

# Page Desgins================

# page 1
# if page == 'Page 1':
    
# page 2
# if page == 'Page 2':

    
# # button example
# st.button('Click here for free money!')

# # slider example
# st.slider('How much money you want?',1,1000)

    