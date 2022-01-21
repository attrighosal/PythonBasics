import csv 

## Reading a special csv file
filename = "csv/special_result.csv"
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(filename, 'r') as csvfile:

    # creating a csv reader object
    csvreader = csv.reader(csvfile, delimiter=";")
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row) 

print(fields)
print(rows)

