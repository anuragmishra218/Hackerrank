def Range(X,Y,Z):
    lst = []
    while X <= Y:
        X += Z
        lst.append(X)
    return lst

def GradientDescent(X,Y):
    res_m = 0
    rs_b = 0
    for m in Range(-1000,1000,0.01):
        mse_temp = 100

        for  b in Range(-1000, 1000, 0.1):
            z = 0
            for i in range(len(X)):
                y = (m*X[i]) +b
                z = z + (Y[i]-y)**2
        mse = 1/len(X) * z
        if mse_temp > mse:
            mse_temp = mse
            res_m = m
            res_b = b
        return m,b
xx = [[0,0], [1,1], [1.9,2], [3,3.2], [4,4.1], [5,5.11]]
X = []
Y = []
for i in xx:
    X.append(i[0])
    Y.append(i[1])


print(GradientDescent(X,Y))


