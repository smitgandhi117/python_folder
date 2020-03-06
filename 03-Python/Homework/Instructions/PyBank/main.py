#imports
import csv
import pandas as pd
import numpy as np

#read the csv file using pandas read_csv function
df_csv = pd.read_csv('./Resources/budget_data.csv')

#create a DataFrame object
df = pd.DataFrame(df_csv)

#total number of months included in the dataset
totalMonths = len(df['Date'])

#net total amount of "Profit/Losses" over the entire period
netProfitLoss = np.sum(df['Profit/Losses'])

#average of the changes in "Profit/Losses" over the entire period
sum_changes = 0
change = 0
value = 0
n = 0

tempProfit = 0
tempLosses = 0

tempDateProfit = 0 
tempDateLoss = 0

for value in df.iterrows():
    if (n < (totalMonths-1)):
        change = (df.iloc[n+1, 1])-(df.iloc[n, 1])

        #check if the change of profits is bigger than the previous positive change
        if (change > tempProfit): 
            tempProfit = change
            tempDateProfit = n+1
        
        #check if the change of profits is smaller than the previous negative change
        elif (change < tempLosses):
            tempLosses = change
            tempDateLoss = n+1

        sum_changes = sum_changes + change
    #print("Change " + str(n) + ": " + str(change))
    avgChangePL = sum_changes / (totalMonths-1)
    n = n + 1

#Greatest increase in profits (date and amount) over the entire period
grtIncreaseProfits = df['Date'].iloc[tempDateProfit]

#Greatest decrease in profits (date and amount) over the entire period
grtDecreaseLosses = df['Date'].iloc[tempDateLoss]

print(df)
print("\n")

print("Financial Analysis")
print("---------------------------------------")
print("Total Months: " + str(totalMonths))
print("Net Profit/Loss: " + "$" + str(netProfitLoss))
print("Average Change: " + "$" + str(round(avgChangePL, 2)))
print("Greatest Increase in Profits: " + str(grtIncreaseProfits) + "\t" + "($" + str(tempProfit) + ")")
print("Greatest Decrease in Losses: " + str(grtDecreaseLosses)  + "\t" + "($" + str(tempLosses) + ")")