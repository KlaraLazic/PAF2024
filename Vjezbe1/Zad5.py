import matplotlib.pyplot as plt
x1=float(input("Upiši koordinatu x1: "))
y1=float(input("Upiši koordinatu y1: "))
x2=float(input("Upiši koordinatu x2: "))
y2=float(input("Upiši koordinatu y2: "))
def graf(a,b,c,d):
    xos=[a,c]
    yos=[b,d]
    plt.title("pravac")
    plt.plot(xos,yos)
    p=str(input("Ako želiš pdf reci DA, a ako želiš sliku na ekranu reci NE- "))
    if p=="DA":
        plt.savefig("pravac.pdf")
    elif p=="NE":
        plt.show()
graf(x1,y1,x2,y2)


