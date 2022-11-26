while True:
    try:
        x,y=input("Fraction: ").split('/')
        a=int(x)
        b=int(y)
        f=a/b
        if(f<=1):
            break

    except  (ZeroDivisionError, ValueError):
        pass
p=f*100
if p<=1:
    print ("E")
elif p>=99:
    print('F')
else:
    print (f"{p:.0f}%")



