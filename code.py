class BookNode:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.next = None


class UserNode:
    def __init__(self, user_id, name, status):
        self.user_id = user_id
        self.name = name
        self.status = status
        self.next = None


class TransactionNode:
    def __init__(self, transaction_id, user_id, book_id, borrow_date):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.next = None


class BookLinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if not self.head:
            self.head = new_book
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_book

    def remove_book(self, book_id):
        current = self.head
        previous = None
        while current:
            if current.book_id == book_id:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def search_book(self, book_id=None, title=None):
        current = self.head
        while current:
            if (book_id and current.book_id == book_id) or (title and current.title.lower() == title.lower()):
                return current
            current = current.next
        return None

    def display_books(self):
        current = self.head
        while current:
            print(f"ID: {current.book_id}, Title: {current.title}, Author: {current.author}")
            current = current.next


class UserLinkedList:
    def __init__(self):
        self.head = None

    def add_user(self, user_id, name, status='Active'):
        new_user = UserNode(user_id, name, status)
        if not self.head:
            self.head = new_user
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_user

    def deactivate_user(self, user_id):
        current = self.head
        while current:
            if current.user_id == user_id:
                current.status = 'Inactive'
                return True
            current = current.next
        return False

    def search_user(self, user_id=None, name=None):
        current = self.head
        while current:
            if (user_id and current.user_id == user_id) or (name and current.name.lower() == name.lower()):
                return current
            current = current.next
        return None

    def display_users(self):
        current = self.head
        while current:
            print(f"ID: {current.user_id}, Name: {current.name}, Status: {current.status}")
            current = current.next


class TransactionLinkedList:
    def __init__(self):
        self.head = None

    def record_transaction(self, transaction_id, user_id, book_id, borrow_date):
        new_transaction = TransactionNode(transaction_id, user_id, book_id, borrow_date)
        if not self.head:
            self.head = new_transaction
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_transaction

    def remove_transaction(self, transaction_id):
        current = self.head
        previous = None
        while current:
            if current.transaction_id == transaction_id:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def display_transactions(self):
        current = self.head
        while current:
            print(f"Transaction ID: {current.transaction_id}, User ID: {current.user_id}, Book ID: {current.book_id}, Date: {current.borrow_date}")
            current = current.next

    def reverse_transactions(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


def main():
    book_list = BookLinkedList()
    user_list = UserLinkedList()
    transaction_list = TransactionLinkedList()

    while True:
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
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book_list.add_book(book_id, title, author)
            print("Book added successfully!")
        elif choice == "1.2":
            book_id = input("Enter book ID to remove: ")
            if book_list.remove_book(book_id):
                print("Book removed successfully!")
            else:
                print("Book not found!")
        elif choice == "1.3":
            book_id = input("Enter book ID to search (or press Enter to search by title): ")
            title = input("Enter book title (or press Enter to skip): ")
            book = book_list.search_book(book_id if book_id else None, title if title else None)
            if book:
                print(f"Book found - ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
            else:
                print("Book not found!")
        elif choice == "1.4":
            book_list.display_books()
        elif choice == "2.1":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user_list.add_user(user_id, name)
            print("User added successfully!")
        elif choice == "2.2":
            user_id = input("Enter user ID to deactivate: ")
            if user_list.deactivate_user(user_id):
                print("User deactivated successfully!")
            else:
                print("User not found!")
        elif choice == "2.3":
            user_id = input("Enter user ID to search (or press Enter to search by name): ")
            name = input("Enter user name (or press Enter to skip): ")
            user = user_list.search_user(user_id if user_id else None, name if name else None)
            if user:
                print(f"User found - ID: {user.user_id}, Name: {user.name}, Status: {user.status}")
            else:
                print("User not found!")
        elif choice == "2.4":
            user_list.display_users()
        elif choice == "3.1":
            transaction_id = input("Enter transaction ID: ")
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            borrow_date = input("Enter borrow date: ")
            transaction_list.record_transaction(transaction_id, user_id, book_id, borrow_date)
            print("Transaction recorded successfully!")
        elif choice == "3.2":
            transaction_id = input("Enter transaction ID to remove: ")
            if transaction_list.remove_transaction(transaction_id):
                print("Transaction has been removed successfully!")
            else:
                print("Transaction not found!")
        elif choice == "3.3":
            transaction_list.display_transactions()
        elif choice == "3.4":
            transaction_list.reverse_transactions()
            print("Transactions has been reversed successfully!")
        elif choice == "4":
            print("Exiting Smart Library System. Goodbye Motion Family!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()

