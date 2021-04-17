import numpy as np
import pandas as pd

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

hourly_counts = []

for year0 in years:
    
    file_in = f'./data/ems{year0}.csv'
    df = pd.read_csv(file_in)
    df = df[['INCIDENT_DATETIME', 'BOROUGH']]
    
    print(f'loaded in data for {year0}.')
    
    time_strings = df['INCIDENT_DATETIME']
    years = [pd.to_numeric(s[6:10])  for s in time_strings]
    months= [pd.to_numeric(s[0:2])   for s in time_strings]
    days  = [pd.to_numeric(s[3:5])   for s in time_strings]
    hours = [pd.to_numeric(s[11:13]) for s in time_strings]
    PM    = [(s[20:22]=='PM')       for s in time_strings]
    hours = [hr+12 if PM[n] else hr for n,hr in enumerate(hours)]

    df['year'] = years
    df['month']= months
    df['day']  = days
    df['hour'] = hours

    print(f'Organized and ready to count for {year0}.')
    
    boroughs = ['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'RICHMOND / STATEN ISLAND', 'UNKNOWN']

    for m in range(12):
        month0 = m + 1
        for d in range(31):
            day0 = d + 1
            for h in range(24):
                hour0 = h + 1
                chk = (df['month']==month0) & (df['day']==day0) & (df['hour']==hour0)
                cnt = df[chk].shape[0]
                if cnt>0:
                    new_dict = {
                        'year': year0,
                        'month': month0,
                        'day': day0,
                        'hour': hour0,
                        'num_calls': cnt
                    }
                    for borough in boroughs:
                        cnt_b = df[(df['BOROUGH']==borough) & chk].shape[0]
                        new_dict[borough] = cnt_b
                    hourly_counts.append(new_dict)

            print(f'{month0}/{day0}/{year0}.')
    counts_df = pd.DataFrame(hourly_counts)
    save_file = f'./data/hourlycounts_through{year0}.csv'
    counts_df.to_csv(save_file)
    print(f'saved data through {year0}.')
