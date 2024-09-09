import pandas as pd
import xlrd
import sqlite3

# read in data into dataframes
data_origonal_boys = pd.read_excel('names.xlsx', sheet_name='1')
data_origonal_girls = pd.read_excel('names.xlsx', sheet_name='2')

# set the top row to be the header
data_boys.columns = data_origonal_boys.iloc[0]
data_boys = data_origonal_boys[1:]

data_girls.columns = data_origonal_girls.iloc[0]
data_girls = data_origonal_girls[1:]

# create database file
conn = sqlite3.connect('names.db')

# Write the DataFrame to a SQL table
data_boys.to_sql('boys', conn, if_exists='replace', index=False)
data_girls.to_sql('girls', conn, if_exists='replace', index=False)

# Close the connection
conn.close()