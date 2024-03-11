x1=float(input("Upiši koordinatu x1: "))
y1=float(input("Upiši koordinatu y1: "))
x2=float(input("Upiši koordinatu x2: "))
y2=float(input("Upiši koordinatu y2: "))
k=(y2-y1)/(x2-x1)
l=-k*x1+y1
print("y={}x+{}".format(k,l))