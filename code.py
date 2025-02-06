class BookNode:
    def __init__(self, book_id, title, author):
        # Initialize a new book node with ID, title, author, and a pointer to the next node
        self.book_id = book_id
        self.title = title
        self.author = author
        self.next = None  # Pointer to the next book node


class UserNode:
    def __init__(self, user_id, name, status):
        # Initialize a new user node with ID, name, status, and a pointer to the next node
        self.user_id = user_id
        self.name = name
        self.status = status
        self.next = None  # Pointer to the next user node


class TransactionNode:
    def __init__(self, transaction_id, user_id, book_id, borrow_date):
        # Initialize a new transaction node with transaction ID, user ID, book ID, borrow date, and a pointer to the next node
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.next = None  # Pointer to the next transaction node


class BookLinkedList:
    def __init__(self):
        # Initialize the linked list with a head pointer
        self.head = None

    def add_book(self, book_id, title, author):
        # Create a new book node and add it to the end of the linked list
        new_book = BookNode(book_id, title, author)
        if not self.head:  # If the list is empty, set the new book as the head
            self.head = new_book
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_book  # Add the new book at the end

    def remove_book(self, book_id):
        # Remove a book from the linked list by its ID
        current = self.head
        previous = None
        while current:
            if current.book_id == book_id:  # If the book is found
                if previous:  # If it's not the head
                    previous.next = current.next  # Bypass the current node
                else:  # If it is the head
                    self.head = current.next  # Move head to the next node
                return True  # Indicate success
            previous = current
            current = current.next
        return False  # Indicate failure if book not found

    def search_book(self, book_id=None, title=None):
        # Search for a book by ID or title
        current = self.head
        while current:
            # Check if either the book ID or title matches
            if (book_id and current.book_id == book_id) or (title and current.title.lower() == title.lower()):
                return current  # Return the found book node
            current = current.next
        return None  # Return None if not found

    def display_books(self):
        # Display all books in the linked list
        current = self.head
        while current:
            print(f"ID: {current.book_id}, Title: {current.title}, Author: {current.author}")
            current = current.next  # Move to the next book


class UserLinkedList:
    def __init__(self):
        # Initialize the linked list with a head pointer
        self.head = None

    def add_user(self, user_id, name, status='Active'):
        # Create a new user node and add it to the end of the linked list
        new_user = UserNode(user_id, name, status)
        if not self.head:  # If the list is empty, set the new user as the head
            self.head = new_user
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_user  # Add the new user at the end

    def deactivate_user(self, user_id):
        # Deactivate a user by changing their status to 'Inactive'
        current = self.head
        while current:
            if current.user_id == user_id:  # If the user is found
                current.status = 'Inactive'  # Change status
                return True  # Indicate success
            current = current.next
        return False  # Indicate failure if user not found

    def search_user(self, user_id=None, name=None):
        # Search for a user by ID or name
        current = self.head
        while current:
            # Check if either the user ID or name matches
            if (user_id and current.user_id == user_id) or (name and current.name.lower() == name.lower()):
                return current  # Return the found user node
            current = current.next
        return None  # Return None if not found

    def display_users(self):
        # Display all users in the linked list
        current = self.head
        while current:
            print(f"ID: {current.user_id}, Name: {current.name}, Status: {current.status}")
            current = current.next  # Move to the next user


class TransactionLinkedList:
    def __init__(self):
        # Initialize the linked list with a head pointer
        self.head = None

    def record_transaction(self, transaction_id, user_id, book_id, borrow_date):
        # Create a new transaction node and add it to the end of the linked list
        new_transaction = TransactionNode(transaction_id, user_id, book_id, borrow_date)
        if not self.head:  # If the list is empty, set the new transaction as the head
            self.head = new_transaction
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_transaction  # Add the new transaction at the end

    def remove_transaction(self, transaction_id):
        # Remove a transaction from the linked list by its ID
        current = self.head
        previous = None
        while current:
            if current.transaction_id == transaction_id:  # If the transaction is found
                if previous:  # If it's not the head
                    previous.next = current.next  # Bypass the current node
                else:  # If it is the head
                    self.head = current.next  # Move head to the next node
                return True  # Indicate success
            previous = current
            current = current.next
        return False  # Indicate failure if transaction not found

    def display_transactions(self):
        # Display all transactions in the linked list
        current = self.head
        while current:
            print(f"Transaction ID: {current.transaction_id}, User ID: {current.user_id}, Book ID: {current.book_id}, Date: {current.borrow_date}")
            current = current.next  # Move to the next transaction

    def reverse_transactions(self):
        # Reverse the linked list of transactions
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current
            current = next_node  # Move to the next node
        self.head = prev  # Update head to the new first node


def main():
    # Create instances of the linked lists for books, users, and transactions
    book_list = BookLinkedList()
    user_list = UserLinkedList()
    transaction_list = TransactionLinkedList()

    while True:
        # Display the main menu for the Smart Library System
        print("\nWelcome to the Smart Library System!")
        print("1. Manage Books")
        print("   1.1 Add a Book")
        print("   1.2 Remove a Book")
        print("   1.3 Search a Book")
        print("   1.4 Display Books")
        print("2. Manage Users")
        print("   2.1 Add a User")
        print("   2.2 Deactivate a User")
        print("   2.3 Search a User")
        print("   2.4 Display Users")
        print("3. Manage Transactions")
        print("   3.1 Record a Transaction")
        print("   3.2 Remove a Transaction")
        print("   3.3 Display Transactions")
        print("   3.4 Reverse Transactions")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1.1":
            # Add a new book
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book_list.add_book(book_id, title, author)
            print("Book added successfully!")
        elif choice == "1.2":
            # Remove a book by ID
            book_id = input("Enter book ID to remove: ")
            if book_list.remove_book(book_id):
                print("Book removed successfully!")
            else:
                print("Book not found!")
        elif choice == "1.3":
            # Search for a book by ID or title
            book_id = input("Enter book ID to search (or press Enter to search by title): ")
            title = input("Enter book title (or press Enter to skip): ")
            book = book_list.search_book(book_id if book_id else None, title if title else None)
            if book:
                print(f"Book found - ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
            else:
                print("Book not found!")
        elif choice == "1.4":
            # Display all books
            book_list.display_books()
        elif choice == "2.1":
            # Add a new user
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user_list.add_user(user_id, name)
            print("User  added successfully!")
        elif choice == "2.2":
            # Deactivate a user by ID
            user_id = input("Enter user ID to deactivate: ")
            if user_list.deactivate_user(user_id):
                print("User  deactivated successfully!")
            else:
                print("User  not found!")
        elif choice == "2.3":
            # Search for a user by ID or name
            user_id = input("Enter user ID to search (or press Enter to search by name): ")
            name = input("Enter user name (or press Enter to skip): ")
            user = user_list.search_user(user_id if user_id else None, name if name else None)
            if user:
                print(f"User  found - ID: {user.user_id}, Name: {user.name}, Status: {user.status}")
            else:
                print("User  not found!")
        elif choice == "2.4":
            # Display all users
            user_list.display_users()
        elif choice == "3.1":
            # Record a new transaction
            transaction_id = input("Enter transaction ID: ")
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            borrow_date = input("Enter borrow date: ")
            transaction_list.record_transaction(transaction_id, user_id, book_id, borrow_date)
            print("Transaction recorded successfully!")
        elif choice == "3.2":
            # Remove a transaction by ID
            transaction_id = input("Enter transaction ID to remove: ")
            if transaction_list.remove_transaction(transaction_id):
                print("Transaction removed successfully!")
            else:
                print("Transaction not found!")
        elif choice == "3.3":
            # Display all transactions
            transaction_list.display_transactions()
        elif choice == "3.4":
            # Reverse the list of transactions
            transaction_list.reverse_transactions()
            print("Transactions reversed successfully!")
        elif choice == "4":
            # Exit the program
            print("Exiting Smart Library System. Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()  # Start the program
