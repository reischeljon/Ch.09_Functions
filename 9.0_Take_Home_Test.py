'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________

Remember, for 1-7 record your prediction AND actual. It's not a problem if you are wrong.
It IS a problem if you don't record your prediction. Make sure you understand HOW the code works.
'''

'''
1.)
def f1(x):
    print(x)
y = 3
f1(y)
'''




'''
2.)
def f2(x):
    x = x + 1
    print(x)
y = 3
f2(y)
print(y)
'''




'''
3.)
def f3(x):
    x = x + 1
    print(x)
x = 3
f3(x)
print(x)
'''




'''
4.)
def f4(x):
    z = x + 1
    print(z)
x = 3
f4(x)
print(z)
'''




'''
5.)
def foo(x):
    x = x + 1
    print("x=", x)
 
x = 10
print("x=", x)
foo(x)
print("x=", x)
'''




'''
6.)
def f():
    print("f start")
    g()
    h()
    print("f end")
 
def g():
    print("g start")
    h()
    print("g end")
 
def h():
    print("h")
 
f()
'''




'''
7.)
def jedi():
    x = 3
    print("The last Jedi!")
 
x = 10
print("x=", x)
jedi()
print("x=", x)
'''


'''
This next section involves finding the mistakes in the code. 
'''



'''
8.) Correct the following code: (Don't let it print out the word ``None'')

def sum(a, b, c):
    print(a + b + c)
 
print(sum(10, 11, 12))
'''




'''
9.) Correct the following code: (x should increase by one, but it doesn't.)

def increase(x):
    return x + 1
 
x = 10
print("X is", x, " I will now increase x." )
increase(x)
print("X is now", x)
'''                          
 
  
  
  
  
'''
10.) Correct the following code:

def print_hello:
    print("Hello")
 
print_hello()
'''





'''
11.) Correct the following code:

def count_to_ten():
    for i in range[10]:
        print(i)
 
count_to_ten()
'''






'''
12.) Correct the following code:

def sum_list(list):
    for i in list:
        sum = i
        return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))
'''






'''
13.) Correct the following code: (This almost reverses the string. What is wrong?)

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * -1]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))
'''






'''
14.) Correct the following code: (if one of the options is not entered it should print the statements)

def get_user_choice():
    while True:
        command = input("Command: ")
        if command = f or command = m or command = s or command = d or command = q:
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)

'''
