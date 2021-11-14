from setuptools import setup

setup(
 name='quick-eda',
 version='0.1.3',
 author='Sven Eschlbeck',
 author_email='sven.eschlbeck@t-online.de',
 packages=['quick-eda'],
 url='http://pypi.python.org/pypi/quick-eda/',
 license='LICENSE.txt',
 description='Important dataframe statistics with a single command',
 long_description_content_type='text/markdown',
 long_description=open('README.md').read(),
 install_requires=[
     "pandas",
   ],
)