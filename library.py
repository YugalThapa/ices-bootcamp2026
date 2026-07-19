class library():
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            print("Book already exists.")
        else:
            self.books[title] = author
            print("Book successfully added.")

    def remove_book(self, title):
        if title in self.books:
            self.books.pop(title)
            print(f"{title} book removed successfully.")
        else:
            print("Book not found.")

    def search_book(self, title):
        if title in self.books:
            print("Book found.")
            print(f"Title: {title} | Author: {self.books[title]}")
        else:
            print("Book not found.")

    def display_all(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("--Available books--")
            for title, author in self.books.items():
                print(f"Title: {title} | Author: {self.books[title]}")


def main():
    wrc_library = library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            wrc_library.add_book(title,author)
            

        elif choice == "2":
            title = input("Enter Book Title to remove: ")
            wrc_library.remove_book(title)

        elif choice == "3":
            title = input("Enter Book Title to search: ")
            wrc_library.search_book(title)

        elif choice == "4":
            wrc_library.display_all()

        elif choice == "5":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()