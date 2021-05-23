# Import the file
import csv
import os

myfile = os.path.dirname(__file__) + '//Resources//02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv'

# Open the csv
with open (myfile)as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',') 

    # Assign values to variables with descriptive names
    months = int(0)
    totalpl = float(0)
    averagepl = float(0)
    monthlyplchange = float(0)
    changeinpl = float(0)
    lastmonthpl = float(0)
    greatestincrease = float(0)
    greatestincreasemonth = ""
    greatestdecrease = float(0)
    greatestdecreasemonth=""
    
    # Loop through the data totalpl=totalpl + row1
    for row in csvreader:
   
        months+= 1
        if months > 1:
            totalpl += float(row[1])
    # calculate the change in PL over the entired period 
            if months >2 :
                changeinpl = (float(row[1])-float(lastmonthpl))
            
            monthlyplchange = monthlyplchange + changeinpl
            lastmonthpl=row[1]
    # Find the greatest increase
            if changeinpl >0:
                if changeinpl > greatestincrease:
                    greatestincrease=changeinpl
                    greatestincreasemonth=row[0]
    # Find the greatest decrease
            if changeinpl<0:
                if changeinpl < greatestdecrease:
                    greatestdecrease=changeinpl
                    greatestdecreasemonth=row[0]

# Outputs
averagepl = monthlyplchange/(months-2)

print(f'Financial Analysis')
print(f'----------------------------------')
print(f'Total Months: {months-1}')
print(f'Total: ${round(totalpl)}')
print(f'Average  change: ${round(averagepl,2)}')
print(f'Greatest Increase in Profits: {greatestincreasemonth} (${round(greatestincrease)})')
print(f'Greatest Decrease in Profits: {greatestdecreasemonth} (${round(greatestdecrease)})')

# Open a text file for writing and reading 
Report_File = open(os.path.dirname(__file__) + "\\Analysis\\PyBankOutput.txt","w+")
Report_File.write('Financial Analysis \n')
Report_File.write('----------------------------------\n')
Report_File.write(f'Total Months: {months-1}\n')
Report_File.write(f'Total: ${(totalpl)}\n')
Report_File.write(f'Average  change: ${round(averagepl,2)}\n')
Report_File.write(f'Greatest Increase in Profits: {greatestincreasemonth} (${round(greatestincrease)})\n')
Report_File.write(f'Greatest Decrease in Profits: {greatestdecreasemonth} (${round(greatestdecrease)})\n')
Report_File.close()
csv_file.close()

