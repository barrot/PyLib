#!/usr/bin/python

def changes(string1, string2):
	#initialize the matrix which will contain the penalty map
	matrix = [[0 for i in range(len(string1)+1)] for i in range(len(string2)+1)]
	
	#populate the matrix with the two strings
	for letter in string1:
		matrix[0][string1.index(letter)+1] = string1.index(letter)+1
	for letter in string2:
		matrix[string2.index(letter)+1][0] = string2.index(letter)+1
		
	#calculate the penalties and populate the rest of the matrix
	for j in range(0, len(string2)-1):
		for k in range(0, len(string1)-1):
			if(string2[j] == string1[k]):
				matrix[j+1][k+1] = min(matrix[j][k], matrix[j+1][k], matrix[j][k+1])
			else:
				matrix[j+1][k+1] = 2 + min(matrix[j][k], matrix[j+1][k], matrix[j][k+1])
	
	return matrix[len(string2)+1][len(string1)+1]
