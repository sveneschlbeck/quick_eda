"""
================================
Column Exploratory Data Analysis
================================
Easy and quick way to get the most important statistics for
a dataframe column with a single command showing several metrics.
"""

# Author: Sven Eschlbeck <sven.eschlbeck@t-online.de>
# License: BSD 3 clause

def column_eda(df, column):
	df = df
	column = column

	print("Head of column:\n")
	print(df[column].head())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nTail of column:\n")
	print(df[column].tail())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nMemory usage of the column:\n")
	print(df[column].memory_usage())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nShape of the column:\n")
	rows = df[column].shape[0]
	print("There are " + str(rows) + " rows in this column.")
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nNumber of occuring duplicates in the column:\n")
	dupRows = df[column].duplicated().sum()
	print("There are " + str(dupRows) + " duplicated rows in this column.")
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nNumber of occuring NULL/NA values in column:\n")
	print(df[column].isnull().sum())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nNumber of occuring unique values in column:\n")
	print(df[column].nunique())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nStandard statistics for column:\n")
	print(df[column].describe())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")
