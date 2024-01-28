print("BPP pizza price calculator")
print("="*len("BPP pizza price calculator"))
print("\n")

# Get user input for the number of pizzas ordered (positive integer)
while True:
    try:
        pizzas_ordered = int(input("How many pizzas ordered? "))
        if pizzas_ordered >= 1:
            break
        else:
            print("please enter positive integer ")
    except ValueError:
        print("Please enter a number")

# Get user input for delivery requirement (Y/N)
while True:
    delivery_required = input("Is delivery required?(y/n) ")
    if delivery_required.upper() in {"Y","N"}:
        break
    else:
        print("Please enter y or n")

# Get user input for whether it is Tuesday (Y/N)
while True:
    delivery_day = input("Is it tuesday?(y/n) ")
    if delivery_day.upper() in {"Y","N"}:
        break
    else:
        print("Please enter y or n")

# Get user input for app usage (Y/N)
while True:
    app_used = input("Did the customer use the app?(y/n)")
    if app_used.upper() in {"Y","N"}:
        break
    else:
        print("Please enter y or n")
    
def calculate_price(pizzas_ordered,delivery_required,delivery_day,app_used):
    """
    Calculate the total price of pizzas based on user inputs.

    Parameters:
    - pizzas_ordered (int): The number of pizzas ordered.
    - delivery_required (str): Whether delivery is required (Y/N).
    - delivery_day (str): Whether it is Tuesday (Y/N).
    - app_used (str): Whether the customer used the app (Y/N).

    Returns:
    - float: The total price of pizzas.
    """
    price = 12
    delivery_cost = 2.50
    if delivery_day.upper() == "Y":
        price = price - 50/100 * price
    if delivery_required.upper() == "Y":
       total_price = price * pizzas_ordered if pizzas_ordered >= 5 else price * pizzas_ordered + delivery_cost
    else:
        total_price = price * pizzas_ordered
    if app_used.upper() == "Y":
        total_price = total_price - 25/100 * total_price
    return total_price

final_price = calculate_price(pizzas_ordered,delivery_required,delivery_day,app_used)
print(f"Total Price: £{final_price:.2f}")
    
    