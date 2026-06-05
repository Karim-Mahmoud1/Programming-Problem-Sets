def main():
    time_input = input("What time is it? ").strip()
  
    hours = convert(time_input)
    
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")


def convert(time):
    hours_str, minutes_str = time.split(":")
    
    hours = float(hours_str)
    minutes = float(minutes_str)
   
    return hours + (minutes / 60.0)


if __name__ == "__main__":
    main()