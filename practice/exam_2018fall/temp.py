# -*- encoding:utf-8 -*-

#lineList=[(a,b),...]
def lengthLine(lineList):
    rightSize=max([i[1] for i in lineList])
    leftSize=max([i[0] for i in lineList])
    longLine=[0]*(rightSize-leftSize)

    for line in lineList:
        for x in range(line[0],line[1]):
            longLine[x-leftSize]=1
    count=0
    for u in longLine:
        if u ==1:
            count+=1
    return count
    # cuLeft=lineList[0][0]
    # cuRight=lineList[0][1]
    # cuLen = cuRight-cuLeft
    # for line in lineList[1:]:
    #     if line[0]<cuLeft:
    #         if line[1]>cuLeft:
    #             if line[1]<cuRight:
    #                 cuLen+=cuLeft-line[0]
    #                 cuLeft=line[0]
    #             else:
    #                 cuLen=line[1]-line[0]
    #                 cuLeft=line[0]
    #                 cuRight=line[1]
    #         else:
    #
    #
    #     cuLen+=line[1]-line[0]

def spinMat(n):
    mat=[[0]*n]*n
    x=1
    for i in range(0,n/2):
        for j in range(i,n-i-1):
            mat[i][j]=x
            x+=1

        for j in range(i,n-i-1):
            mat[j][n-i-1]=x
            x+=1

        for j in range(n-i-1,i,-1):
            mat[n-i-1][j]=x
            x+=1

        for j in range(n-i-1,i,-1):
            mat[j][i]=x
            x+=1

    if n%2==1:
        mat[n/2][n/2] = x

    return mat

def printMat(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            print mat[i][j]

