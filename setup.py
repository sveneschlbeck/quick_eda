from setuptools import setup

setup(
 name='quick_eda',
 version='0.1.7',
 author='Sven Eschlbeck',
 author_email='sven.eschlbeck@t-online.de',
 packages=['quick_eda'],
 url='http://pypi.python.org/pypi/quick_eda/',
 license='LICENSE.txt',
 description='Important dataframe statistics with a single command',
 long_description_content_type='text/markdown',
 long_description=open('README.md').read(),
 install_requires=[
     "pandas",
   ],
)