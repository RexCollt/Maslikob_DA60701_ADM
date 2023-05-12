from Other.ClassFuncDb import *

if __name__ == '__main__':
    db = dbFunctions
    print(f"Введите параметр:\ninit\nfill\nshow [tablename]") 
    while True:
        consoleInput = str.lower(input('Input:'))
        if consoleInput == 'init':
            db.createDb()
        elif consoleInput == 'fill':
            db.fillDb()
        elif consoleInput == 'show clients':
            db.showClientsDb()
        elif consoleInput == 'show orders':
            db.showOrdersDb()
        else:
            print(f"Not Found!")
