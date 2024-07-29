#python prgm for qe.
import cmath as m
a=int(input("Enter a coefficient for a"))
b=int(input("Enter a coefficient for b"))
c=int(input("Enter a coefficient for c"))
d=b*b-4*a*c
if d>0:
    root1=-b+m.sqrt(d)/2*a
    root2=-b-m.sqr(d)/2*a
    print("Roots are real")
    print(f"Roots={root1} Root2{root2}")
elif d==0:
    root1=root2=-b/2*a
    print("Roots are equal")
    print(f"Root1={root1} Root2={root2}")
else:
    root1=-b/2*a+m.sqrt(d)/2*a 
    root2=-b/2*a-m.sqrt(d)/2*a 
    print("Roots are imaginary")
    print(f"Root1={root1} Root2={root2}")



