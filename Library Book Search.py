#Library Book Search
books = ["Physics", "Biology", "Maths", "Science"]

book = input("Enter book name: ")

if book in books:
    print("Book available in library")
else:
    print("Book not available")