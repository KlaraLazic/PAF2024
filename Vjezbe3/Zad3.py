from math import sqrt
from statistics import stdev
from statistics import mean

TOCKE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def AritmetickaSredina(tocke):
    n = len(tocke)
    x = 0
    for tocka in tocke:
        x += tocka

    return x / n

def StandardnaDevijacija(tocke):
    n = len(tocke)
    x = 0
    mean = AritmetickaSredina(tocke)
    for tocka in tocke: 
        x += ( tocka - mean ) ** 2

    return sqrt( x / ( n*(n - 1) ) )


# A)
print (AritmetickaSredina(TOCKE))
print (StandardnaDevijacija(TOCKE))

# B)
print (mean(TOCKE))
print (stdev(TOCKE))