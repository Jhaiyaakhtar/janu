
from colorama import init, Fore, Style
import time

# Initialize colorama
init()

def slowprint(text, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.1)  # Adjust the delay as needed
    print(Style.RESET_ALL)  # Reset color after printing the text

# Example usage with green color
slowprint("⌛️=================💫", Fore.YELLOW)
slowprint("|~~~~~~~~~~~~joyriya akhtar~~~~~~~~~~💫", Fore.GREEN)
slowprint("|https://github.com/Jhaiyaakhtar/joyriya-427 💫", Fore.CYAN)
slowprint("|~~~~~~~~~~~😊😊😊😊😊😊😊😊😊~~~~~~~~💫", Fore.MAGENTA)
slowprint("|~~~~~~~~~~~💫", Fore.RED)
slowprint("                    💫")  
slowprint("                   💫") 
slowprint("                  💫") 
slowprint("===================💫")







import datetime
import os
import random

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print("Name:", contact.name)
            print("Phone Number:", contact.phone_number)
            print("Email:", contact.email)
            print("")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Name:", contact.name)
                print("Phone Number:", contact.phone_number)
                print("Email:", contact.email)
                return
        print("Contact not found.")

class Car:
    def __init__(self):
        self.position = [0, 0]

    def move_forward(self):
        self.position[1] += 1
        print(f"Moving forward! Current position: {self.position}")

    def move_backward(self):
        self.position[1] -= 1
        print(f"Moving backward! Current position: {self.position}")

    def move_left(self):
        self.position[0] -= 1
        print(f"Moving left! Current position: {self.position}")

    def move_right(self):
        self.position[0] += 1
        print(f"Moving right! Current position: {self.position}")

def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious forest.")
    print("You encounter a path nearby.")

    choice = input("Which way do you want to go, left or right? (left/right): ")
    if choice.lower() == "left":
        print("You've chosen to go left.")
        print("You discover a hidden cave.")
        print("Inside the cave, you find a glowing treasure chest!")
        print("Congratulations, you've found the treasure!")
    elif choice.lower() == "right":
        print("You've chosen to go right.")
        print("You proceed forward and find yourself at the starting point.")
        print("Nothing interesting found here.")
    else:
        print("Invalid direction. Please provide a valid direction.")

def main():
    username = input("Enter username: ")
    if username == 'joyriya':
        password = input("Enter password: ")
        if password == 'joya':
            choice = int(input("1: Date and Time Check\n"
                               "2: Password Cracker TMX\n"
                               "3: Contact Book\n"
                               "4: Number Guessing Game\n"
                               "5: Adventure Games\n"
                               "6: Seli Driving Car\n"
                               "7: Exit\n"
                               "Please choose 1-6 or continue>>> "))
            if choice == 1:
                print("_______________________________________")
                print(datetime.datetime.now())
            elif choice == 3:
                contact_book = ContactBook()
                while True:
                    print("1. Add Contact")
                    print("2. Display Contacts")
                    print("3. Search Contact")
                    print("4. Exit")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        name = input("Enter name: ")
                        phone_number = input("Enter phone number: ")
                        email = input("Enter email: ")
                        contact = Contact(name, phone_number, email)
                        contact_book.add_contact(contact)
                    elif choice == '2':
                        contact_book.display_contacts()
                    elif choice == '3':
                        name = input("Enter name to search: ")
                        contact_book.search_contact(name)
                    elif choice == '4':
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == 2:
                def check_password(password):
                    # Path to the password list file
                    password_file_path = "passwords.txt"
                    
                    # Checking password from the password list file
                    with open(password_file_path, "r") as file:
                        for line in file:
                            # Fetch each password from the password list file
                            # Check each password thoroughly
                            if password.strip() == line.strip():
                                return True
                    return False

                # Get password input from the user
                user_password = input("Enter the password to check: ")

                # Check password and print the result
                if check_password(user_password):
                    print("Password found in the list.")
                else:
                    print("Password not found in the list.")
            elif choice == 4:
                number_guessing_game()
            elif choice == 5:
                adventure_game()
            else:
                print("Sorry, your choice number is wrong.")
        else:
            print("Invalid password.")
    else:
        print("Your username does not match.")

if __name__ == "__main__":
    main()