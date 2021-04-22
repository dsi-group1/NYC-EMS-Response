# This script loops through the years 2010-2019. 
# For each year, the year's data is loaded in, and then the totals call volume is computed on an hourly basis.

#imports:
import numpy as np
import pandas as pd

# list of years for which we are aggregating the hourly call volumes
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# initialize an empty list (will be a list of dictionaries)
hourly_counts = []

# loop over years:
for year0 in years:
    
    # load in the year's data file, and immediately drop all columns except time and borough,
    # since we are aggregating:
    file_in = f'../../yearlyfiles/ems{year0}.csv'
    df = pd.read_csv(file_in)
    df = df[['INCIDENT_DATETIME', 'BOROUGH']]
    
    # output for my sanity:
    print(f'loaded in data for {year0}.')
    
    # break the tmestamp column into year, month, day, and hour:
    time_strings = df['INCIDENT_DATETIME']
    years = [pd.to_numeric(s[6:10])  for s in time_strings]
    months= [pd.to_numeric(s[0:2])   for s in time_strings]
    days  = [pd.to_numeric(s[3:5])   for s in time_strings]
    hours = [pd.to_numeric(s[11:13]) for s in time_strings]
    
    # convert hours to 24 hour clock by adding 12 if "PM":
    PM    = [(s[20:22]=='PM')       for s in time_strings]
    hours = [hr+12 if PM[n] else hr for n,hr in enumerate(hours)]
    # the line above makes 12 noon - 12:59 pm hour 24, should be 12,
    # and 12 midnight - 12:59 am hour 12, should be 0. So a quick fix to that:
    hours = [0 if hr==12 else hr for hr in hours] 
    hours = [12 if hr==24 else hr for hr in hours]
    # This sets hour = 0-23.
    
    # add year, month, day and hour to the dataframe to make counting easier:
    df['year'] = years
    df['month']= months
    df['day']  = days
    df['hour'] = hours

    # another output for sanity:
    print(f'Organized and ready to count for {year0}.')
    
    # list the possible values of the boroughs column,
    # hardwired just in case one of the years was missing a borough, so the code won't break:
    boroughs = ['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'RICHMOND / STATEN ISLAND', 'UNKNOWN']

    # loop over months:
    for m in range(12):
        month0 = m + 1
        # loop over days, 1-31 -- if there are < 31 days in a month, the count will just return 0
        for d in range(31):
            day0 = d + 1
            # loop over hours (now on 24 hour clock) :
            for hour0 in range(24):
                # get total count of ALL NYC calls for that year/month/day/hour combo:
                chk = (df['month']==month0) & (df['day']==day0) & (df['hour']==hour0)
                cnt = df[chk].shape[0]
                # if total calls not >0, skip -- to avoid rows for Feb 30, 31, April 31, ... :
                if cnt>0:
                    # create dictionary of data to save for this year/month/day/hour:
                    new_dict = {
                        'year': year0,
                        'month': month0,
                        'day': day0,
                        'hour': hour0,
                        'num_calls': cnt
                    }
                    # also divide the total count into columns of count for each borough:
                    for borough in boroughs:
                        cnt_b = df[(df['BOROUGH']==borough) & chk].shape[0]
                        new_dict[borough] = cnt_b
                        
                    # append this hour's data to the list:
                    hourly_counts.append(new_dict)

            # output for sanity:
            print(f'{month0}/{day0}/{year0}.')
    
    # make a dataframe and save data after each year (in case the process is interrupted) :
    counts_df = pd.DataFrame(hourly_counts)
    save_file = f'./data/hourlycounts_through{year0}.csv'
    counts_df.to_csv(save_file)
    print(f'saved data through {year0}.')

    # This will make a file each time it finishes a year, with a new filename, but cumulative:
    # hourlycounts_through2010.csv is 2010 only,
    # hourlycounts_through2011.csv is 2010-2011, ...
    
    # Once hourlycounts_through2019.csv is successfully written (contains 2010-2019), the 
    # preceding files can be deleted. They exist purely as a failsafe.
    