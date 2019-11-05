mat=[[ 1, 1, 2 ],  
     [ 1, 1, 1 ],  
     [ 2, 1, 1 ]]


#      {1, 1, 2},
# {1, 1, 1},
# {2, 1, 1}
row,col=len(mat),len(mat[0])
size=row*col

track=[[0 for i in range(col)] for j in range(row)]
# print(track)
cnts=[]
def find_path(i,j,cnt):
  # print(i,j)
  if(i==row-1 and j==col-1):
    cnts.append(cnt)
  val=mat[i][j]
  if(val<=size):
    # print('sss',val)
    for vals in range(0,val+1):
      a=i+vals
      b=j+abs(val-vals)
      # print(val,a,b)
      if (a>=row or b>=col or track[a][b]):
        continue
  
      # if(track[a][b]):
      #   continue
      track[a][b]=1
      temp=cnt+1
      find_path(a,b,temp)

find_path(0,0,0)
print(min(cnts))


  # return 1E+5