Introduction

Here is a - very - basic py library in order to perform basic EDA.
This aim to be a quick and basic analysis utility. 

FILE --- eda_utils.py

-- What : eda_utils.py is the file you will import in a py or ipynb to perform a quick EDA.

-- How  : import using 'import [repertory where you put eda_utils.py/]eda_utils OR
                       'from [repertory where you put eda_utils.py/]eda_utils import [function(s) defined below]'

-- 'eda_prime' function : ef eda_prime(ds:pandas.DataFrame, l:int=30):
The function will allow you to quickly set up a basic analysis on :
- Shape & columns         : these are gathered together for readability ; 
- A sample                : fixed at ten random rows of the dataset ;
- Descriptive statisctics : the describe(include = "all") of the dataset ;
- MValues                 : % of missing values of the dataset.

Args :
- ds:pandas.DataFrame  : The pandas DataFrame for which you which you want to perform basic analysis.
- l:int=30             : The optional number of '-' car that will be used in the displayed elements. 30 is a good number for display.

Example : 
<img width="1156" height="657" alt="image" src="https://github.com/user-attachments/assets/e9bc209b-251c-4d4b-9dc1-e2a16049bab0" />
