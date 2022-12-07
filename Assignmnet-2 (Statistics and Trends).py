# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:20:54 2022

@author: sande
"""

#importing pandas module to read the file(data set) and to calculate the statistical property(Describe)
import pandas as pd

#importing numpy module to calculate the statistical properties (mean and standard deviation)
import numpy as np

#importing pyplot from matplotlib module to plot the visualization graphs
import matplotlib.pyplot as plt

#importing stats from scipy module to calculate the statistical properties (kurtosis and skewness)
import scipy.stats as st

#defining a function to read the dataset and to produce original and transposed dataframes
def read_data_file(input_file_name,countries):
    #reading the data set using pandas module
    dataFrame = pd.read_csv(input_file_name)
    #cleaning the dataFrame by filling the NaN values with 0
    cleaned_dataFrame = dataFrame.fillna(0)
    #slicing the data frame by selecting fewe countries of our option
    sliced_dataFrame = cleaned_dataFrame[cleaned_dataFrame['Country Name'].isin(countries)]
    #creating a new data frame with countires as first column using the sliced data frame
    dataFrame_countries = pd.DataFrame(sliced_dataFrame)
    print('Original DataFrame:\n',dataFrame_countries)
    #transposing the sliced data frame
    transposed_dataFrame = pd.DataFrame.transpose(sliced_dataFrame)
    #creating a header
    header = transposed_dataFrame.iloc[0].values.tolist()
    #assigning the header to the transposed data frame
    transposed_dataFrame.columns = header
    #assigning the transposed dataframe with years as first column to a new variable
    dataFrame_years = transposed_dataFrame
    print('Transposed DataFrame:\n',dataFrame_years)
    #returning the 2 dataframes (one dataframe with countries as first column and other dataframe with years as first column)
    return dataFrame_countries,dataFrame_years

#calling the function with the data set and our own selection of countries.
df_countries,df_years = read_data_file('API_19_DS2_en_csv_v2_4700503-Copy.csv',['Australia','Bolivia','Canada','Switzerland','Denmark'])

#printing the statistical property "mean" using numpy module
print('Mean:\n',np.mean(df_years.iloc[4:,10:20]))

#printing the statistical property "standard deviation" using numpy module
print('\n\nStandard Deviation:\n',np.std(df_years.iloc[5:,10:20]))

#printing the statistical property "describe" using pandas module (using the dataframe)
print('\n\nDescribe:\n',df_years.iloc[4:,10:20].describe())

#printing the statistical property "kurtosis" using scipy module
print('\n\nKurtosis:',st.kurtosis(df_countries.iloc[10,4:]))

#printing the statistical property "Skewness" using scipy module
print('\nSkewness:',st.skew(df_countries.iloc[8,4:]))

#extracting the data for Australia's Population Growth
correlation=df_countries.iloc[4:,60:65]

#Calculating the Pearsons Correlation for Australia's Population Growth
print('\nPearsons Correlation:\n',correlation.corr())

#Calculating the Kendalls Correlation for Australia's Population Growth
print('\nKendalls Correlation:\n',correlation.corr(method='kendall'))

#plotting a line graph between two indicators: Denmark's Renewable energy consumption 
#(% of total final energy consumption) and Renewable electricity output (% of total electricity output)
plt.figure(figsize=(15,10))
plt.rcParams.update({'font.size': 17})
plt.plot(df_countries.iloc[356,35:50],label='Renewable energy consumption (% of total energy consumption)')
plt.plot(df_countries.iloc[359,35:50],label='Renewable energy production (% of total energy production)')
plt.title('Electricity Supply & Demand for Denmark',fontsize=23)
plt.xlabel('Time Period',fontsize=25)
plt.ylabel('Energy Levels',fontsize=25)
plt.legend(fontsize=16)
plt.show()