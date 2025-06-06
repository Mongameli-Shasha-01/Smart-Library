from datetime import date
from fastapi import FastAPI
from api.book_routes import router as book_router
from api.member_routes import router as member_router
from api.reservation_routes import router as reservation_router

from src.book import Book
from src.library_member import LibraryMember
from src.loan import Loan

# === FastAPI Setup ===
app = FastAPI(title="Smart Library API", version="1.0")

# Register API routers
app.include_router(book_router)
app.include_router(member_router)
app.include_router(reservation_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Library API"}

# === Demo Code for Domain Objects ===
def demo_library_operations():
    # Create a Book object
    book1 = Book(
        "The Hitchhiker's Guide to the Galaxy", "978-0345391802", 1979,
        ["Douglas Adams"], "Science Fiction", 1, "Pan Books", 10, 5, None
    )

    # Create a LibraryMember object
    member1 = LibraryMember(
        "LM001", "Alice", "Smith", date(1990, 5, 10),
        "alice@example.com", "555-1234", "123 Main St",
        date(2023, 1, 15), "Regular", "Active"
    )

    # Create a Loan object
    loan1 = Loan("LN001", book1, member1, date(2024, 1, 20), date(2024, 2, 10))

    # Demonstrate relationships
    print(f"{member1} borrowed {loan1.get_book().get_title()}")
    print(f"{loan1.get_book()} is borrowed by {loan1.get_member()}")

    # Example of using a method
    if book1.check_out():
        print(f"{book1.get_title()} checked out successfully")
    else:
        print(f"{book1.get_title()} is not available")

    # Returning the book
    if book1.return_book():
        print(f"{book1.get_title()} returned successfully")
    else:
        print(f"{book1.get_title()} could not be returned")


# Only run the demo code if executed directly
if __name__ == "__main__":
    demo_library_operations()
