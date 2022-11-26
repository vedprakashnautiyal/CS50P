def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i=0
    if len(s)<2 or len(s)>6:
        return 0
    if s[0].isalpha()==False and s[1].isalpha()==False:
        return 0
    for c in s:
        if c.isalnum()==False:
            return 0
    for c in s:
        if c.isalpha() and s.index(c)>0:
            if s[s.index(c)-1].isdigit()==True:
                return 0
    for c in s:
        if c.isdigit():
            if c=='0' and s[s.index(c)-1].isalpha()==True:
                return 0
    return 

main()
