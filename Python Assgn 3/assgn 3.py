def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
 # Prompt user  for input 
try :
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount_percentage)
    if discount_percentage >= 20:
        print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
# This code calculates the final price of an item after applying a discount if the discount percentage is 20% or more.
