# This script was used to get an initial subsample of the full EMS dataset, sampled every 1000th row.

# This data was to answer our original problem statement, predicting response time. It is no longer needed.

# https://stackoverflow.com/questions/35295981/how-to-select-every-5th-row-in-a-csv-file-using-python


import csv

count = 0

# open files and handle headers
with open('./data/EMS_Incident_Dispatch_Data.csv') as infile:
    with open('./data/emssubsample.csv', 'w') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        # iterate through file and write only every nth row
        for row in reader:
            count += 1
            if not count % 1000:
                writer.writerow(row)
                print(count)
