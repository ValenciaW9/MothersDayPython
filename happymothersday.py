import pyfiglet # type: ignore

from termcolor import colored # type: ignore

import random

def get_random_font_style():

    # List of available Figlet font styles

    font_styles = pyfiglet.FigletFont.getFonts() 

    # Choose a random font style from the list

    return random.choice(font_styles)

def get_random_color():

    # List of available colors

    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    # Choose a random color from the list

    return random.choice(colors)

def wish_mothers_day():

    # Get a random font style and color

    random_font_style = get_random_font_style()

    random_color = get_random_color()

    # Create a Figlet font object with the random style

    font = pyfiglet.Figlet(font=random_font_style)

    # Print the decorative greeting in the chosen color

    print(colored(font.renderText("Happy Mother's Day!"), random_color))

wish_mothers_day()

#This code generates a Mother's Day wish with a randomly selected font style and color using the pyfiglet and termcolor libraries in Python. Here's a breakdown of what each part of the code does:
#import pyfiglet: Imports the pyfiglet library, which is used to create ASCII art text.
#from termcolor import colored: Imports the colored function from the termcolor library, which is used to add color to text in the terminal.

#import random: Imports the random module, which is used to generate random font styles and colors.

#get_random_font_style(): Defines a function that returns a random font style chosen from the available Figlet font styles provided by pyfiglet.

#get_random_color(): Defines a function that returns a random color chosen from a predefined list of colors.
