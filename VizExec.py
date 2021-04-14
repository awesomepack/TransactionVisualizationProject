'''
This .py file executes the code neccesary to visualize my bank transaction
data.
'''


# Importing the neccessary libraries

import pandas as pd
import datetime as dt
import VizFunctions as FX

# Importing the bank transaction data into a dataframe named tData

tData = pd.read_excel(
r'C:\Users\daypa\Documents\git\Bank_Transaction_Project\TransactionVisualizationProject\Transactions_20-21.xlsx');

# Confirming the data was uploaded by printing the first 10 rows of the dataframe

print(tData.head(10));


# Calling the valueToDate function on tData

FX.valueToDate(tData);

print(tData.head(10)); # printing the first 10 rows to confirm the changes


# Iterating over the SubClass column and collecting all of the unique values
     

SpecificClass = []; # defining a list to collect unique instances of subclasses
Count = 0;

for i in tData.iloc[: , (3)]: # iterating over the values in the "subclass" column of the dataset
    
    if i not in SpecificClass:
        
        SpecificClass.append(i); # append the List with unique values of SubClass
        Count += 1; # icrement the count by one every time a new sub class is enocuntererd

print('');
print(SpecificClass);

# Reclassifying SubClasses in tData

FX.ReClass(tData);






