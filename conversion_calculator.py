# Conversion Calculator
# Christopher Cruz
# Purpose: Convert decimal numbers to binary and vice versa.

def decimal_to_binary(decimal_num):
    """Convert decimal to binary."""
    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    return binary_num

def binary_to_decimal(binary_num):
    """Convert binary to decimal."""
    decimal_num = 0
    binary_num = str(binary_num)[::-1]  # Reverse the binary string for easier calculation
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            decimal_num += 2 ** i
    return decimal_num

def main():
    """Main function to run the conversion program."""
    print("Welcome to the Conversion Calculator!")
    
    while True:
        # Display menu
        print("\nMenu:")
        print("1) Binary to Decimal")
        print("2) Decimal to Binary")
        print("3) Quit")

        # Get user choice
        choice = input("Enter your choice (1, 2, or 3): ")

        # Validate user input
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        # Quit the program
        if choice == '3':
            print("Goodbye!")
            break

        # Get user input for number
        user_input = input("Enter a {} number: ".format("binary" if choice == '1' else "decimal"))

        # Validate user input for number
        if (choice == '1' and not all(bit in '01' for bit in user_input)) or (choice == '2' and not user_input.isdigit()):
            print("Invalid {} number. Please enter a valid {} number.".format("binary" if choice == '1' else "decimal"))
            continue

        # Optional: Confirm user input
        confirm = input("You entered {}. Is this correct? (y/n): ".format(user_input))
        if confirm.lower() != 'y':
            print("Please re-enter your {} number.".format("binary" if choice == '1' else "decimal"))
            continue

        # Perform the conversion and display the result
        if choice == '1':
            result = binary_to_decimal(user_input)
            print("Binary {} is equivalent to Decimal {}".format(user_input, result))
        else:
            result = decimal_to_binary(int(user_input))
            print("Decimal {} is equivalent to Binary {}".format(user_input, result))

# Run the program
if __name__ == "__main__":
    main()
