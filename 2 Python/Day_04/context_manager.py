# context manager automatically closed the file that we open 
# creating our own context manager
class Max : 
    x = 10
    def __init__(self):
        print("Hello Constructor of Max")
        pass


class context_manager :
    
    # The first one is obviously the class constructor that doesn't accept any parameter yet. It'll be responsible for accepting a database path: 
    def __init__(self):
        pass


    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc, tb):
        pass

with open('/home/anjali/GitHub/Kodvix-Data-Engineer/my.txt', 'w') as test_file : 
    test_file.write("I am the one who is writing inside the file\n")
    test_file.write("I am the one who is writing inside the file\n")
    try : 
        num = 1 / 0
    except ZeroDivisionError as z : 
        print(z)
    except: 
        print("File handled")
    finally : 
        test_file.write("Finally I am writing here\n")

    test_file.write("I am the one who is writing inside the file\n")
    test_file.write("I am the one who is writing inside the file\n")

