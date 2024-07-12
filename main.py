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

#new_module: 'Named Tuple'
from collections import namedtuple
clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
ClothingItem = namedtuple('ClothingItem',['type','color','size','price'])
new_coat = ClothingItem('coat','black','small',14.99)
coat_cost = new_coat.price
updated_clothes_data = []
for cloth in clothes:
  updated_clothes_data.append(ClothingItem(cloth[0],cloth[1],cloth[2],cloth[3]))

#new_module: 'DefaultDict'
from collections import defaultdict
site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
validated_locations = defaultdict(lambda: 'TODO: Add to website')
validated_locations.update(site_locations)
for product in updated_products:
  site_locations[product] = validated_locations[product]
