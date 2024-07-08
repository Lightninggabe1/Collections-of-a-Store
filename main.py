#new module: "Recap: python Containers"
# Write your code below!
company_name = "®"
company_location = ('0.267127227218127','1234.87719214812984368318309131')
company_products = ['aPads','Datum Reading Platform','Prey MB-225 Multiprocessor Computer','Menclature Janus Console','5V Adapter']
company_data = {'name':company_name, 'location':company_location,'products':company_products}

#new module: 'deque'
from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!
supplies_deque = deque()
for item in csv_data:
  if item[2] == 'important':
    supplies_deque.appendleft(tuple(item))
  else:
    supplies_deque.append(tuple(item))
  
ordered_important_supplies = deque()
for imp in range(25):
  popped = supplies_deque.popleft()
  ordered_important_supplies.append(popped)
ordered_unimportant_supplies = deque()
for unimp in range(10):
  poppun = supplies_deque.pop()
  ordered_unimportant_supplies.append(poppun)
