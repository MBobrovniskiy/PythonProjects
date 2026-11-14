import math

def f(x):
    """Return the value of the variant expression for x."""
    return(math.sin(16/69)
            +24*math.pi-59*math.e*5
            /((x+6)*(x-7))+3*math.atan(x-15)
            +math.log(x-4,7))


def _domaincheck(x):
    """Tell whether x belongs to the domain of f."""
    return x > 4 and x !=7 and math.isfinite(x)


def _main():
    """Read x, evaluate the expression and report the result."""
    print("Author Matvii Bobrovnitskyi K-13.")
    print("Task 117. Program calculates the value of the expression by given х.")
    try:
        x=float(input("Enter a number(x>4, x!=7): "))
    except ValueError:
        print("\nwrong input")
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
            print("result = undefined")


_main()