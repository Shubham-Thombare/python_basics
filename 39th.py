# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in
# variable scope = where variable is visible and accessible

# Local Scope
def func1():
    a = 1
    print(a)

def func2():   
    b = 2
    print(b)

func1()
func2()   

# Enclosed Scope
def func1():
    x = 1
    

    def func2():
        print(x)
    func2()

func1()
   
# Global Scope
def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()

# Built-in
from math import e

def func1():
    print(e)
    
func1()