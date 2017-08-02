def stars_table(n=4,m=8):
    for i in range(1,n+1):
        for j in range(1,m+1):
            q=i%2
            w=j%2
            if q and w:
                print("*", end="")
            if q and not w :
                print(" ", end="")
            if not q and w:
                print(" ", end="")
            if not q and not w:
                print("*", end="")
        print()

stars_table(10,100)

