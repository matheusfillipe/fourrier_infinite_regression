#precision
P=1e-6
def dif(X1,X2):
    x1=X1[0]
    x2=X2[0]
    y1=X1[1]
    y2=X2[1]
    return (y2-y1)/(x2-x1)

DIF=[]

def difTriag(X,Y):
    global DIF
    if not(len(X)==1 or len(Y)==1):
    
        dfunc=[]
        for x in X:
            dfunc.append([x])
        for i,y in enumerate(Y):
            dfunc[i].append(y)

        D=[]
        xx=[]
        for i,pt in enumerate(dfunc):
            if pt==dfunc[0]:
                continue        
            D.append(dif(dfunc[i-1],pt))
            xx.append(pt[0])
        t=True
        for d in D:
            if abs(d)>P:
                t=False
        if t:
            D=[0]
        DIF.append(D)
        if len(D)>=1:
            difTriag(xx,D)
        if len(D)!=len(X)-1:
            return
        return DIF
    else:
        return


def formula(X,Y):
    diff=difTriag(X,Y)
    DIF=[]
    print(diff)
    print(len(diff)-1)
