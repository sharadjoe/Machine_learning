import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    n=np.size(x)
    mean_x=np.mean(x)
    mean_y=np.mean(y)
    cross_derivation=np.sum(y*x-n*mean_x*mean_y)
    squared_derivation=np.sum(x**2-n*(mean_x**2))
    slope=cross_derivation/squared_derivation
    intercept=mean_y-slope*mean_x

    return(intercept,slope)


def plotting(x,y,b):
    plt.scatter(x,y,color="m",marker="o",s=30)
    y_predicted=b[0]+b[1]*x
    plt.plot(x, y_predicted, color = "g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
b=estimate_coef(x,y)
print(b[0])
print(b[1])

plotting(x,y,b)


 

