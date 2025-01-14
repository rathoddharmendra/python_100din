# type: ignore

import os, csv, math

filename = os.path.join(os.path.dirname(__file__), 'weather_data.csv')

with open(filename, 'r') as file:
    # data = [row.strip('\n') for row in file.readlines()]
    csv_data = csv.reader(file, delimiter=',')
    # for row in csv_data:
    #     print(row)

    csv_data_list = [row for row in csv_data][1:]
        # print(csv_data.__next__())
    csv_temperature = [int(row[1]) for row in csv_data_list]
    # print(csv_temperature)


import pandas as pd

pd_data: pd.DataFrame = pd.read_csv(filename, delimiter=',') 
pd_data_temperatures: pd.Series = pd_data['temp']
temp: int = pd_data_temperatures[0]
print(pd_data_temperatures[0])
max = pd_data_temperatures.max(0)

print(round(pd_data_temperatures.mean(0), 2))
print(pd_data_temperatures.max())
print(pd_data_temperatures.index)
# print(f'{pd_data_temperatures.max(0)=}')
print(pd_data[pd_data.temp == max]) # getting hold of the row

monday = pd_data[pd_data.day == 'Monday']
temp = monday.temp.apply(lambda x: (x * 9/5) + 32)
print(float(temp[0]))
print(f'The average temperature on Monday is {temp[0]:.1f}°F')