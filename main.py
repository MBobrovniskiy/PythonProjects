import math

def _domaincheck(x):
    """Перевірка чи число входить до області визначення"""
    return x > 4 and x !=7
def f(x):
        return(math.sin(16/69)+24*math.pi-59*math.e*5/((x+6)*(x-7))+3*math.atan(x-15)+math.log(x-4,7))

try:
    print("Author Matvii Bobrovnitskyi K-13.")
    print("Task 117. Program calculates the value of the expression by given х.")
    x=float(input("Enter a number(x>4, x!=7): "))
except ValueError:
    print("wrong input")
else:
    print("\n***** do calculations ...", end=" ")
    if _domaincheck(x):
        result = f(x)
        print("done")
        print(f"for x = {x:.5f}")
        print(f"result = {result:.7f}")
    else:
        print("done")
        print(f"for x = {x:.5f}")
        print("undefined")