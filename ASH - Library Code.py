print()
txt = "Welcome To Our Library"
b = txt.center(50)
print(b)
print()


def main():
	print("Enter 1 to Add a book ")
	print("Enter 2 to View book List")
	print("Enter 3 to Issue a book ")
	print("Enter 4 to View Issued books")
	print("Enter 5 to Exit")
	choice = int(input("Enter Your Choice: "))
	print()
	print()

	while choice != 5:
		if choice == 1:
			add = addbook()
			print(add)
		elif choice == 2:
			view = viewbook()
			print(view)
		elif choice == 3:
			issue = issuebook_fcfs() # Use FCFS for book issuance
			print(issue)
		else:
			issued = issuelist()
			print(issued)

		print("Enter 1 to Add a book ")
		print("Enter 2 to View book List")
		print("Enter 3 to Issue a book ")
		print("Enter 4 to View Issued books")
		print("Enter 5 to Exit")
		choice = int(input("Enter your Choice (1-5): "))
	print("Thank you for visiting our Library!")


def addbook():
	book = open("books.txt", "a")
	newbook = input("Enter Book to add: ")
	book.write(newbook)
	book.write("\n")
	print("Book has been added to the collection")
	book.close()
	print()


def viewbook():
	print("BookList:")
	print()
	booklist = []
	book = open("books.txt", "r")
	for line in book:
		books = line
		booklist.append(books)

	for x in booklist:
		x.strip()
		print(x)

	book.close()


def issuebook_fcfs():
	print("BookList:")
	booklist = []
	book = open("books.txt", "r")
	for line in book:
		books = line
		booklist.append(books)

	for x in booklist:
		x.strip()
		print(x)

	book.close()

	names = open("name.txt", "a")
	name = input("Enter Your Full Name : ")
	email = input("Enter Your Email: ")
	bookname = input("Enter Book Name from List: ")
	names.write(name)
	names.write("\n")
	names.write(email)
	names.write("\n")
	names.write(bookname)
	names.write("\n")
	names.write("\n")
	names.close()

	print("The Book", bookname, "Issued to", name, "Successfully")


def issuelist():
	issuename = []
	i = open("name.txt", "r")
	for line in i:
		names = line
		issuename.append(names)

	for x in issuename:
		x.strip()
		print(x)

	i.close()


main()
