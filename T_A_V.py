def hello():
    print("Hello")
hello()


def hello(name):
    print("hello" , name)
hello("barbod")

def add(a , b):
    print(a * b)
add(5 , 3)


def add(a , b):
    return a + b
result = add(5 , 3)
print(result)

def hello(name='barbod'):
    print('hello' , name)
hello()
hello('mahbod')

def var_a(a , b):
    return a + b , a - b
c , d = var_a(10 , 3)
print(c)
print(d)

def add(*numbers): 
    print(sum(numbers))
add(1, 2, 3)
add(10, 20, 30, 40)

def var_b(**data):
    print(data)
var_b(name = 'barbod', age = 13)

def say_hello():
    print('Hello')
def start():
    say_hello()
    print('Welcome')
start()

def var_c(n):
    if n == 0:
        return
    print(n)
    var_c(n - 1)
var_c(5)
