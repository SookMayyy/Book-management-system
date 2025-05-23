# a program to become a personal book management system with the ability to add, delete, edit, display or search book records.

# datetime module to check for valid input format for year and dates
import datetime

# Define a class named 'Book' to represent the information of books 
class Book:
    book_list = [] # initialize an empty list to store instances of the 'Book' class
    # __init__ method is a constructor used to initialize the attributes of a book object when an instance of the class is created
    def __init__(self, isbn, author, title, publisher, genre, year_published, date_purchased, status):
        # Initialize the attributes of the book object with the values passed as parameters
        #self is a parameter name which represent the instance of the class 
        self.isbn = isbn
        self.author = author
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.year_published = year_published
        self.date_purchased = date_purchased
        self.status = status
        # initializing the attributes of a book instance with values passed as parameters

# Read data from the text file and store it in a list of Book objects
file_name = "books_StudentID.txt"
book_list = [] # initialize an empty list to store book objects
try:
    with open(file_name, 'r') as file: #open the text file as read mode
        for line in file:
            # Split the line into individual attributes using comma as a delimiter
            data = line.strip().split(',')

            # Create a Book object and append it to the list
            book = Book(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
            book_list.append(book)
            # Store the objects in the book list

except FileNotFoundError:
    print(f"File '{file_name}' not found. Please check your file name and rerun the program. ")
    exit() #exit the current program if file is not found

# Function 1
# Add new book record
def add_book_record():
    outer_loop = True
    while outer_loop:
    #prompt user to enter new book information
        print("Please fill in all the blanks and replace any commas (,) with semicolons (;)")
        isbn = input("Enter ISBN (13-digit): ") #13 digit
        if len(isbn) != 13 or not isbn.isdigit(): #if length not equal to 13, and isbn not equal to digit only 
            print("Invalid input. Please enter a 13 digit ISBN containing only digits. ")
            continue # skip all the code after this and repeat the outer_loop from the start

        author = input("Enter author: ")

        title = input("Enter title: ")

        publisher = input("Enter publisher: ")

        genre = input("Enter genre: ")

        while True:
            year_published = input("Enter year published (Format: YYYY): ") 

            # exception handling for date/time to make sure it is in year format
            try:
                user_year = datetime.datetime.strptime(year_published, "%Y") # parse string into year format
                if 1000 <= user_year.year <= datetime.datetime.now().year:
                    break  # Break the loop if a valid year is entered
                else:
                    print("Year must be between 1000 and the current year.")

            except ValueError:
                print("Invalid date format. Please enter a valid year of publication. ")  
                continue #skip the code after this and restart the current while loop

        while True:
            date_purchased = input("Enter date purchased (Format: DD-MM-YYYY): ")

            # exception handling for date/time to make sure valid date is entered
            try:
                user_date = datetime.datetime.strptime(date_purchased, "%d-%m-%Y")
                if 1000 <= user_date.year <= datetime.datetime.now().year:
                    break
                else:
                    print("Invalid year. Please enter a year between 1000 and the current year.")

            except ValueError:
                print("Invalid date format. Please enter a valid date in the format DD-MM-YYYY.")
                continue

        while True:
            status = input("Enter status (read/to-read): ")
            if status.lower() != "read" and status.lower() != "to-read":
                print("Enter read or to-read only. ")
            else:
                break

        # Input validation 
        # check for blanks 
        if not all([isbn, author, title, publisher, genre, year_published, date_purchased, status]):
            print("Please fill in all the required fields.")
            continue

        # check for commas
        if any(',' in field for field in [isbn, author, title, publisher, genre, year_published, date_purchased, status]):
            print("Please avoid using commas in any of the fields.")
            continue

        # Create a new Book object with the entered information
        new_book = Book(isbn, author, title, publisher, genre, year_published, date_purchased, status)

        # Add the new book object to the list of books
        book_list.append(new_book)

        print("Book added successfully.")

        while True:
            repeat = input("Do you want to add another book? (Y/N): ")
            if repeat.upper() == "Y":
                break #exit the inner loop 

            elif repeat.upper() == "N":
                outer_loop = False
                break #exit both inner and outer loop

            else:
                print("Please enter Y or N only.")
                continue 

        if not outer_loop:
            break

# Function 2
# Delete book record #try to make user can search book by keyword, and choose the one they want to delete
def delete_book_record():
    while True:
        # prompt user to enter information to identify the book
        author_to_delete = input("Enter author (leave empty if not searching by author): ")
        title_to_delete = input("Enter title (leave empty if not searching by title): ")

        # check if there is at least one input
        if not (author_to_delete or title_to_delete):
            print("Please enter at least one search criteria.")
            continue

        #create a list to store the matching books and books to delete
        to_delete_indices = []
        matching_books = []

        # Use a loop to find and delete the book with matching information
        for book in book_list:
            # author_to_delete != '' (check if the user entered a non-empty string for the author search criteria)
            # book.author.upper().find(author_to_delete.upper()) != -1:
            # (Converts both the user-entered author and the book's author to uppercase and checks if the user's author is a substring of the book's author)
            # != -1: (Checks if the result of find() is not equal to -1)
            # (If the substring is found in the book's author, find() returns an index greater than or equal to 0, and the condition becomes true. If the substring is not found, find() returns -1, and the condition becomes false.)
            if (author_to_delete != '' and book.author.upper().find(author_to_delete.upper()) != -1 ) or (title_to_delete != '' and book.title.upper().find(title_to_delete.upper()) != -1):
                #returns true if user's author/title is found in book's author/title
                matching_books.append(book)
                print(f"Isbn: {book.isbn}, Author: {book.author}, Title: {book.title}, Publisher: {book.publisher}, Genre: {book.genre}, Year Published: {book.year_published}, Date Purchased: {book.date_purchased}, Status: {book.status}")
        
        if not matching_books:
            print("Book not found. No changes made. ") 
            break

        if len(matching_books) > 0:
            if len(matching_books) > 1:
                print("Multiple books found. Please confirm deletion for each book:")   
            else: #if only one book is found
                print("Book found!")

            for i, book in enumerate(matching_books):
            # i is the index of current book
            # book represents the actual book object/value
            # enumerate used to iterate over the elements of matching_books
                while True:
                    confirmation = input(f"Do you want to delete this book ({book.title}) ? (Y/N): ")
                    if confirmation.upper() == "Y":
                        to_delete_indices.append(i)
                    elif confirmation.upper() == "N":
                        print("No changes made for this book.")
                    else:
                        print("Please enter Y or N only.")
                        continue
                    break
            break

    for i in to_delete_indices:
        deleted_book = matching_books[i]
        #remove the book from the list
        book_list.remove(deleted_book)
        print("Book deleted successfully.")
                        
# Function 3
# Update/edit book record
def update_book_record():
    while True:
        # search criteria (ISBN/author/title)
        isbn_to_update = input("Enter ISBN of the book to update (leave empty if not searching by ISBN): ")
        author_to_update = input("Enter author of the book to update (leave empty if not searching by author name): ")
        title_to_update = input("Enter title of the book to update (leave empty if not searching by title): ")

        if not (isbn_to_update or author_to_update or title_to_update):
            print("Please enter at least one search criteria.")
            continue

        matching_books = []
        to_update_indices = []
        original_book = None
    
        # Use a loop to find and update the book with matching information
        for book in book_list:
            # assign book class to variable original_book
            original_book = Book(book.isbn, book.author, book.title, book.publisher, book.genre, book.year_published, book.date_purchased, book.status)
            # search and print out for books matching with search criteria
            if (isbn_to_update != '' and book.isbn.find(isbn_to_update) != -1) or (author_to_update != '' and book.author.upper().find(author_to_update.upper()) != -1 ) or (title_to_update != '' and book.title.upper().find(title_to_update.upper()) != -1):
                print(f"Isbn: {book.isbn}, Author: {book.author}, Title: {book.title}, Publisher: {book.publisher}, Genre: {book.genre}, Year Published: {book.year_published}, Date Purchased: {book.date_purchased}, Status: {book.status}")
                matching_books.append(book)

        if not matching_books:
            print("Book not found. No changes made. ")
            break      

        if len(matching_books) > 0:
            if len(matching_books) > 1:
                print("Multiple books found. Please confirm updation for each book:")   
            else:
                print("Book found!")
            
            # loop to confirm whether to edit each book
            for i, book in enumerate(matching_books):
                while True:
                    confirmation = input(f"Do you want to update this book ({book.title}) ? (Y/N): ")
                    if confirmation.upper() == "Y":
                        to_update_indices.append(i) # add to list of books to edit
                    elif confirmation.upper() == "N":
                        print("No changes made for this book.")
                    else:
                        print("Please enter Y or N only.")
                        continue
                    break
            break

    while True:             
        for i in to_update_indices:
            #contains current information before any updates, i retrives from the matching books list
            original_book = matching_books[i] 
            # creating a copy of the original book with the same info
            original_book = Book(matching_books[i].isbn, matching_books[i].author, matching_books[i].title, matching_books[i].publisher, matching_books[i].genre, matching_books[i].year_published, matching_books[i].date_purchased, matching_books[i].status)
            #prompt user to enter new information for update
            while True:
                print("Please fill in all the blanks and replace any commas (,) with semicolons (;)")
                print(f"Isbn: {book.isbn}")
                book.isbn = input("Enter new ISBN (leave empty if not updating): ")
                if not book.isbn:
                    book.isbn = original_book.isbn
                    break
                if len(book.isbn) != 13 or not book.isbn.isdigit():
                    print("Invalid input. Please enter a 13 digit ISBN containing only digits. ")
                    continue
                else:
                    break

            print(f"Author: {book.author}")
            book.author = input("Enter new author (leave empty if not updating): ")
            if not book.author:
                book.author = original_book.author

            print(f"Title: {book.title}")
            book.title = input("Enter new title (leave empty if not updating): ")
            if not book.title:
                book.title = original_book.title

            print(f"Publisher: {book.publisher}")
            book.publisher = input("Enter new publisher (leave empty if not updating): ")
            if not book.publisher:
                book.publisher = original_book.publisher

            print(f"Genre: {book.genre}")
            book.genre = input("Enter new genre (leave empty if not updating): ")
            if not book.genre:
                book.genre = original_book.genre

            print(f"Year of publication: {book.year_published}")
            while True:
                book.year_published = input("Enter new year published (leave empty if not updating): ")
                if not book.year_published:
                    book.year_published = original_book.year_published
                    break

                #exception handling for date/time format             
                try:
                    user_year = datetime.datetime.strptime(book.year_published, "%Y")
                    if 1000 <= user_year.year <= datetime.datetime.now().year:
                        break  # Break the loop if a valid year is entered
                    else:
                        print("Year must be between 1000 and the current year.")

                except ValueError:
                    print("Invalid date format. Please enter a valid year of publication. ") #check this 
                    continue

            print(f"Date of Purchase: {book.date_purchased}")   
            while True:
                book.date_purchased = input("Enter new date purchased (leave empty if not updating): ")
                if not book.date_purchased:
                    book.date_purchased = original_book.date_purchased
                    break 
                if not book.date_purchased:
                    book.date_purchased = original_book.date_purchased

                # exception handling for valid date/time format
                try:
                    user_date = datetime.datetime.strptime(book.date_purchased, "%d-%m-%Y")
                    if 1000 <= user_date.year <= datetime.datetime.now().year:
                        break  # Break the loop if a valid year is entered
                    else:
                        print("Year must be between 1000 and the current year.")
                    break

                except ValueError:
                    print("Invalid date format. Please enter a valid date in the format DD-MM-YYYY.")
                    continue
                    
            print(f"Status: {book.status}")
            while True:
                book.status = input("Enter new status (leave empty if not updating): ")
                if not book.status:
                    book.status = original_book.status
                    break
                # check for valid input (read/to-read)
                if book.status != "read" and book.status != "to-read":
                    print("Enter read or to-read only. ")
                else:
                    break
                
        if any(',' in field for field in
            [book.isbn, book.author, book.title, book.publisher, book.genre, book.year_published,
            book.date_purchased, book.status]):
            print("Please avoid using commas in any of the fields.")
            continue

        else:
            print("Book updated successfully.")
            break

# Function 4
# Display all books in system
def display_all_books():
    
    # Check if there are no books in the list
    if not book_list:
        print("No books in the system.")
        return

    # Print column headings
    # left-aligned with a width of x characters
    print("{:<15} {:<20} {:<32} {:<27} {:<20} {:<15} {:<15} {:<10}".format(
        "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status")
        )
    
    title_width = 30 # set width for wrapping

    # Iterate through the list of books and print their information
    for book in book_list:
        wrapped_title_lines = [book.title[i:i + title_width] for i in range(0, len(book.title), title_width)]
        # book.title[i:i + title_width] (slicing operation)
        # (starts from the index i and goes up to i + title_width)
        # (each value of i obtained from the range function where it cannot exceed the title_width set)

        # print the first line with the rest of the information
        print("{:<15} {:<20} {:<32} {:<27} {:<20} {:<15} {:<15} {:<10}".format(
            book.isbn,
            book.author,
            wrapped_title_lines[0], #print the first line of the wrapped title
            book.publisher,
            book.genre,
            book.year_published,
            book.date_purchased,
            book.status,
            )
        )

        # for other lines in wrapped title 
        for line in wrapped_title_lines[1:]:
            print("{:<15} {:<20} {:<32} {:<27} {:<15} {:<15} {:<15} {:<10}".format(
            "", "", line, "", "", "", "", "") #print the next few lines in title 
        )
        
# Function 5
# Search for a book by ISBN, author, and title
def search_for_book():
    outer_loop = True
    while outer_loop:
        # Prompt the user to enter information for the search
        isbn_to_search = input("Enter ISBN (leave empty if not searching by ISBN): ")
        author_to_search = input("Enter author (leave empty if not searching by author): ")
        title_to_search = input("Enter title (leave empty if not searching by title): ")

        if not (isbn_to_search or author_to_search or title_to_search):
            print("Please enter at least one search criteria.")
            continue

        #create a list to store the matching books
        matching_books = []

        # Iterate through the list of books and display information for matching books
        for book in book_list:
           if (isbn_to_search != '' and book.isbn.find(isbn_to_search) != -1) or (author_to_search != '' and book.author.upper().find(author_to_search.upper()) != -1 ) or (title_to_search != '' and book.title.upper().find(title_to_search.upper()) != -1):
                    matching_books.append(book)
                    print("\nBook found!")
                    # Display information for the matching book
                    # Print column headings
                    print("{:<15} {:<20} {:<32} {:<27} {:<20} {:<15} {:<15} {:<10}".format(
                        "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status")
                         )
    
                    title_width = 30 # set width for wrapping

                    # Iterate through the list of books and print their information
                    for book in matching_books:
                        wrapped_title_lines = [book.title[i:i + title_width] for i in range(0, len(book.title), title_width)]

                    # print the first line with the rest of the information
                    print("{:<15} {:<20} {:<32} {:<27} {:<20} {:<15} {:<15} {:<10}".format(
                    book.isbn,
                    book.author,
                    wrapped_title_lines[0],
                    book.publisher,
                    book.genre,
                    book.year_published,
                    book.date_purchased,
                    book.status,
                        )
                    )

                    # for other lines
                    for line in wrapped_title_lines[1:]:
                        print("{:<15} {:<20} {:<32} {:<27} {:<15} {:<15} {:<15} {:<10}".format(
                        "", "", line, "", "", "", "", "")
                    )
                
        # If no matching books are found, print a message
        if not matching_books:
            print("No matching books found.")
            break

        while True:
            repeat = input("\nDo you want to search another book? (Y/N): ")
            if repeat.upper() == "Y":
                break

            elif repeat.upper() == "N":
                outer_loop = False
                break
            
            else:
                print("Please enter Y or N only.")
                continue
        
        if not outer_loop:
            break

# Main program loop
def print_welcome_message():
    outer_loop = True
    while outer_loop:
        cute_icon = r"""
                 ╭────────────────────────────────────╮
         /\_/\   │     Welcome to Your Book System    │    /\_/\
        ( o.o )  │                                    │   ( o.o )
         > ^ <   │    📚🌈💖 Happy Reading! 💖🌈📚    │    > ^ <
                 ╰────────────────────────────────────╯
        """
        print(cute_icon)

        start_program = input("Press Enter to start the program: ")
        if not start_program:
            while True:
                print("\n===== Main Menu =====")
                print("1. Add Book Record(s)")
                print("2. Delete Book Record(s)")
                print("3. Update/Edit Book Record(s)")
                print("4. Display All Books")
                print("5. Search for Book(s)")
                print("6. Write to file and Exit")

                # Prompt the user to choose an option
                choice = input("Enter your choice (1-6): ")

                # Perform the corresponding action based on the user's choice
                match (choice):
                    case '1':
                        add_book_record()

                    case '2':
                        delete_book_record()

                    case '3':
                        update_book_record()

                    case '4':
                        display_all_books()

                    case '5':
                        search_for_book()

                    case '6':
                        with open(file_name, 'w') as file:
                            for book in book_list:
                                book_info = f"{book.isbn},{book.author},{book.title},{book.publisher},{book.genre}," \
                                            f"{book.year_published},{book.date_purchased},{book.status}\n"
                                file.write(book_info)
                        print("Data writen to file. Exiting...")
                        cute_icon = r"""
                ╭────────────────────────────────────╮
        /\_/\   │    Goodbye from Your Book System   │    /\_/\
       ( o.o )  │                                    │   ( o.o )
        > ^ <   │    📚🌈💖 Happy Reading! 💖🌈📚    │    > ^ <
                ╰────────────────────────────────────╯
                        """
                        print(cute_icon)
                        outer_loop = False
                        break #break the inner loop

                    case _ : #nothing match function
                        print("Invalid choice. Please enter a number between 1 and 6.")
                        continue

        if not outer_loop:
            break #break the outer loop

# Call the function to display 
print_welcome_message()
