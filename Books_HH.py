import json
import os

class BookStore:

    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, title: str, author: str, year: int):
        book = {
            "id": self.next_id,
            "title": title.strip(),
            "author": author.strip(),
            "year": year
        }
        self.books.append(book)
        self.next_id += 1

        return book.copy()
    
    def get_book(self, book_id: int):
        if not self.books:
            raise ValueError("Catalog is empty")
        
        try:
            book_id = int(book_id)
        except ValueError:
            raise ValueError("book_id must be an integer")
        
        for book in self.books:
            if book["id"] == book_id:
                return book.copy()
        raise ValueError(f"Book with id={book_id} not found")
    

    def list_books(self) -> list[dict]:
        return [book.copy() for book in self.books]

    def delete_book(self, book_id):
        if not self.books:
            raise ValueError(f"Book with id={book_id} not found")
        
        try:
            book_id = int(book_id)
        except ValueError:
            raise ValueError("book_id must be an integer")
        
        for i, book in enumerate(self.books):
            if book["id"] == book_id:
                deleted_book = book.copy()
                del self.books[i]
                return deleted_book
        raise ValueError(f"Book wiht id={book_id} is not found")

    def save(self, path: str = "books.json") -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.books, f, ensure_ascii=False, indent=2)

    def load(self, path: str = "books.json") -> None:
        if not os.path.exists(path):
            self.books = []
            self.next_id = 1
            return

        with open(path, "r", encoding="utf-8") as f:
            self.books = json.load(f)

        if self.books:
            max_id = max(book["id"] for book in self.books)
            self.next_id = max_id + 1
        else:
            self.next_id = 1

def run_cli():
    store = BookStore()
    store.load()

    while True:
        command = input("> ").strip()

        if command == "exit":
            store.save()
            print("Bye!")
            break

        elif command == "help":
            print("Commands:")
            print("  add     - add a new book")
            print("  list    - show all books")
            print("  get     - get a book by id")
            print("  delete  - delete a book by id")
            print("  exit    - save and exit")

        elif command == "add":
            try:
                title = input("Title: ").strip()
                if not title:
                    raise ValueError("Title cannot be empty")
                author = input("Author: ").strip()
                if not author:
                    raise ValueError("Author cannot be empty")
                year_str = input("Year: ")

                year = int(year_str)

                book = store.add_book(title, author, year)
                print(f"Added: {book}")
            except ValueError as e:
                print(f"Error: {e}")

        elif command == "get":
            try:
                book_id = input("Book_id: ").strip()
                book = store.get_book(book_id)
                print(f"Found: {book}")
            except ValueError as e:
                print(f"Error: {e}")

        elif command =="delete":
            try:
                book_id = input("Book_id: ").strip()
                book = store.delete_book(book_id)
                print(f"Deleted: {book}")
            except ValueError as e:
                print(f"Error: {e}")

        elif command == "list":
            books = store.list_books()
            if not books:
                print("Catalog is empty")
            else:
                for b in books:
                    print(f'{b["id"]}. "{b["title"]}" — {b["author"]} ({b["year"]})')

        else:
            print("Unknown command")
if __name__ == "__main__":
    run_cli()