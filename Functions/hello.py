def hello():
    print("Hello AkiraChix")    

def hello2(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    print(f"Hello {name} you were born in {2024-age}")   

def my_country(country="Uganda"):
    print(f"Hello AkiraChix from {country}")    


def hello(name):#function only has one argument. 
    print(f"Hello {name}")
     

def greet(*names):#coverts all arguments to a list of arguments.
    for name in names:
        print(f"Hello {name}")


def create_sentence(**words):
    print(words)
    sentence =""
    for word in words.values():
        sentence+=word
        sentence+=" "
    return sentence


def sum_and_greet(*args , **kwargs):
    total =0
    for x in args:
        total +=x

    f = kwargs["first_name"]
    l = kwargs["last_name"]

    greeting = f"Hello {f} {l} total of your numbers is {total}"
    return greeting
