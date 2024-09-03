def calculate_discount(price, discount_percent):
    # Check if the discount os 20% or higher
    if discount_percent >=20:
        # Calculate the discount amount
        discount_amount = (discount_percent/100) * price
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        #Return the original price if the discount is less than 20%
        return price
    
    # Case with 25% discount
    final_price_1 = calculate_discount(100, 25)
    price(final_price_1) # Output: 75.0

    # Case with 10% discount
    final_price_2 = calculate_discount(100, 10)
    print(final_price_2) # Output: 100

    # If the dscount_percent is 20% higher, the discount is applied, 
    #and the final price is returned
#If the discount_percent is less than 20%, THE FUNCTION simply return the original 'price' without any modication


def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount = (discount_percent /100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user the input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price
if discount_percent >=20:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The orginal price is: ${original_price:.2}")



#output
# Enter the original price of the item: 100
# Enter the discount percentage: 25
# The final price after applying the discount is: $75.00

# Enter the original price of the item: 100
# Enter the discount percentage: 10
# The final price after applying the discount is: $100.00


