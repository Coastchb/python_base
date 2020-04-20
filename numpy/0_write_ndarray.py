import numpy as np
import os

def write_ny_1array(list,fd):
	fd.writelines(' '.join(map(str,list)))
	fd.writelines('\n')
   
def write_ny_2array(matrix, fd):
	for line in matrix:
		print("line:")
		print(line)
		write_ny_1array(line,fd)

def write_ny_3array(tensor,fd):
	for matrix in tensor:
		print("matrix:")
		print(matrix)
		write_ny_2array(matrix,fd)


def main():
	a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
	with open("data/3array.txt","w") as fd:
		write_ny_3array(a, fd)
main()
    
