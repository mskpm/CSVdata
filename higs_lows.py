# Wizaualizacja wykrsu temperatur dla miasta Sitka

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import temperature_data as tdata

# Pobieranie z pliku dat i temperatur w poszczególnych okresach

filename_sitka = 'csv/sitka_weather_2014.csv'
filename_dth_valley = 'csv/death_valley_2014.csv'

sitka = tdata.temperature_data('sitka', filename_sitka)
dthv = tdata.temperature_data('death_valley', filename_dth_valley)

# Dane wykresu
fig = plt.figure(dpi=128, figsize=(9, 5))
plt.plot(sitka.dates, sitka.highs, label=str(sitka.place), c='blue', alpha=0.5)
plt.plot(sitka.dates, sitka.lows, c='blue', alpha=0.5)
plt.plot(dthv.dates, dthv.highs, label=str(dthv.place),c='red', alpha=0.5)
plt.plot(dthv.dates, dthv.lows, c='red', alpha=0.5)
plt.fill_between(sitka.dates, sitka.highs, sitka.lows, facecolor='blue', alpha=0.3)
plt.fill_between(dthv.dates, dthv.highs, dthv.lows, facecolor='red', alpha=0.3)

plt.legend()

# Formatowanie wykresu
plt.title("Najwyższa i najniższa temperatura dnia, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

