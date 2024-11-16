# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the final price or the original price
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")