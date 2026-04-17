import colorama
from colorama import Fore, Back, Style

# Initialize colorama with autoreset so colors don’t “stick”
colorama.init(autoreset=True)

# First line: Blue text on Yellow background, then Yellow text on Blue background
print(Fore.BLUE + Back.YELLOW + "Hi My name is Aman Kharwal " + 
      Fore.YELLOW + Back.BLUE + "I am your Machine Learning Instructor")

# Second line: Default text color with Cyan background
print(Back.CYAN + "Hi My name is Aman Kharwal")

# Third line: Red text with Green background
print(Fore.RED + Back.GREEN + "Hi My name is Aman Kharwal")
