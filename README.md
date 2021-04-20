# Predicting Emergency Medical Services Call Volume in New York City

### DSI 2-22-E Project 5, Group 1
* Chris Caress
* Christina Holland
* Ashley Poon
* David Romo

## Problem Statement  

#### Can we predict emergency (EMS) call volume in NYC using time, weather, and traffic data? 

While these features are beyond our control, the goal of this project is to increase preparedness for a surge in emergency services given specific conditions. Using predictive modeling, we hope to be able to provide an indication of when the city should increase staff in emergency call centers or even on response teams.

## Table of Contents - TBD after the repo is reorganized

## [Click Here for the Executive Summary](ExecSummary.md)

## Data

#### Datasets


__EMS call data: https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj__

The entire EMS call and response dataset is extremely large, so we saved it into separate files for each year, 2010-2019 for ease of manipulation. This year range was chosen to align with the weather and traffic data. The timestamp column is parsed into year, month, day, and hour, and AM/PM, and the hour column is then converted to a 24 hour clock using the hour and AM/PM values. Then, nested loops were used to go through each year (2010-2019), month (1-12), day (1-31), and hour (0-23), and calculate both the total number of EMS calls within that hour timeframe and the number of calls within each borough. If the total call volume on a given month/day/hour is zero, that row was not recorded, to prevent rows for Feb 30th and similar non-existent days.


__Weather data: https://www.ncdc.noaa.gov/cdo-web/search__

We requested daily weather data for the New York area from Jan 1, 2005 to Jan 3, 2021. We were only able to pull data for ~3 years at a time, and concatenated the individual files using pandas. The data we pulled were collected from hundreds of stations in the area, and we decided to filter for the Central Park station only as that is a good indicator of weather in New York City overall, and also had a more comprehensive dataset. 

For cleaning, we took the date column (formatted as YYYY-MM-DD) and created new columns for YEAR, MONTH, and DAY which could then be used to join with the hourly call data. We also noticed that the majority of the average temperature (TAVG) column was missing, and created a new column which calculated the average temperature based on max and min temperatures for the day.

__Traffic data: [source needed]__

This data contains traffic incidents in New York from 2010 to 2016. We removed all incidents outside of the five boroughs (Manhattan, Queens, Brooklyn, Bronx, and Staten Island) since we’re focusing on NYC only. Similar to weather, we created YEAR, MONTH, and DAY columns, however we also created an HOUR  column to look at traffic incidents by hour.  We then used groupby to create a new dataframe with the number of traffic incidents by year, month, day, and hour to join with the hourly call + weather data. 

#### Data Dictionary:


A problem statement.
A succinct formulation of the question your analysis seeks to answer.
A table of contents, which should indicate which notebook or scripts a stakeholder should start with, and a link to an executive summary.
A paragraph description of the data you used, plus your data acquisition, ingestion, and cleaning steps.
A short description of software requirements (e.g., Pandas, Scikit-learn) required by your analysis.
