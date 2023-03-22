#functions
def fibonacchi(nn):
    if nn ==0:
        return 0
    elif nn == 1:
        return 1
    else:
        return fibonacchi(nn-1) + fibonacchi(nn-2)

#0
print("Fibonacci sorozat elemei")

#1
a = float(input("a = ").replace(',' , '.'))
b = float(input("b = ").replace(',' , '.'))

#2
if a>b:
    a, b = b, a

fibJo = []
n=0
while True:
    elem = fibonacchi(n)
    if elem>=a and elem<=b:
        fibJo.append(elem)
    if elem>b:
        break
    n+=1

    #3
tempStr = []
for item in fibJo:
 tempStr.append( str(item) )

kiiras = "; ".join(tempStr) 
print(kiiras)