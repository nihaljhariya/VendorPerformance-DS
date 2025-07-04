import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import sqlite3
from scipy.stats import ttest_ind
import scipy.stats as stats
warnings.filterwarnings('ignore')


# Creating database connections 
conn = sqlite3.connect ('inventory.db')

#fetching vendor summary data 
df= pd.read_sql_query("select * from vendor_sales_summary" , conn)
df.head()

