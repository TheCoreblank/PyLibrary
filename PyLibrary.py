import json

addjson = {}

print('Welcome to PyLibrary cmd line. \n')

def writefile(file, book, id):
    with open(file, 'a') as i:
        addjson[str(id)] = {"book": book}
        json.dump(addjson, i)
        

while True:
    cmd = input('> ')
    if cmd == 'addbook':
        print('What book wolud you like to add?')
        cmd = input('> ')
        xid = input('What id? >')
        writefile('books.json', cmd, xid)
    elif cmd == 'borrow':
        xid = input('What is the id? >')
        user = input('What is the user id?')
        with open('users.json', 'a+') as i:
            i = i.read()
            xfile = json.loads(i)
            xfile[str(xid)]["books"].append(xid)
            json.dump(xfile, i)

