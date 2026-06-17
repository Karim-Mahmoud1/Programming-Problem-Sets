def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_input = input("Date: ").strip()

        if "/" in date_input:
            try:
                parts = date_input.split("/")
                if len(parts) != 3:
                    continue

                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])

                if 1 <= month <= 12 and 1 <= day <= 31:
                    break
            except ValueError:
                pass

        else:
            try:
                if "," not in date_input:
                    continue

                clean_date = date_input.replace(",", "")
                parts = clean_date.split()

                if len(parts) != 3:
                    continue

                month_word = parts[0].title()
                day = int(parts[1])
                year = int(parts[2])

                if month_word in months and 1 <= day <= 31:
                    month = months.index(month_word) + 1
                    break
            except ValueError:
                pass

    print(f"{year}-{month:02d}-{day:02d}")

main()