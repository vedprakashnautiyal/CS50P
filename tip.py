def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars) * float(percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d= d.replace("$","")
    d=float(d)
    return f"{d:0.1f}"


def percent_to_float(p):
    p= p.replace("%","")
    p=float(p)
    return p/100




main()