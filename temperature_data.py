import csv
from datetime import datetime

class temperature_data():
    """Przechowuje dane do wykresu temperatur"""
    
    def __init__(self, place, filename):
        """Inicjacja atrybutów"""
        self.place = str(place)
        self.filename = str(filename)

        self.dates, self.highs, self.lows = [], [], []

        with open(self.filename) as file:
            reader = csv.reader(file)
            header_row = next(reader)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    high = (int(row[1]) - 32)/1.8
                    low = (int(row[3]) - 32 )/1.8
                except ValueError:
                    print(current_date, 'brak danych')
                else:
                    self.highs.append(high)
                    self.lows.append(low)
                    self.dates.append(current_date)


