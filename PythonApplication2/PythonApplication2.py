import os 
import csv

#Function to count columns and rows in the CSV then multiply them together and return all 3 numbers as seperate values 
def CountTotalData(CSVPath: str):
    Count = 0
    Rows = 0
    with open(CSVPath, newline="") as f:
        for Row in csv.reader(f):
            Rows += 1
            #Counts how many rows
            if len(Row) > Count:
                Count += 1
    #Multiply rows by columns to get data entries (Not good if there are blank spaces, not sure how to account for that yet)
    DataEntries = int(Count * Rows)
    return Count, Rows, DataEntries

#Check for matching strings in CSV
def NumberOfSalesPerConsole(CSVPath: str, Console: str, SalesRegion: int):
     
    total = 0.0
    with open(CSVPath, newline="") as f:
         reader = csv.reader(f)
         for row in reader:
             if len(row) <= 10:
                 continue

             if row[2] != Console:
                continue


             try:
                sales = float(row[SalesRegion])
                total += sales
             except ValueError:
                continue

    return total



SelectConsole = input("Type the Games Console you want to see sales figures for: \n Wii, NES, SNES, GC, DS, 3DS, GB, GBA, XB, X360, PS, PS2, PS3, PSP\n\n")
SelectRegion = int(input ("Select the Region you want to count all sales in for this console: 6 = NA_Sales, 7 = EU_Sales, 8 = JP_Sales, 9 = Other_Sales, 10 = Global_Sales\n\n"))


#Print the number of Sales for a selected Games console
print(NumberOfSalesPerConsole("VideoGamesSales.csv", SelectConsole, SelectRegion))
#Print the number of items in csv
print(CountTotalData("VideoGamesSales.csv"))



