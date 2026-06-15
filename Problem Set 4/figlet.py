import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
available_fonts = figlet.getFonts()

if len(sys.argv) == 1:

    font_name = random.choice(available_fonts)
elif len(sys.argv) == 3:

    flag = sys.argv[1]
    font_name = sys.argv[2]
    
    if flag not in ["-f", "--font"] or font_name not in available_fonts:
        sys.exit("Invalid usage")
else:
    
    sys.exit("Invalid usage")


figlet.setFont(font=font_name)

user_text = input("Input: ")

print("Output:")
print(figlet.renderText(user_text))
