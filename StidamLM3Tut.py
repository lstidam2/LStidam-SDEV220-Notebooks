#functional
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def do_math(action, x, y):
    return action(x,y)

print(do_math(subtract, 7,5))
print(do_math(divide, 12, 3))




#oop
class go_calc:
    def __init__(self, val1, val2):
        self.val1= val1
        self.val2=val2

    def add(self):
        return self.val1+self.val2

    def subtract(self):
        return self.val1-self.val2

    def multiply(self):
        return self.val1 * self.val2

    def divide(self):
        return self.val1 / self.val2

subex=go_calc(7,5)
print(subex.subtract())
divideex=go_calc(12,3)
print(divideex.divide())
