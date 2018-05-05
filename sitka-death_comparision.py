import csv
from datetime import datetime
from matplotlib import pyplot as plt


def main():
    with open('sitka_weather_2014.csv', 'r') as f:
        sitka_reader = csv.reader(f)
        header_sitka = next(sitka_reader)

        with open('death_valley_2014.csv', 'r') as d:
            death_reader = csv.reader(d)
            header = next(death_reader)

            dates_sitka, highs_sitka, lows_sitka = [], [], []
            dates_death, highs_death, lows_death = [], [], []

            dates_sitka, highs_sitka, lows_sitka = time_reader(sitka_reader, 'sitka')
            dates_death, highs_death, lows_death = time_reader(death_reader, 'death')

            sitka = (dates_sitka, highs_sitka, lows_sitka)
            death = (dates_death, highs_death, lows_death)

            printer(sitka, death)


def time_reader(reader, header = 'unknown dataset'):
    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print(datetime, 'NO DATA  ', header)
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


            return dates, highs, lows


def printer(sitka, death):

    dates_sitka, highs_sitka, lows_sitka = sitka
    dates_death, highs_death, lows_death = death


    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates_sitka, highs_sitka, c='red', alpha = 0.4 )
    plt.plot(dates_death, highs_death, c='black', alpha = 0.5 )
    # plt.fill_between(dates_sitka, highs_death, highs_death,
    #                                 facecolor='red', alpha = 0.1)
    #
    # plt.plot(dates_sitka, lows_sitka, c='blue', alpha = 0.4 )
    # plt.plot(dates_death, lows_death, c='black', alpha = 0.5 )
    # plt.fill_between(dates_sitka, lows_death, lows_death,
    #                 facecolor='blue', alpha = 0.1)

    # plt.show()


main()
