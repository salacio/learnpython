shopping_list = ["banana", "orange", "apple"]

prices= {
        "banana" : 4,
        "apple" : 2,
        "orange" : 1.5,
        "pear" : 3
        }

stock = {
        "banana" : 6,
        "apple" : 0,
        "orange" : 32,
        "pear" : 15
        }

"""for key in prices:
    print("%s\nprice: %s\nstock: %s\n"
            % (key, prices[key], stock[key]))"""

def compute_bill(food):
    total = 0
    for item in food:
        total += food
    return total
compute_bill(shopping_list)
