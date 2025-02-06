 In this assignment, you will implement a Smart Library System that uses linked lists to manage books, users, and borrowing transactions. This will give you hands-on experience with linked list operations, including insertion, deletion, traversal, searching, and reversing.

Problem Statement (Practical Context):
You are hired by a library to develop a system to manage its day-to-day operations. The library wants to:
Keep track of the books available.
Maintain a user list (students who borrow books).
Record and manage borrowing transactions (who borrowed which book).
Your task is to design a Linked List-based Smart Library System to handle these functionalities.

Requirements:
You must implement the following features using linked lists:
1. Manage Books (25 points)
Each book should have:
A unique ID (e.g., B001, B002, etc.).
A title (e.g., "Python Programming").
Author name (e.g., "John Doe").
Create a linked list of books where you can:
Add a new book to the library (at the end).
Remove a book when it is permanently removed from the library (by ID).
Search for a book by its ID or title and display its details.

2. Manage Users (25 points)
Each user should have:
A unique User ID (e.g., U001, U002, etc.).
Name of the user (e.g., "Alice Johnson").
Membership status (Active or Inactive).
Create a linked list of users where you can:
Add a new user to the system (at the end).
Deactivate a user (mark their membership as inactive).
Search for a user by their ID or name and display their details.

3. Borrowing Transactions (30 points)
Each borrowing transaction should have:
Transaction ID (e.g., T001).
User ID (who borrowed the book).
Book ID (which book was borrowed).
Borrowing date (e.g., 2025-01-24).
Create a linked list of transactions where you can:
Record a new borrowing transaction.
Remove a transaction when a book is returned (based on the transaction ID).
Display all transactions.

4. Reverse the Linked List of Transactions (20 points)
Implement a feature to reverse the linked list of transactions.
This is useful for displaying the borrowing history in reverse chronological order.


Program Design Guidelines:
Node Classes:
 Create separate node classes for books, users, and transactions.


Linked List Classes:
 Implement separate linked list classes for managing books, users, and transactions.


Menu System:
 Create a user-friendly menu-driven program to:


Add, remove, and search books.
Add, deactivate, and search users.
Record, delete, and display transactions.
Reverse and display transactions.

Sample Menu Output:
Welcome to the Smart Library System!
1. Manage Books
   1.1 Add a Book
   1.2 Remove a Book
   1.3 Search for a Book
   1.4 Display All Books
2. Manage Users
   2.1 Add a User
   2.2 Deactivate a User
   2.3 Search for a User
   2.4 Display All Users
3. Manage Transactions
   3.1 Record a Transaction
   3.2 Remove a Transaction
   3.3 Display All Transactions
   3.4 Reverse Transaction List
4. Exit
Enter your choice: 


Submission Instructions:
Submit the Python code in a .py file with comments explaining each section.
Include a README file that describes your approach, challenges, and how the system works.
Provide sample input/output for each functionality.

Evaluation Criteria:
Linked List Implementation (60 points): Correct implementation of linked lists for books, users, and transactions.
Features (30 points): Functional menu options and operations (add, remove, search, reverse).
Code Clarity and Comments (10 points): Code readability and clear explanations through comments.
