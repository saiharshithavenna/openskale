import csv

def min_price_calculation(csv_file, food_items):
    #add the food_items as input
    food_items = set(food_items.replace('+', ' ').split())

    #dictionary to store restaurant data
    restaurant_data = {}

    #set to get the food items if found
    food_items_found = set()

    #read the input csv file
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            restaurant_id, price, food_item = int(row[0]), float(row[1]), row[2]
            
            if restaurant_id not in restaurant_data:
                restaurant_data[restaurant_id] = {}
            
            restaurant_data[restaurant_id][food_item] = price

            # get the food items which are found
            if food_item in food_items:
                food_items_found.add(food_item)

    # if not found all the food items return not found
    if not food_items.issubset(food_items_found):
        return "No matching found"

    # Filter restaurants that have all the required food items
    min_price = None
    best_restaurant = None

    for restaurant_id, items in restaurant_data.items():
        if food_items.issubset(items.keys()):
            total_price = sum(items[food_item] for food_item in food_items)
            
            if min_price is None or total_price < min_price:
                min_price = total_price
                best_restaurant = restaurant_id

    if best_restaurant is None:
        return "No matching found"
    else:
        return best_restaurant, min_price

# Sample usage
csv_file = 'question_two_data.csv'
food_items = "extreme_fajita+jalapeno_poppers+extra_salsa"
result = min_price_calculation(csv_file, food_items)
print(result)
