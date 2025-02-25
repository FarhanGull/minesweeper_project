def minesweeper(A):
    rows=len(A)
    cols=len(A[0])
    A=[list(A[i]) for i in range (rows)]
    for i in range (rows):
        for j in range (cols):
            if not A[i][j]=="X":
                counter=0
                for k in range (i-1,i+2):
                    for l in range (j-1,j+2):
                        if (-1<k<rows and -1<l<cols) and A[k][l]=="X":
                            counter += 1
                A[i][j]=str(counter)
    A=["".join(A[i]) for i in range (rows)]  
    #code that coverts the test matrix into desired output
    return A

if __name__=="__main__":
    
    test = ["XOOXXXOO", 
            "OOOOXOXX", 
            "XXOXXOOO", 
            "OXOOOXXX", 
            "OOXXXXOX", 
            "XOXXXOXO", 
            "OOOXOXOX", 
            "XOXXOXOX"]

    """Desired Output is as under
    
    ["X11XXX32", 
     "3335X5XX", 
     "XX3XX554", 
     "3X556XXX", 
     "24XXXX6X", 
     "X3XXX5X3", 
     "245X6X5X", 
     "X2XX4X4X"]
    """

    print(minesweeper(test))

