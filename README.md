# LibSys - Library Management System
---
## DESCRIPTION

_LibSys_ is a comprehensive and user-friendly library management system designed to efficiently manage customer information and library operations. It provides a range of functions to facilitate customer management and library operations seamlessly.

---
## FUNCTIONALITIES OF THE LIBRARY MANAGEMENT SYSTEM

>Class Customer Management: <br>

`def register_customer(self):` 

This function is used for getting a user registered into the system <br>

`def login_customer(self):` 

This function is used for logging into the system <br>

`def update_customer_details(self):`

This function is used for updating the details of the user  <br>

`def display_customers(self):`

This function is used for displaying users' database  <br>

`def logout_customer(self):`

This function is used for logging out of the system  <br>

---
>Class Library System: <br>

`def display_books(self):`

This function is used for displaying the books' database <br>

`def borrow_book(self):`

This function is used for borrowing a book <br>

`def available(self, book, username):`

This function is used for finding out if the book is available or not <br>

`def book_return(self):`

This function is used for returning a book <br>

`def review_book(self):`

This function is used for giving a review for the book <br>

`def payment(self , amount):`

This function is used for paying for damages done to the book <br>

`def damage(self):`

This function is used for finding out how much damage is done to the book <br>

---
## CODE EXPLANATION

The program contains 2 classes:

- Class Customer Management
- Class Library Management

`main()` function that serves as the entry point for the library management system.

- The function starts by printing a welcome message to the console.

- Instances of the CustomerManagement and LibrarySystem classes are created, passing the respective database parameters (customer_database and book_database) to their constructors. These instances are used to interact with the customer management and library management functionalities.

- The function enters a while loop that displays the main menu options and asks for user input.

- The main menu options are displayed, including options for customer management, library management, and exiting the system.

- The user is prompted to enter their choice.

- If the user selects "1" for customer management, a sub-menu for customer management options is displayed.

- The user is prompted to enter their choice for the customer management sub-menu.

- Based on the user's choice, the corresponding methods from the CustomerManagement class are called to perform the desired action, such as registering a customer, logging in, updating customer details, displaying customers, or logging out.

- If the user selects "2" for library management, a sub-menu for library management options is displayed.

- The user is prompted to enter their choice for the library management sub-menu.

- Based on the user's choice, the corresponding methods from the LibrarySystem class are called to perform the desired action, such as displaying books, borrowing a book, returning a book, assessing fines for damages, or exiting the library management section.

- If the user selects "3" in the main menu, a message is printed indicating the system is exiting, and the while loop is broken, ending the program.

- If the user enters an invalid choice in either the main menu or sub-menus, an appropriate error message is displayed, and the user is prompted to try again.


## SAMPLE OUTPUTS

> Customer Management: <br>

`main()` is used for initialising the front-end. <br>
Registering to the system

![image](https://github.com/Ananya22112308/Library_System/assets/118894662/e8a87767-238c-466b-b092-b86da41be028)
![image](https://github.com/Ananya22112308/Library_System/assets/118894662/d4512465-7323-4b4f-9e7b-9287cd91689b)
![image](https://github.com/Ananya22112308/Library_System/assets/118894662/0313f215-4af5-4116-a9fb-f03d846cb369)

---
> Library System: <br>

Borrowing a book

![image](https://github.com/Ananya22112308/Library_System/assets/118894662/60cca3d5-bfa3-4736-8c9b-88f9e50475be)
![image](https://github.com/Ananya22112308/Library_System/assets/118894662/4034e834-67c6-48d8-99b4-f9069dd746b2)

Getting an extension on the due date for a book

![image](https://github.com/Ananya22112308/Library_System/assets/118894662/d850e909-d22b-4679-9fc0-eda5e1488513)

Returning a book

![image](https://github.com/Ananya22112308/Library_System/assets/118894662/5332d223-6d83-48f9-baa2-0afee72aa36e)

Returning a damaged book

![image](https://github.com/Ananya22112308/Library_System/assets/118894662/331d1917-56d7-4696-a17e-91d48ff1895e)

error handling and exit

![image](https://github.com/Ananya22112308/Library_System/assets/118894662/9740877b-cd7f-43ed-a9da-d16426b2ca0b)

---
### Collaborators: <br>
Ananya Geetey (22112308) : https://github.com/Ananya22112308 <br>
Siddhi Jhanwar (22112334) : https://github.com/Siddhi22112334
