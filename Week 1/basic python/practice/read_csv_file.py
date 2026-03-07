# how read the csv file
import csv

with open('./assets/data.csv', 'r') as file:
  reader = csv.reader(file)
  # I want to see what the reader object is
  print(reader)

  # printing the rows of the csv file
  for row in reader:
    print(row)
