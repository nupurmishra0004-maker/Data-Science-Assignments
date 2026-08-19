# Python Assignment 1
# Library_Management system
books = []

while True:
    print("\n===== Library Management system =====")
    print("1. Add New Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Display Available Books")
    print("9. Display Issued Book")
    print("10. Exit")
    choice = input("Enter your choice (1-10):")
    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title ")
        author = input("Enter Author Name: ")

        book = {
            "Book ID": book_id,
            "Title": title,
            "Author": author,
            "Status": "Available"
        }

        books.append(book)
        print("Book added successfully!")
    elif choice == "2":
        if len(books) == 0:
            print("No books available in the library.")
        else:
            for book in books:
                print(book)
    elif choice == "3":
        print("Search by:")
        print("1. Book ID")
        print("2. Book Title")
        print("3. Author Name")
        search_choice = input("Enter search choice (1-3):")

        if search_choice == "1":
            search_id = input("Enter Book ID to search: ")
            found = False
            for book in books:
                if book["Book ID"] == search_id:
                    print("Book found:")
                    print(book)
                    found = True
                    break
            if found == False:
                print("Book not found.")

        elif search_choice == "2":
            search_title = input("Enter Book Title to search: ")
            found = False
            for book in books:
                if book["Title"].lower() == search_title.lower():
                    print("Book found:")
                    print(book)
                    found = True
                    break

            if found == False:
                print("Book not found.")

        elif search_choice == "3":
            search_author = input("Enter Author Name to search: ")
            found = False
            for book in books:
                if book["Author"].lower() == search_author.lower():
                    print("Book found:")
                    print(book)
                    found = True
                    break

            if found == False:
                print("Book not found.")
    elif choice == "4":
        update_id = input("Enter Book ID to update: ")
        found = False
        for book in books:
            if book["Book ID"] == update_id:
                new_title = input("Enter New Book Title: ")
                new_author = input("Enter New Author Name: ")
                book["Title"] = new_title
                book["Author"] = new_author
                print("Book updated successfully!")
                found = True
                break

        if found == False:
            print("Book not found.")
    elif choice == "5":
        delete_id = input("Enter Book ID to delete: ")
        found = False
        for book in books:
            if book["Book ID"] == delete_id:
                books.remove(book)
                print("Book deleted successfully!")
                found = True
                break

        if found == False:
            print("Book not found.")
    elif choice == "6":
        issue_id = input("Enter Book ID to issue: ")
        found = False
        for book in books:
            if book["Book ID"] == issue_id:
                if book["Status"] == "Available":
                    student_name = input("Enter Student Name: ")
                    book["Status"] = "Issued"
                    book["Issued To"] = student_name
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
            found = True
            break

        if found == False:
            print("Book not found.")
    elif choice == "7":
        return_id = input("Enter Book ID to return: ")
        found = False
        for book in books:
            if book["Book ID"] == return_id:
                if book["Status"] == "Issued":
                    book["Status"] = "Available"
                    book.pop("Issued To", None)
                    print("Book returned successfully!")
                else:
                    print("Book is not currently issued.")
                found = True
                break

        if found == False:
            print("Book not found.")
    elif choice == "8":
        found = False
        for book in books:
            if book["Status"] == "Available":
                print(book)
                found = True

        if found == False:
            print("Not available books.")
    elif choice == "9":
        found = False
        for book in books:
            if book["Status"] == "Issued":
                print(book)
                found = True

                
        if found == False:
            print("No issued book.")
    elif choice == "10":
        print("Existing Library Management system...")
        break