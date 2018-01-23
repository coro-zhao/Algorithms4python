#!/usr/bin/env python
# -*- coding: utf-8 -*-
#冒泡排序
import random

def randomlist():
	random_list = []
	for i in range(10):
		random_list.append(random.randint(1, 50))
	return random_list

a = [5,2,4,6,1,3]

def insertion_sort_up(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		while i >=0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key
	return A

def insertion_sort_down(a):
	for j in range(1,len(a)):
		key = a[j]
		i = j-1
		while i >= 0 and a[i] < key:
			a[i+1] = a[i]
			i -= 1
		a[i+1] = key
	return a

print insertion_sort_up(randomlist())
print insertion_sort_down(randomlist())
