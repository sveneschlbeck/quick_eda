*****
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/sveneschlbeck/quick_eda)
![GitHub top language](https://img.shields.io/github/languages/top/sveneschlbeck/quick_eda)
![GitHub](https://img.shields.io/github/license/sveneschlbeck/quick_eda)
![PyPI](https://img.shields.io/pypi/v/quick_eda)
![Wheel](https://img.shields.io/pypi/wheel/quick_eda)
![Language](https://img.shields.io/pypi/implementation/quick_eda)
*****

[![quick_eda logo](logo.png)](https://pypi.org/project/quick_eda/)

## Project Description

A python package for Data Scientists, Students, ML Engineers and anyone who wants dataframe meta data without the trouble
of having to type in numerous commands.

## Installation

Use ``pip`` to install ``quick-eda`` by typing or copying the following command.
```python
pip install quick-eda
```

## License

This package is licensed under ``BSD Clause 3``.

## Example Usage

Users of the package can import the individual modules from this package, for example:
```python
import quick_eda.df_eda
import quick_eda.column_eda
```

This loads the submodules ``quick_eda.df_eda`` and ``quick_eda.column_eda``.
They must be referenced with their full name.
```python
quick_eda.df_eda.df_eda(<df>)
quick_eda.column_eda.column_eda(<column_name>)
```

An alternative way of importing the submodules is:
```python
from quick_eda import df_eda
from quick_eda import column_eda
```

This also loads the submodules ``quick_eda.df_eda`` and ``quick_eda.column_eda``,
and makes them available without their prefix, so they can be used as follows:
```python
df_eda.df_eda(<df>)
column_eda.column_eda(<column_name>)
```

Yet another variation is to import the desired functions directly:
```python
from quick_eda.df_eda import df_eda
from quick_eda.column_eda import column_eda
```

Again, this loads the submodules, but makes them directly available:
```python
df_eda(<df>)
column_eda(<column_name>)
```

Imagine you have a dataframe called ``pets`` with the columns ``name``, ``age`` and ``color``.
You could then run statistics on both the entire dataframe or e.g. the column ``age`` with
```python
df_eda(pets)
column_eda(pets, "age")
```

The returned information resulting from those commands contain the following meta data:

- ``df_eda()``:
	- First 5 rows of dataframe
	- Last 5 rows of dataframe
	- Names of the existing columns
	- Data types of the existing columns
	- Numbers of columns with same data type
	- Memory usage of each column
	- Shape of the dataframe (rows/columns)
	- Number of occuring duplicates in the dataframe
	- Number of occuring NULL/NA values per column
	- Number of occuring unique values per column
	- Standard statistics for each column
	- Correlations between columns

- ``column_eda()``:
	- First 5 entries of column
	- Last 5 entries of column
	- Memory usage of the column
	- Shape of the column
	- Number of occuring duplicates in the column
	- Number of occuring NULL/NA values in column
	- Number of occuring unique values in column
	- Standard statistics for column

## Source Code & Further Information

The source code is maintained at https://github.com/sveneschlbeck/quick_eda  
There are also further information concerning the BSD license model and more...
