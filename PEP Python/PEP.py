'''
a = int(input("A: "))
b= int(input("B: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

a = float(input("Distance in Kilometers: "))
print("Distance in meters", a * 1000 , "m")
print("Distance in centimeters",a * 100000,"cm")

a = float(input("Size in Gigbytes: "))
print("Size in Mb", a * 1024)
print("Size in Kb", a * 1024 * 1024)


a = float(input("Enter the length: "))
b = float(input("Enter the base: "))
print("Area of Triangle", 0.5 * a * b)

r = float(input("Radius of circle: "))
print("Area of circle",3.14 * r * r)

s = float(input("Length of the side: "))
print("Area of square", s * s)



a = int(input("Enter the number: "))
if (a > 0):
    print("Positive Number")
elif (a < 0):
    print("Negative Number")
else:
    print("Zero")


a = int(input("Enter a number: "))
if( a % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

a = int(input("Enter a number: "))

if(a % 3== 0 & a % 5 ==0):
    print("Divisible by both 3 and 5.")
else:
    print("Not divisible.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

max = a if a > b else b
max = c if c > max else max
print(max)

a = input("Enter a character: ")
vowel = ["a","e","i","o","u"]
if(a in vowel):
    print("Vowel")
else:
    print("consonent")

a = int(input("Enter the number: "))
if( a % 7 ==0):
    print("Multiple of 7.")
else:
    print("Not a multiple of 7.")



a = int(input("Enter your attendance: "))
if(a > 75):
    print("Eligible for placement.")
elif(a < 75):
    print("Debarred.")
else:
    print("Talk to your teacher.")
a = int(input("Enter a 2 digit character: "))
count = 0
while(a > 0):
    a = a / 10
    count = count + 1
if(count == 2):
    print("Correct")
else:
    print("2 digit integer.")
res = eval("2 * 'str'")
print(res)    #vulnerable bacuse eval can run system commands in input (__import__("os").system("dir"))



a  = int(input("Enter the year: "))
if( (a % 4==0) & (a % 100 != 0)) | ((a % 400 == 0)):
    print("leap year")
else:
    print("not a leap year")


temp = int(input("Enter the temprature: "))

if(temp> 30):
    print("Hot.")
elif(temp < 15):
    print("Cold.")
else:
    print("Moderate.")

user = "admin"
password = "password"

u = input("Enter user id: ")
p = input("Enter user password: ")

if((u == user) & (p == password)):
    print("Succesfull login.")
else:
    print("Unauthoirzed.")




a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if((a+b > c) & (a+c > b) & (b+c > a)):
    print("Triangle is possible.")
else:
    print(f"Not possible to form a triangle with the given length of sides.")
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if(( a*a + b * b == c * c)|(a*a == b * b + c * c) | ( b * b == a * a + c * c)):
    print("Right angled triangle.")
else:
    print("Not a right angled triangle.")


a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if((a == b) & (b == c)):
    print("Equilateral")
elif((a != b)& (b!=c)& (c != a)):
    print("Scalean")
else:
    print("Isoceles")

a = 2
b = 2
print(id(a))
print(id(b))  #same id if the values of the variables are same
st = "string"
st1 = "string"
print(id(st))
print(id(st1))

import calculation
print(calculation.add(1,2,3,4))
import PEPdata
PEPdata.data(name="Akshat",age=22,sem="6th",reg="12321")

from mycustompackage import help

a = help.help_info()



def ad(a,b):
    """
    Docstring for ad
    
    :param a: Description
    :param b: Description
    """
    return (a+b)
y = help(ad(1,2))
print(y)

#pyfiglet



import pyfiglet

output = pyfiglet.figlet_format("Hello" , "slant")
Fonts = pyfiglet.FigletFont.getFonts()
print(output)
print(Fonts)



f = open("hello.txt")
d = f.read()
print(d)
f.close()

send_data = input("Enter the data you want int he file: ")

data = f.write("hello.txt","a")

f= open("hello.txt","r")
data = f.read(5)
print(data)
f.close()

with open("hello.txt","r") as html_file:
    for line in html_file:
        print(line)


import os
#print(dir(os))
f1 = input("Enter the file name with extention: ")
check = os.path.exists(f1)
print(check)

def detect_file_type(file_path):
    with open(file_path, "rb") as file:
        header = file.read(8)   # read first 8 bytes

    # Known magic numbers
    if header.startswith(b"%PDF"):
        return "PDF file"
    elif header.startswith(b"\x89PNG"):
        return "PNG image"
    elif header.startswith(b"\xFF\xD8\xFF"):
        return "JPEG image"
    elif header.startswith(b"PK\x03\x04"):
        return "ZIP archive"
    elif header.startswith(b"MZ"):
        return "Windows EXE file"
    else:
        return "Unknown file type"

file_path = input("Enter file path: ")
result = detect_file_type(file_path)
print("Detected:", result)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page."
@app.route("/about")
def about():
    return "About Page."
app.run()
# print(type(app))

# print()

# print(dir(app))

'''

class Employee:
    def __init__(self, name, salary, employee_number):
        self.name = name
        self.salary = salary
        self.employee_number = employee_number

    def add_bonus(self, bonus):
        self.salary += bonus

    def is_high_earner(self):
        return self.salary >= 100000

    def display(self):
        print(self.employee_number, self.name, self.salary, self.is_high_earner())

    
e1 = Employee("Hell",100001,25)
e1.name = "raj"
e1.add_bonus(20000)
e1.display()





















