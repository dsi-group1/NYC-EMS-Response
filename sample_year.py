# https://stackoverflow.com/questions/35295981/how-to-select-every-5th-row-in-a-csv-file-using-python

# This script runs through the (VERY LARGE) EMS dataset, and splits it into separate files for each year.

# We are selecting 2010-2019 to match with weather and traffic data.

# These files will later be used to compute hourly counts of EMS calls.

import csv

count = 0

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

for yr_wanted in years:
    
# open files and handle headers
    with open('./data/EMS_Incident_Dispatch_Data.csv') as infile:
        file_out = f'./data/ems{yr_wanted}.csv'
        with open(file_out, 'w') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            # iterate through file and write only every nth row
            for row in reader:
                year=int(row['INCIDENT_DATETIME'][6:10])
                count += 1
                if year==yr_wanted:
                    writer.writerow(row)
                if not count % 1000: 
                    print(f'Looking for {yr_wanted} rows, read {count} rows so far')
