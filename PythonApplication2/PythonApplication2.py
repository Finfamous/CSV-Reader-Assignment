
import os 
import csv

#Function to count columns and rows in the CSV then multiply them together and return all 3 numbers as seperate values 
def CountTotalData(CSVPath: str):
    Count = 0
    Rows = 0
    try:
        with open(CSVPath, newline="") as f:
            for Row in csv.reader(f):
                Rows += 1
                if len(Row) > Count:
                    Count += 1
        #Multiply rows by columns to get data entries (Not good if there are blank spaces, not sure how to account for that yet)
        DataEntries = int(Count * Rows)
        return Count, Rows, DataEntries
    #Error checking for csv file
    except (FileNotFoundError, PermissionError) as exc:
        print(f"Cannot open CSV file, File not found: {exc}")
    except csv.Error as exc:
        print(f"Cannot open CSV file, Error: {exc}")
    return None

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

#while True Loop waits for valid string input
while True:
    SelectConsole = input("Type the Games Console you want to see sales figures for: \n Wii, NES, SNES, GC, DS, 3DS, GB, GBA, XB, X360, PS, PS2, PS3, PSP\n\n")
    try:
        Console = str(SelectConsole)
        if Console in ("Wii", "NES", "SNES", "GC", "DS", "3DS", "GB", "GBA", "XB", "X360", "PS", "PS2", "PS3", "PSP"):
            break
        else: 
            print("Console Name not selected")
    except ValueError:
        print("")
#while True Loop waits for valid number input
while True:
    SelectRegion = int(input ("Select the Region you want to count all sales in for this console: 6 = NA_Sales, 7 = EU_Sales, 8 = JP_Sales, 9 = Other_Sales, 10 = Global_Sales\n\n"))
    try: 
        Region = int(SelectRegion)
        if Region in {6, 7, 8, 9, 10}:
            break
        else: 
            print("Number between 6 - 10 was not selected")
    #As far as I can see, this exception will never be called but the code doesn't work without it
    except ValueError:
        print("")

#Print the number of Sales for a selected Games console
print(NumberOfSalesPerConsole("VideoGamesSales.csv", SelectConsole, SelectRegion))
#Print the number of items in csv
print(CountTotalData("VideoGamesSales.csv"))



