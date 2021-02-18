'''This program is used to calculate Information Gain given a dataset using the Gini Impurity for a Decision Tree Classification Model. 
Input format:
- First line: list of the target values in the initial dataset
- Second line: list of the target values of the left split
- Third line: list of the target values of the right split
'''

S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ginilist = []

def gini(list):
	i = 0
	for number in list:
		if number == 1:
			i+=1
	p = i/len(list)
	gini = 2 * p * (1-p)
	return gini

def info_gain(gini_root, gini_left, gini_right, list_root, list_left, list_right):
	info_gain = gini_root-(gini_left*(len(list_left)/len(list_root))) - (gini_right*(len(list_right)/len(list_root)))
	return info_gain
	
gini_root = gini(S)
gini_left = gini(A)
gini_right = gini(B)

information_gain = info_gain(gini_root, gini_left, gini_right, S, A, B)
	
print('Information gain: ', information_gain)
		
