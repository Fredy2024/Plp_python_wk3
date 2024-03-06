def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

def main():
    # Prompt the user for input
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percent)

    if final_price != original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print("No discount applied. The original price is: ${:.2f}".format(original_price))

# Call the main function
if __name__ == "__main__":
    main()

