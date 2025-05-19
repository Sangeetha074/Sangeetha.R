class Calc:
    #this as same as self-holds a current value
    #inputs:a,b
    #operate is a method
    #init is constructor/builtin function inside a class
    def __init__(this,a,b):
        this.a=a
        this.b=b
    def operate(this, operation):
        if operation=="add":
            return this.a + this.b
        elif operation=="sub":
            return this.a - this.b
        elif operation=="multiply":
            return this.a * this.b
        elif operation=="divide":
            if this.b!=0:
              return this.a / this.b
            else:
                return "error:division by zero"
        else:
                return "invalid operation"
a=float(input("enter value of a"))
b=float(input("enter value of b"))
operation=input("enter operation(add,sub,multiply,divide):")
call=Calc(a,b)
result=call.operate(operation)
print("Result:",result)

