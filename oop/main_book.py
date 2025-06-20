from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    
    print(my_book)  # __str__ method
    print(repr(my_book))  # __repr__ method

    del my_book  # triggers __del__

    if __name__ == "__main__":
        main()