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

#new_module: 'OrderedDict' 
from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# Write your code below!
orders = OrderedDict(order_data)
to_move = []
to_remove = []
for order, value in orders.items():
  if value == 'returned':
    to_move.append(order)
  elif value == 'canceled':
    to_remove.append(order)

for removal in to_remove:
  orders.pop(removal)

for returnee in to_move:
  orders.move_to_end(returnee)

print(orders)

#new_module:_'chainmap'
from collections import ChainMap
year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!

# Checkpoint #1
profit_map = ChainMap(*year_profit_data)

def get_profits(input_map):
    total_standard_profit = 0.0
    total_holiday_profit = 0.0

    for key in input_map.keys():
        if 'holiday' in key:
            total_holiday_profit += input_map[key]
        else:
            total_standard_profit += input_map[key]

    return total_standard_profit, total_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)
for item in new_months_data:
    profit_map = profit_map.new_child(item)
current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)
year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit

#new_module:8/13
from collections import Counter
opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# Write your code ben
def find_amount_sold(opening,closing,item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)
  opening_count.subtract(closing_count)
  return opening_count[item]

tshirts_sold = find_amount_sold(opening_inventory,closing_inventory, 't-shirt')
print(tshirts_sold)


#new_module: "UserDict"
from collections import UserDict
data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
class OrderProcessingDict(UserDict):
  def clean_orders(self):
    to_del = []
    for key, val in self.data.items():
        if val['order_status'] == 'complete':
          to_del.append(key)
    for item in to_del:
      del self.data[item]

process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
