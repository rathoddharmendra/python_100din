#type: ignore
import pandas as pd
import os

filename = os.path.join(os.path.dirname(__file__),'squirrel-data-long.csv')

# Load the data into a pandas DataFrame from the CSV file
raw_squirrel_data = pd.read_csv(filepath_or_buffer=filename)

# Display the first few rows of the DataFrame
# print(type(raw_squirrel_data.columns))
# print(raw_squirrel_data.columns)
# Index(['X', 'Y', 'Unique Squirrel ID', 'Hectare', 'Shift', 'Date',
#        'Hectare Squirrel Number', 'Age', 'Primary Fur Color',
#        'Highlight Fur Color', 'Combination of Primary and Highlight Color',
#        'Color notes', 'Location', 'Above Ground Sighter Measurement',
#        'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating',
#        'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail flags',
#        'Tail twitches', 'Approaches', 'Indifferent', 'Runs from',
#        'Other Interactions', 'Lat/Long'],
#       dtype='object')


# Select the 'Primary Fur Color' column and display the values
fur_colors = raw_squirrel_data['Primary Fur Color']
unique_colors = fur_colors.unique()

squirrel_count = {}
for color in unique_colors[1:]:
    squirrel_count[color] = 0

# Count the number of squirrels for each fur color and store the counts in a dictionary
for fur_color in fur_colors:
    if fur_color in unique_colors[1:]:
        squirrel_count[fur_color] += 1
print(f'{squirrel_count=}')
# {'Gray': 2473, 'Cinnamon': 392, 'Black': 103}
# df_squirrel_count = pd.DataFrame(squirrel_count, index=squirrel_count.keys())
df_squirrel_count = pd.DataFrame.from_dict(squirrel_count, orient='index', columns= [ 'Count'])
df_squirrel_count.index.name = 'Fur Color'

print(df_squirrel_count)
df_squirrel_count.to_csv(os.path.join(os.path.dirname(__file__),'squirrel_count.csv'))


# create dataframe
keys = []
values = []

for key, value in squirrel_count.items():
    keys.append(key)
    values.append(value)

data_dict = {
    'Fur Color': keys,
    'Count': values
}

df_data_dict = pd.DataFrame(data_dict)
df_data_dict.to_csv(path_or_buf=os.path.join(os.path.dirname(__file__),'squirrel_count_new.csv'))

