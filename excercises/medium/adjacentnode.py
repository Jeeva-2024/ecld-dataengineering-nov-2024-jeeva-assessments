def adajecntnode(n1,n2):
    matrix = [
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
    return matrix[n1][n2]==1
print (adajecntnode(0,2))
