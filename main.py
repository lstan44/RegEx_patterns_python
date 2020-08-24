# import for regular expressions
import re

# Read input from file instead of Web scraping
content  = open("input.txt").read()

print("====== Content ======\n")
print (content)

#### Continue your code here ####
#### Copy the RegExp part from your first submission ####
#### Then, modify the corresponding RegExp(s) ####
#### so that they work for the new content  ####
#### Output should be the same as in file out.png ####
#### Do not change anything in the input file ####

print("\n================== RegEx Results ======================\n")
print("Names:\n")
name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)
names = name_pattern.findall(content)
print(names)


school_pattern = re.compile(r'(?:,|,\s)([A-Z]{1}.*?)(?:\s\(|:|,)')
schools = school_pattern.findall(content)

print("\nSchools:\n")
print(schools)

money_pattern = re.compile(r'(?:\$)([0-9].*?)(?:U)')
money = money_pattern.findall(content)
print("\nSalaries:\n")

# print(money)
# print("\n")
# money = [strr.replace(',','') for strr in money]
# print(money)

#I realized the output file initally had the salaries as such '$600,000'
# And the picture that I sent on blackboard did not reflect that, 
# so I am fixing it here. 

salary_pattern = re.compile(r'(?:\s)(\$[0-9].*?)(?:U)' )
salaries = salary_pattern.findall(content)
print(salaries)
print("\n")

salaries = [s.replace('$','').replace(',','') for s in salaries]
print(salaries)