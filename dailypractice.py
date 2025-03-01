
text = "M2auygw77"
#chceking the stirng is alphanumeirc
print (text.isalnum())

print(text.isalpha())
print(text.isspace())
print(text.isupper())
print(text.islower())

# return a range of characters of a string
text1= "hello world!"
print(text1[1:6])

#convert a string into int.

string= "2"
convert = int(string)

print(type(convert))


class  parent():
    num1= 200
    def show(self):
         print("parent class function")

class child(parent):
    num= 100

    def show(self):
        print("child class function")

    def sum(self,a ,b):  #taking input from users
        sum= a+b
        print(sum)
    def sum2(self):
        sum2= self.num1+self.num
        print(sum2)

    # creating module and calling using that module
    def greeting(self, name):
        print("hello" + name)
     #find if string is palindrome

    def is_palindrome(self,s):
           if s == s[::-1]:
               print("string is palindrome")
           else:
               print("string is not palindrome")




obj= child()
obj.show()
obj.sum(10,30)
obj.sum2()
obj.greeting(" mausam")
print("********************************")
obj.is_palindrome("mausam")

#Membership Operators?
print("*******************************")
x= ["banana","apple"]
print("banana" in x)
print("apples" not in x)


# swapping 2 variables without using third variable

a= 10
b= 20

a,b= b,a
print(a,b)
# string is palindrome, create a function which has return type
print("***************************")
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("hannah"))















