import read_matix as rm
import numpy as np

#declare constant
MAX_ELEMENT_BIG_MATRIX = 46

def process_big_matrix():
    a = np.array(bigmatrix[0,:])
    b = np.array([1])
    c = int(np.nonzero(np.in1d(a, b))[0][0])
    d = bigmatrix[0][c]
    r = 0
    while bigmatrix[r][c] < MAX_ELEMENT_BIG_MATRIX :
        if bigmatrix[r+1][c] == d+1:
            r=r+1
            #moving forward
        if bigmatrix[r][c+1] == d+1:
            c=c+1
            #turn right
        if c-1 >= 0:
            if bigmatrix[r][c-1] == d+1:
                c=c-1
                #turn left
        if r-1>=0:
            if bigmatrix[r-1][c] == d+1:
                r=r-1
                #moving backward 
        d=d+1
        print(bigmatrix[r][c])
    return 1

def process_small_matrix():
    print("test")




if __name__ == '__main__':
    bigmatrix=rm.read_big_matrix()
    smallmatrix=rm.read_small_matrix()
    c = process_big_matrix()
    print(c)
    ## print(smallmatrix)