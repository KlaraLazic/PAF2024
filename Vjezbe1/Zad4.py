def pravac(x1,y1,x2,y2):
    k=(y2-y1)/(x2-x1)
    l=-k*x1+y1
    print("y={}x+{}".format(k,l))
pravac(2,3,-1,4)
