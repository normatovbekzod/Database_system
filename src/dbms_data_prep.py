# -*- coding: utf-8 -*-
"""DBMS_Data_prep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SDlI2rD86tc5AYHgfwGe9IpJs-zQVBk2
"""

import csv

# Data to be written to the CSV file
rows = [
    [1, 'Address1', 'Phone1', 'Fax1', 'Manager1'],
    [2, 'Address2', 'Phone2', 'Fax2', 'Manager2'],
    [3, 'Address3', 'Phone3', 'Fax3', 'Manager3']
]

# Name of the CSV file
filename = "outlets.csv"

# Writing the data to the CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Writing the header row
    writer.writerow(['Outlet number', 'Address', 'Phone number', 'Fax number', 'Manager'])
    
    # Writing the data rows
    writer.writerows(rows)

import random

# Generating a list of 350 unique 7-digit random numbers
random_numbers = random.sample(range(1000000, 10000000), 350)

# Name of the text file
filename = "random_numbers.txt"

# Writing the list of numbers to the text file
with open(filename, 'w') as file:
    for number in random_numbers:
        file.write(str(number) + '\n')

import random

# Generating a list of 350 unique 10-digit random numbers
random_numbers = random.sample(range(1000000000000, 10000000000000), 420)

# Name of the text file
filename = "random_NIN_numbers.txt"

# Writing the list of numbers to the text file
with open(filename, 'w') as file:
    for number in random_numbers:
        file.write(str(number) + '\n')

import random

# List of first names
first_names = ['John', 'Jane', 'Robert', 'Emily', 'William', 'Elizabeth', 'Michael', 'Sophia', 'David', 'Olivia', 'James', 'Ava', 'Christopher', 'Isabella', 'Daniel', 'Mia', 'Matthew', 'Madison', 'Joseph', 'Charlotte']

# List of last names
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Young', 'Allen', 'King', 'Wright']

# Generating a list of 350 unique full names (first name and last name)
names = []
for i in range(350):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    names.append(first_name + ' ' + last_name)

# Name of the text file
filename = "names.txt"

# Writing the list of names to the text file
with open(filename, 'w') as file:
    for name in names:
        file.write(name + '\n')

import random

# Number of numbers to choose
num_numbers = 350

# Range of numbers to choose from
population = range(1, 251)

# Choosing the numbers randomly (with repetition allowed)
numbers = [random.choice(population) for i in range(num_numbers)]

# Name of the text file
filename = "numbers.txt"

# Writing the list of numbers to the text file
with open(filename, 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')

# Number of repetitions for each number
repetitions = 5

# Initialize the list
numbers = []

# Loop through the numbers from 1 to 70
for i in range(1, 71):
    # Repeat each number 'repetitions' times
    for j in range(repetitions):
        numbers.append(i)

# Name of the text file
filename = "numbers(1-70).txt"

# Writing the list of numbers to the text file
with open(filename, 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')