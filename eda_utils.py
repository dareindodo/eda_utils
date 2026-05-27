import string
import pandas
from IPython.display import display

def header_format(str:str, l) -> str:
    return "\n" + "---" + " " + str + " " + "-"*(l - len(str) - 5)

def end_format(l:int) -> str:
    return "-"*l + "\n"

def eda_prime(ds:pandas.DataFrame, l:int=30):
    print(header_format("Dataset Shape", l))
    print(ds.shape)
    print(end_format(l))

    print(header_format("Dataset Shape", l))
    print(ds.shape)
    print(end_format(l))

    print(header_format("Dataset Sample", l))
    display(ds.sample(10))
    print(end_format(l))
    
    print(header_format("Dataset Describe", l))
    print(ds.describe(include = "all"))
    print(end_format(l))
    
    print(header_format("Dataset MValues", l))
    print(100*ds.isnull().sum()/ds.shape[0])
    print(end_format(l))