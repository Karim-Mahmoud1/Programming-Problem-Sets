import os

def clear_screen():
    """Clears the terminal for a cleaner UI experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

def decimal_to_octal(decimal_num):
    """Converts a base-10 decimal integer to a base-8 octal string."""
    if decimal_num == 0:
        return "0"
    
    octal_digits = []
    # Loop divides by 8 repeatedly and tracks the remainders
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_digits.append(str(remainder))
        decimal_num = decimal_num // 8
        
    # Reverse the remainders list to get the final octal representation
    return "".join(reversed(octal_digits))

def octal_to_decimal(octal_str):
    """Converts a base-8 octal string to a base-10 decimal integer."""
    decimal_val = 0
    # Reverse the string to process digits from right to left (units, eights, sixty-fours...)
    reversed_octal = octal_str[::-1]
    
    for power, digit in enumerate(reversed_octal):
        decimal_val += int(digit) * (8 ** power)
        
    return decimal_val

def main():
    while True:
        clear_screen()
        print("=== NUMBER SYSTEM CONVERTER ===")
        print("1. Decimal to Octal (Base 10 ➔ Base 8)")
        print("2. Octal to Decimal (Base 8 ➔ Base 10)")
        print("3. Exit")
        print("===============================")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            try:
                dec_input = input("\nEnter a positive Decimal number: ").strip()
                # Validate that it's a positive integer
                if not dec_input.isdigit():
                    raise ValueError
                
                result = decimal_to_octal(int(dec_input))
                print(f"✅ Decimal {dec_input} is equal to Octal: {result}")
            except ValueError:
                print("❌ Invalid input! Please enter a valid, positive decimal integer.")
                
            input("\nPress Enter to continue...")

        elif choice == '2':
            oct_input = input("\nEnter an Octal number: ").strip()
            # Validate that the string only contains digits from 0 to 7
            if not oct_input.isdigit() or any(int(d) > 7 for d in oct_input):
                print("❌ Invalid input! Octal numbers can only contain digits from 0 to 7.")
            else:
                result = octal_to_decimal(oct_input)
                print(f"✅ Octal {oct_input} is equal to Decimal: {result}")
                
            input("\nPress Enter to continue...")

        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")
            input("\nPress Enter to try again...")

if __name__ == "__main__":
    main()