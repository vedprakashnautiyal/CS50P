dict={}
# value =1
while True:
    value =1
    try:
        item=input().upper().strip()
        if item in dict:
            dict[item]=value+1
        else:
            dict[item]=value
    except EOFError:
        for item in sorted(dict.items()):
            print(item[1],end=" ")
            print(item[0])
        break
