def main():
    while True:
        fraction = input("Fraction: ").strip()
        
        try:
            numerator_str, denominator_str = fraction.split("/")
            
            X = int(numerator_str)
            Y = int(denominator_str)
            
            if X < 0 or Y < 0:
                raise ValueError
            
            if X > Y or Y == 0:
                continue
                
            percentage = round((X / Y) * 100)
            break
            
        except (ValueError, ZeroDivisionError):
            pass

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

main()