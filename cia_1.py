# -*- coding: utf-8 -*-
"""CIA 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qzPr4weElKGfEh0D13ZKYyawvmEzzSy8

# ***Python Project***
Ananya Geetey 22112308
Siddhi Jhanwar 22112334

"""

# --- Importing all the necessary libraries ---

import csv
import pandas as pd
import requests
import os
import random
import time
from datetime import date, timedelta
from tabulate import tabulate

customer_database = {
    'Username': [],
    'Password': [],
    'First Name': [],
    'Last Name' : [],
    'Mobile Number': [],
    'Email ID': []
}
customer_database_copy = customer_database.copy()

book_database = {
    'Book_ID': ['111A', '111B', '111C', '111D', '111E', '111F', '111G', '111H', '111I', '111J', '111K', '111L', '111M'],
    'Book_Name': ['To Kill A Mockingbird', 'The Catcher In The Rye', 'The Great Gatsby', 'Anna Karenina', 'Little Women', 'Pride And Prejudice', 'The Kite Runner', 'The Book Thief', "Midnight's Children", 'War And Peace', 'The Fault In Our Stars', 'The Hunger Games', 'The Perks Of Being A Wallflower'],
    'Publish_Year': [1960, 1951, 1925, 1877, 1863, 1813, 2003, 2005, 1981, 1867, 2012, 2008, 1999],
    'Availability': ['Yes']*13,
    'Username' : [' ']*13,
    'Due Date' : [' ']*13
}

book_database_copy = book_database.copy()

class CustomerManagement:
    def __init__(self, database):
        self.database = database

    def register_customer(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        first_name = input("Enter your First name: ")
        last_name = input("Enter your Last name: ")
        mobile_number = input("Enter your mobile number: ")
        email_id = input("Enter your email ID: ")

        self.database['Username'].append(username)
        self.database['Password'].append(password)
        self.database['First Name'].append(first_name)
        self.database['Last Name'].append(last_name)
        self.database['Mobile Number'].append(mobile_number)
        self.database['Email ID'].append(email_id)
        print("Customer registered successfully.")

    def login_customer(self):
        print("Welcome!!")
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        index = self.database['Username'].index(username)
        if self.database['Password'][index] == password:
            print("Customer logged in successfully.")
        else:
            print("Invalid username or password.")

    def update_customer_details(self):
        username = input("Enter username: ")
        new_first_name = input("Enter new first name (leave blank to skip): ")
        new_last_name = input("Enter new last name (leave blank to skip): ")
        new_mobile_number = input("Enter new mobile number (leave blank to skip): ")
        new_email_id = input("Enter new email ID (leave blank to skip): ")

        index = self.database['Username'].index(username)
        if new_first_name:
            self.database['First Name'][index] = new_first_name
        if new_last_name:
            self.database['Last Name'][index] = new_last_name
        if new_mobile_number:
            self.database['Mobile Number'][index] = new_mobile_number
        if new_email_id:
            self.database['Email ID'][index] = new_email_id
        print("Customer details updated successfully.")

    def display_customers(self):
        data = {
            'Username': self.database['Username'],
            'First Name': self.database['First Name'],
            'Last Name' : self.database['Last Name'],
            'Mobile Number': self.database['Mobile Number'],
            'Email ID': self.database['Email ID'],
        }
        df = pd.DataFrame(data)
        table = tabulate(df, headers='keys', tablefmt='fancy_grid')
        print(table)

    def logout_customer(self):
       lgout=input("Do you want to Logout? ")
       if lgout.lower() == "yes":
          print("Logout Successful")
          lg=input("Do you want to Login again? ")
          if lg.lower() == "yes":
            self.login_customer()
          else:
             print("*"*10,"See You Soon!","*"*10)
       else:
          print("Back to Page!")

class LibrarySystem:
    def __init__(self, database):
        self.database = database

    def display_books(self):
        data = {
            'Book ID': self.database['Book_ID'],
            'Book Name': self.database['Book_Name'],
            'Publish Year': self.database['Publish_Year'],
            'Availability': self.database['Availability'],
            'Username': self.database['Username'],
            'Due Date': self.database['Due Date']
        }
        df = pd.DataFrame(data)
        table = tabulate(df, headers='keys', tablefmt='fancy_grid')
        print(table)

    def borrow_book(self):
        book = input("Which book do you want to borrow: ")
        book = book.title()
        username = input("Enter your Username: ")
        self.available(book, username)

    def available(self, book, username):
      book_index = None
      for index, book_name in enumerate(self.database['Book_Name']):
        if book_name == book:
            book_index = index
            break

      if book_index is not None and self.database['Availability'][book_index] == 'Yes':
        print('Book is Available')
        confirm = input("Kindly confirm if you want to borrow. Enter 'yes' for yes: ")
        if confirm.lower() == 'yes':
            today = date.today()
            borrowing_period = 15  # 15 days
            due_date = today + timedelta(days=borrowing_period)

            print("You have successfully issued", book, "for", borrowing_period, "days from", today)
            print("Please return the book by", due_date)

            self.database['Availability'][book_index] = 'No'
            self.database['Username'][book_index] = username
            self.database['Due Date'][book_index] = due_date
        else:
            print("Okay")
      else:
        print('Book is not available')

    def book_return(self):
      #error handling
      try:
        confirm = int(input("Do you want to return the book or get an extension? \nEnter 1 for returning and 2 for extension: "))
      except:
        print("That is not an Integer")
      else:
        print("Okay!")
        book = input("Please enter the Book Name: ")
        book = book.title()
        book_index = None
        for index, book_name in enumerate(self.database['Book_Name']):
          if book_name == book:
             book_index = index
             break
        if confirm == 1:
            # Change availability
            self.database['Availability'][book_index]= 'Yes'
            # Remove username
            self.database['Username'][book_index] = ' '
            # Remove due date
            self.database['Due Date'][book_index] = ' '
            print("Book Returned Successfully")
            self.review_book()
        if confirm == 2:
          #error handling
          try:
            Ext = 5  # 5 days extension
            # Add 5 days to the due date
            print("Okay! You have a 5-day extension on", book)
            # Get the updated due_date value
            self.database['Due Date'][book_index]+=timedelta(days=Ext)
          except:
            print("You haven't borrowed a book")
          else:
            print("Please return the book by:", self.database['Due Date'][book_index])



    def review_book(self):
      ask=int(input("Would you like to give a review? \nEnter 1 for yes: "))
      if ask==1:
        review=input("Please write your review! :) \n")
        print("*"*10, "Thanks!", "*"*10)
      else:
        print("Hope you liked reading the book!")

    def payment(self , amount):
      print("Payment successful. Amount: ", amount, "Rupees")

    def damage(self):
        print("Levels of Damage:")
        print("If there is a mark, the damage is considered 10%")
        print("If there is a tear, the damage is considered 25%")
        print("If pages are torn, the level of damage is considered 50%")
        print("If the whole book is damaged, the level is considered 100%")

        level = int(input("How much damage was done to the book? "))

        if level <= 10:
            print("It's Okay, There is no fine. Kindly return the book!")
            self.book_return()
        elif level <= 25:
            print("Please pay the fine of 100 Rupees and return the book.")
            self.payment(100)
            self.book_return()
        elif level <= 50:
            print("Please pay the fine of 500 Rupees and return the book.")
            self.payment(500)
            self.book_return()
        else:
            print("Please replace the book within 10 days.")

"""#Front End"""

def main():
    print("*"*30, "Welcome to the Library System!","*"*30, "\n")

    customer = CustomerManagement(customer_database)
    library = LibrarySystem(book_database)

    while True:
        print("*"*25, "----- Main Menu -----" ,"*"*25)
        print("1. Customer Management")
        print("2. Library Management")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("*"*10, "--- Customer Management ---" ,"*"*10)
            print("1. Register Customer")
            print("2. Login Customer")
            print("3. Update Customer Details")
            print("4. Display Customers")
            print("5. Logout")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                print("*"*5,"Please Register!","*"*5)
                customer.register_customer()
                print("*"*5,"Please Login!","*"*5)
                customer.login_customer()
            elif sub_choice == "2":
                print("*"*5,"Please Login!","*"*5)
                customer.login_customer()
            elif sub_choice == "3":
                customer.update_customer_details()
            elif sub_choice == "4":
                customer.display_customers()
            elif sub_choice == "5":
                customer.logout_customer()
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            print("*"*10, "--- Library Management ---" ,"*"*10)
            library.display_books()
            while True:
              print("1. Display Books")
              print("2. Borrow Book")
              print("3. Return Book")
              print("4. Fine for Damages")
              print("5. Exit")
              sub_choice = input("Enter your choice: ")

              if sub_choice == "1":
                print("*"*5,"BookShelf","*"*5)
                library.display_books()
              elif sub_choice == "2":
                library.borrow_book()
              elif sub_choice == "3":
                library.book_return()
              elif sub_choice == "4":
                library.damage()
              elif sub_choice == "5":
                print("Returning to Main Menu!")
                break  # Exiting the submenu and go back to the main menu
              else:
                print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting Library System")
            break
        else:
            print("Invalid choice. Please try again.")

main()
