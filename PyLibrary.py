import json

addjson = {}
books = []
print('Welcome to PyLibrary cmd line. \n')

with open('books.txt', 'r') as i:
    books = i.read().splitlines()
def writefile(file, book, id):
    with open(file, 'a') as i:
        addjson[str(id)] = {"book": book}
        json.dump(addjson, i)
        

while True:
    cmd = input('> ')
    if cmd == 'addbook':
        print('What book wolud you like to add?')
        cmd = input('> ')
        books.append(cmd)
    elif cmd == 'borrow':
        xid = input('What is the book? > ')
        user = input('What is the user? > ')
        #print(books)

