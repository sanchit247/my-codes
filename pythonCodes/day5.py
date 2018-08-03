p = float(input("enter the ammount\n"))
r = float(input("enter the rate of interest\n"))
t = float(input("enter the time period in years\n"))
ci = (1+r/100)**t
ci = ci-1
ci = p*ci
print("compound interest is :" ,ci)
