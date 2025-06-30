
import numpy as np
import pandas as pd

#Функция с вызовом numpy
def my_numpy():
    arr=np.array([1,2,3,4,5])
    print (arr)
    print(type(arr))

#Функция с вызовом pandas
def my_pandas():
    a=[1,2,3,4,5]
    myvar = pd.Series(a)
    print (myvar)
    print ("")
    print(myvar[1])


#точка входа в программу

def main():
    my_numpy()
    print("")
    my_pandas()
    return 0

if __name__ == '__main__':
	main()

