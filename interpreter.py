inp=input ("Expression: ")
x,y,z=inp.split(" ")
if y=='+':
    print (f"{(float(x)+float(z)):0.1f}")
elif y=='-':
    print (f"{(float(x)-float(z)):0.1f}")
elif y=='*':
    print (f"{(float(x)*float(z)):0.1f}")
elif y=='/':
    print (f"{(float(x)/float(z)):0.1f}")