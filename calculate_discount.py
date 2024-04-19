def calculate_discount(price, discount_percent):
    """Calculates the final price after applying discount

    Parameters:
    price(float): origianl item price
    discount_percent (flaot): discount percentag

    returns:
    float: final price after discount.
    """

    if discount_percent > 0.2:
        final_price = price * (1 - discount_percent)
    else:
        final_price = price
    return final_price

# prompt user to enter original price and discount percentage
original_price = float(input("Enter the original price of the item:"))
discount_percent = float(input("Enter the discount percentage as a decimal"))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)

#print the final price 
print("The final price after applying the discount is: Sh{:.2f}".format(final_price))