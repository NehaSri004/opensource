x, y = map(str, input().split())
if x==y:
    print("NULL")
elif x=='R':
    if(y=='P'):
        print("Charan")
    else:
        print("Vignesh")
elif x=='P':
    if(y=='S'):
        print("Charan")
    else:
        print("Vignesh")
elif x=='S':
    if(y=='R'):
        print("Charan")
    else:
        print("Vignesh")
