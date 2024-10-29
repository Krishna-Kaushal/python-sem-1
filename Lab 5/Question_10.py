n=int(input("Enter the numerator: "))
d=int(input("Enter the denominator: "))
print(f"{n}/{d} is simplified as ",end="")
def simplify_frac(n, d):
    i = 2
    while i < min(n, d) + 1:
        if n % i == 0 and d % i == 0:
            n = n // i
            d = d // i
        else:
            i += 1  
    print(f"{n}/{d}")

simplify_frac(n,d)