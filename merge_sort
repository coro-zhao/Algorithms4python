#!/usr/bin/env python
# -*- coding: utf-8 -*-
#分治法
import random
import math

a = [6,3,1,5,4,2]

def merge(A,p,q,r):
	L = A[p:q+1]+[float("-inf")]
	R = A[q+1:r+1]+[float("-inf")]
	i = 0
	j = 0
	k = 0
	for k in xrange(p,r+1):
		if L[i] >= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

def merge_sort(A,p,r):
	if p < r:
		q = (p+r)/2
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge(A,p,q,r)
	return A
print merge_sort(a,0,5)

