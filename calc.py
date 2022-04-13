def adding(a,b):
       return a+b
def subtract(a,b):
       return a-b
def multiply(a,b):
       return a *b
def divide(a,b):
       return a/b    
print("select an operator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4.Divide")
choice = input("enter operater to use")
A = int(input("enter first number"))
B = int(input("enter sec number"))
if choice =="1" :
         print(A,"+",B,"=",adding(A,B))
elif choice == "2" :
         print(A,"-",B,"=",subtract(A,B))
elif choice =="3" :
         print(A,"*",B,"=",multiply(A,B))
elif choice =="4" :
         print(A,"/",B,"=",divide(A,B))
else:
         print("Invalid input")