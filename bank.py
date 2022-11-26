x=input("Greetings: ").lower().strip()
if x.startswith("hello"):
    print("$0")
elif x.startswith("h",0,2):
    print("$20")
else:
    print("$100")