import json

save = {}
books = []
print('Welcome to PyLibrary cmd line. \n')

with open('books.txt', 'r') as i:
    books = i.read().splitlines()
with open('save.json', 'r') as i:
    save = json.load(i)
        

while True:
    cmd = input('> ')
    if cmd == 'addbook':
        print('What book wolud you like to add?')
        cmd = input('> ')
        books.append(cmd)
    elif cmd == 'borrow':
        xid = input('What is the book? > ')
        user = input('What is the user? > ')
        save[xid] = user
    elif cmd == 'save':
        print('Now saving...')
        with open('save.json', 'r+') as i:
            json.dump(save, i)
            try:    
                save = json.load(i)
            except:
                pass
    elif cmd == 'status':
        for i in range(len(save)):
            print('Book ' + books[i] + ' belongs to ' + save[books[i]])

