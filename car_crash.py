import csv
import time
from datetime import datetime
from matplotlib import pyplot as plt
from collections import defaultdict

def main():

    dates, possiblinj = [], []
    previous_year_month, pos_inj = (0,0), 0

    with open('cpd-crash-incidents.csv', 'r') as crash:
        car_crash_reader = csv.DictReader(crash, delimiter = ';')
        header = next(car_crash_reader)
        # years = ['year_month']['incidents']
        years = {}
        incidents = 0
        for row in car_crash_reader:

            year_month = str('-'.join([row['year'],row['month']]))
            year_month = datetime.strptime(year_month, '%Y-%m')

            if year_month not in years:
                years.update({year_month:0})

            years[year_month] += int(row['possblinj'])

            dates, incidents = dict_to_tables(years)
    #
    fig = plt.figure(dpi=128, figsize=(10,6))
    # fig, ax = plt.subplots()

    plt.bar(dates,incidents)
    plt.locator_params(axis='x', nticks=10)

    plt.title('Car Crashes monthy in Iowa', fontsize=20)
    plt.xlabel('Years and months', fontsize=14, rotation=90)
    fig.autofmt_xdate()
    plt.ylabel('Number of possible injuries', fontsize=14)
    plt.tick_params(axis='both', which='minor', labelsize=16)
    plt.locator_params(axis='both', nticks=12)

    plt.show()




def  dict_to_tables(years):

    dates, incidents = [], []

    for key, value in years.items():
        dates.append(key)
        incidents.append(value)

    return dates, incidents


main()
