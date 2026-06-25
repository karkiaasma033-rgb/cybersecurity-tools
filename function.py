def greet(name):
    print ("hello " + name +"!")
    print("Welcome to cybersecurity!")

def check_port(port):
    if port == 631:
        print("Port " + str(port) + " is OPEN!")
    else:
        print("Port " + str(port) + "is CLOSED!")

def calculate_age(birth_year):
    current_year = 2026
    age = current_year - birth_year
    print("You are " + str(age) + "year old!")

greet("Aashma")
check_port(631)
check_port(80)
check_port(443)
calculate_age(2005)
