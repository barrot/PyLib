#!/usr/bin/python

def changes(string1, string2):
	#initialize the matrix which will contain the penalty map
	matrix = [[0 for i in range(len(string1)+1)] for i in range(len(string2)+1)]
	
	#populate the matrix with the two strings
	index = 1
	for letter in string1:
		matrix[0][index] = index
		index = index + 1
		
	index = 1
	for letter in string2:
		matrix[index][0] = index
		index = index + 1
		
	#calculate the penalties and populate the rest of the matrix
	for j in range(0, len(string2)):
		for k in range(0, len(string1)):
			if(string2[j] == string1[k]):
				matrix[j+1][k+1] = min(matrix[j][k], matrix[j+1][k], matrix[j][k+1])
			else:
				matrix[j+1][k+1] = 1 + min(matrix[j][k], matrix[j+1][k], matrix[j][k+1])
				
	for row in matrix:
		print(row)
	
	return matrix[len(string2)][len(string1)]
