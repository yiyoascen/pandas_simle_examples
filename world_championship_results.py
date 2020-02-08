# Basic example usage of pandas from the 2014 Chess World Championship

import pandas as pd

# create the table
df = pd.DataFrame({'Carlsen': [.5, 1, 0, .5, .5, 1, .5, .5, .5, .5, 1],
                   'Anand': [.5, 0, 1, .5, .5, 0, .5, .5, .5, .5, 0]})
# print the winner
print(df, '\n')

# print the
print('The winner is', df.keys().max(), '\n')

# print the total
print('total:')
print('Magnus : ', df['Carlsen'].sum())
print('Anand : ', df['Anand'].sum())

# now I transform it into a evil excel
df.to_excel('noooooo.xlsx')
