class Book:
    """
    A class representing a book with different types (hardcover and paperback).
    """
    TYPES = ("hardcover", "paperback")  # Class-level constant for book types.

    def __init__(self, name: str, book_type: str, weight: int):
        """
        Initialize a Book object.

        :param name: The name of the book.
        :param book_type: The type of the book (hardcover or paperback).
        :param weight: The weight of the book in grams.
        """
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        """
        Developer-friendly representation of the Book object.
        """
        return f"<Book(name={self.name!r}, book_type={self.book_type!r}, weight={self.weight})>"

    def __str__(self) -> str:
        """
        User-friendly string representation of the Book object.
        """
        return f"Book: {self.name}, Type: {self.book_type}, Weight: {self.weight}g"

    @classmethod
    def hardcover(cls, name: str, weight: int) -> "Book":
        """
        Create a hardcover book with an additional 100g weight for binding.

        :param name: The name of the book.
        :param weight: The base weight of the book in grams.
        :return: A Book instance with hardcover type.
        """
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name: str, weight: int) -> "Book":
        """
        Create a paperback book without additional weight.

        :param name: The name of the book.
        :param weight: The base weight of the book in grams.
        :return: A Book instance with paperback type.
        """
        return cls(name, cls.TYPES[1], weight)


# Example usage
if __name__ == "__main__":
    # Direct instantiation
    book_obj = Book("Harry Potter", "hardcover", 1500)
    print(book_obj)

    # Using class methods
    hardcover_book = Book.hardcover("Harry Potter", 1500)
    print(f"Hardcover Book: {hardcover_book}")

    paperback_book = Book.paperback("Python Crash Course", 1500)
    print(f"Paperback Book: {paperback_book}")
    print(f"Paperback Book: {repr(paperback_book)}")
