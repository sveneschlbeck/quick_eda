"""
============================
DF Exploratory Data Analysis
============================
Easy and quick way to get the most important statistics for
a dataframe with a single command showing several metrics.
"""

# Author: Sven Eschlbeck <sven.eschlbeck@t-online.de>
# License: BSD 3 clause

def df_eda(df):
	df = df

	print("Head of dataframe:\n")
	print(df.head())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nTail of dataframe:\n")
	print(df.tail())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nNames of existing columns:\n")
	print(df.columns)
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nData types of the existing columns:\n")
	print(df.info())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nNumbers of columns with same data type:\n")
	print(df.dtypes.value_counts())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nMemory usage of each column:\n")
	print(df.memory_usage())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nShape of the dataframe (rows/columns):\n")
	rows = df.shape[0]
	cols = df.shape[1]
	print("There are " + str(rows) + " rows and " + str(cols) + " columns in this dataframe.")
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nNumber of occuring duplicates in the dataframe:\n")
	dupRows = df.duplicated().sum()
	print("There are " + str(dupRows) + " duplicated rows in the dataframe.")
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nNumber of occuring NULL/NA values per column:\n")
	print(df.isnull().sum())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nNumber of occuring unique values per column:\n")
	print(df.nunique())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nStandard statistics for each column:\n")
	print(df.describe())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")

	print("\nCorrelations between columns:\n")
	print(df.corr())
	print("- - - - - - - - - - - - - - - - - - - - - - - -")
