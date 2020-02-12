import pandas as pd
import numpy as np

# Grouping data by certain properties
# Predefined df of MLB stats
print('{}\n'.format(df))

groups = df.groupby('yearID')
for name, group in groups:
    print('Year: {}'.format(name))
    print('{}\n'.format(group))

print('{}\n'.format(groups.get_group(2016)))
print('{}\n'.format(groups.sum()))
print('{}\n'.format(groups.mean()))

no2015 = groups.filter(lambda x: x.name > 2015)
print(no2015)
# Lambda function will only take the data where the function holds true

# Multiple Columns
# player_df is predefined
groups = player_df.groupby(['yearID', 'teamID'])

for name, group in groups:
  print('Year, Team: {}'.format(name))
  print('{}\n'.format(group))

print(groups.sum())

