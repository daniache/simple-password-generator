SIMPLE RANDOM PASSWORD  GENERATOR 

It is a random password generator that creates a secure password based on user input.
The user specifies how many letters, symbols, and numbers they want in the password, and the application generates it accordingly. 
The purpose is to consolidate an understanding of Python programming fundamentals, especially the use of in-built libraries like random. 
The generated password is then displayed to the use.

INSTRUCTIONS

This project containes two version of the application: 
1. basic simple password generator 
2. simple password generator with a gui

Funtionalities

- The program prompts the user to specify the number of letters, symbols and numbers they want in their password
- it randomly selects the desired number of letters from a predefined list of uppercase and lowercase characters.
- It randomly selects the desired number of symbols from a set of special characters.
- It randomly selects the desired number of numbers from the digits 0-9.
- It Combines the selected characters into a password and shuffles them for added randomness.
- It displays the generated random password to the user.

Technoligies used:

Thoony (but you works in any python-based IDE)
Library: Random
Git Bash

HOW TO INVOKE THE SIMPLE PASSWORD APP (NO GUI)

This program requires:

Python 3.10 or higher in any Python-based IDE (used Thoony) and standard python library 

1. Install Python
2. Save the code  into a Python file or download the one in this repository.
3. Open your terminal or command prompt.
4. Navigate to the directory where you saved pyhonfileName.py.
5. Run the script using the command py pyhonfileName.py
6. The program will ask how many letters, symbols, and numbers you want in your password.
7. After you enter the values, it will display a randomly generated password that meets your criteria.


SIMPLE RANDOM PASSWORD GENERATOR WITH GUI

![Simple-passgenerator IMAGE](https://github.com/user-attachments/assets/97853682-8ccd-49a1-a85c-f4997d42f04a)

This application compared to the previous one allows users to generate a secure password through a user-friendly interface. 
The user inputs the desired number of letters, symbols, and numbers, and the application generates a random password accordingly. 
Additionally, it displays the password's strength and provides a button to copy the password to the clipboard. 
This program is an upgraded version of the previous one with additional features.

Functionalities

User Input via GUI
It uses a graphical interface to ask the user for the number of letters, symbols, and numbers to include in the password.

Password Generation:
It randomly selects the specified number of characters from letters, symbols, and numbers.
It shuffles and generates a password.

Password Display
The generated password is displayed within the interface, with long passwords automatically wrapped to fit within the display area.

Password Strength Indicator
It evaluates the strength of the generated password (Weak, Medium, Strong) based on length and character variety.

Technoligies used:

Python 
Python Standard Library:

- random: Used to randomly select characters for password generation.
- tkinter: A built-in Python library used to create the graphical interface.
- pyperclip: A library used to copy the generated password to the clipboard.
	
HOW TO INVOKE THE SIMPLE RANDOM PASSWORD APP (WITH GUI)

1. Make sure step 1 has been done
2. Install pyperclip dependecy using any terminalof your choice(for this project git bash was used) or command prompt:
   py -m pip install pyperclip
3. Save the code into a Python file or download the one in this repository.
4. Open Thoony and open the saved Python file.
5. Click Run button
