import random
import math
import copy
import sys
sys.setrecursionlimit(100000)

def getMedians(array):
	blocks = [array[i:i+5] for i in range(0, len(array), 5)]
	sortedBlocks = [sorted(block) for block in blocks]
	medians = [block[len(block)//2] for block in sortedBlocks]
	return medians

def chosePivot(array, k):
	medians = getMedians(array)
	# median of medians
	m = medians[len(medians)//2]
	return m

def partition(array, m):
	left = 0
	right = len(array) - 1
	i = 0

	while i <= right:
		if array[i] == m:
			i += 1
		elif array[i] < m:
			array[left], array[i] = array[i], array[left]
			left += 1
			i += 1
		else:
			array[right], array[i] = array[i], array[right]
			right -= 1

	return left

def medianOfMedians(array, k):
	m = chosePivot(array, k)
	left = partition(array, m)

	if left == (k):
		return m
	elif left > (k):
		return medianOfMedians(array[0:left], k)
	else:
		return medianOfMedians(array[left + 1:len(array)], k - left - 1)

# vetor = [2,5,9,19,24,54,5,87,9,10,44,32,18,13,2,4,23,26,16,19,25,39,47,56,71]
vetor = [(random.random()*100*random.random()*100*random.random()*100) for i in range(1000000)]
print('Mediana Real: ', sorted(vetor)[len(vetor)//2])
mm = medianOfMedians(vetor, len(vetor)//2)
print('Mediana Oráculo: ', mm)




def dist(p1, p2):
    return math.sqrt(((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2))

def closest_brute_force(points):
    min_dist = float("inf")
    p1 = None
    p2 = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                p1 = points[i]
                p2 = points[j]
    return p1, p2, min_dist


def rec(xsorted, ysorted):
    n = len(xsorted)
    if n <= 3:
        return closest_brute_force(xsorted)
    else:
        midpoint = xsorted[n//2]
        xsorted_left = xsorted[:n//2]
        xsorted_right = xsorted[n//2:]
        ysorted_left = []
        ysorted_right = []
        for point in ysorted:
            ysorted_left.append(point) if (point[0] <= midpoint[0]) else ysorted_right.append(point)
        (p1_left, p2_left, delta_left) = rec(xsorted_left, ysorted_left)
        (p1_right, p2_right, delta_right) = rec(xsorted_right, ysorted_right)
        (p1, p2, delta) = (p1_left, p2_left, delta_left) if (delta_left < delta_right) else (p1_right, p2_right, delta_right)
        in_band = [point for point in ysorted if midpoint[0]-delta < point[0] < midpoint[0]+delta]
        for i in range(len(in_band)):
            for j in range(i+1, min(i+7, len(in_band))):
                d = dist(in_band[i], in_band[j])
                if d < delta:
                    print(in_band[i], in_band[j])
                    (p1, p2, delta) = (in_band[i], in_band[j], d)
        return p1, p2, delta


def closest(points):
    xsorted = sorted(points, key=lambda point: point[0])
    ysorted = sorted(points, key=lambda point: point[1])
    return rec(xsorted, ysorted)
  

