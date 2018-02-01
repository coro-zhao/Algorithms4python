#!/usr/bin/env python
# -*- coding: utf-8 -*-
#冒泡法
import random

def randomlist():
	random_list = []
	for i in range(10):
		random_list.append(random.randint(1, 50))
	return random_list

x = randomlist()

def bubble_sort(a):
	i = 0
	j = 0
	for j in xrange(0,len(a)-j):
		for i in xrange(0,len(a)-j-1):
			if a[i] > a[i+1]:
				a[i],a[i+1] = a[i+1],a[i]
	return a
print x
print bubble_sort(x)
