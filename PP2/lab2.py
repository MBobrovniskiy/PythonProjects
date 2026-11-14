a=0.0
b=1.0

def s(x, eps):
    term=x/2
    total=0.0
    n=0
    x2=x*x

    while term>=eps or term<=-eps:
        total+=term
        n+=1
        term*=-(n*n*x2)/((2*n+1)*(2*n+2))
    total+=eps
    return total
def _domaincheck(x):
    return x>=a, x<=b
def _main():
    print("Created by Matvii Bobrovnitskyi K-13")
    print("Task 117. Calculate S(x) ")
    print(f"Domain: [{a},{b}]")
    valid=true
    stage=1
    try:
        x=float(input("Enter x(from 0 to 1): "))
        stage = 2
        if _domaincheck(x) == False:
            print("***** error")
            print("x is not in domain")
            valid = False
        if valid==True:
            stage=3
            eps=float(input("Enter eps(>0): "))
            stage=4
            if eps<0 or eps>=float("inf"):
                print("eps not in domain")
                valid = False
    except KeyboardInterrupt:
        print("\nprogram aborted")
        valid = False
    except ValueError:
        print("\n***** error")
        if stage==1:
            print("cant convert x")
        else:
            print("cant convert eps")
        valid = False
    except EOFError:
        print("\n***** error")
        print("input was interrupted")
        valid = False
    if valid==True:
        print("***** do calculations ... ", end=" ")
        result=s(x, eps)
        print("done")
        print(f"for x = {x:.7E}")
        print(f"for eps = {eps:.8E}")
        print(f"result = {result:.8f}")
    _main()

