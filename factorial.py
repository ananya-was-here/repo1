def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)
inp=int(input("Enter any number"))
print("it's factorial is",fact(inp))

#or

inp=int(input("Enter any number"))
fact=1
while inp>=1:
  fact=fact*inp
  inp=inp-1
print(fact)
  
