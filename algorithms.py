import random
import math
import copy
import sys
sys.setrecursionlimit(100000)

def getMedians(choices):
	blocks = [choices[i:i+5] for i in range(0, len(choices), 5)]
	sortedBlocks = [sorted(block) for block in blocks]
	medians = [block[len(block)//2] for block in sortedBlocks]
	return medians

def chosePivot(choices, k):
	medians = getMedians(choices)
	# median of medians
	m = medians[len(medians)//2]
	return m

def partition(choices, m):
	start = 0
	end = len(choices) - 1
	i = 0

	while i <= end:
		if choices[i] == m:
			i += 1
		elif choices[i] < m:
			choices[start], choices[i] = choices[i], choices[start]
			start += 1
			i += 1
		else:
			choices[end], choices[i] = choices[i], choices[end]
			end -= 1

	return start

def medianOfMedians(choices, k):
	m = chosePivot(choices, k)
	start = partition(choices, m)

	if start == (k):
		return m
	elif start > (k):
		return medianOfMedians(choices[0:start], k)
	else:
		return medianOfMedians(choices[start + 1:len(choices)], k - start - 1)

# vetor = [2,5,9,19,24,54,5,87,9,10,44,32,18,13,2,4,23,26,16,19,25,39,47,56,71]
vetor = [(random.random()*100*random.random()*100*random.random()*100) for i in range(1000000)]
print('Mediana Real: ', sorted(vetor)[len(vetor)//2])
mm = medianOfMedians(vetor, len(vetor)//2)
print('Mediana Oráculo: ', mm)




def euclidianDistance(A, B):
    cat1 = ((B[1]-A[1])**2)
    cat2 = ((B[0]-A[0])**2)
    return math.sqrt(cat1 + cat2)

def bruteForce(points):
    minDistance = math.inf
    pA = None
    pB = None

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = euclidianDistance(points[i], points[j])
            if distance < minDistance:
                minDistance = distance
                pA = points[i]
                pB = points[j]
    return pA, pB, minDistance


def rec(xsorted, ysorted):
    n = len(xsorted)
    if n <= 3:
        return bruteForce(xsorted)
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
                d = euclidianDistance(in_band[i], in_band[j])
                if d < delta:
                    print(in_band[i], in_band[j])
                    (p1, p2, delta) = (in_band[i], in_band[j], d)
        return p1, p2, delta


def closest(points):
    x = sorted(points, key=lambda point: point[0])
    y = sorted(points, key=lambda point: point[1])
    return rec(x, y)
  
def calculateInversions(choices, map):
    numbers = []

    for choice in choices:
        numbers.append(map[choice])
        
    return _calculateInversions(numbers, copy.copy(numbers), 0, len(numbers)-1)

def _calculateInversions(choices, aux, start, end):
    inversions_counter = 0
  
    if start < end:
        mid = (start + end)//2

        #rA
        inversions_counter += _calculateInversions(choices, aux, start, mid)
        #rB
        inversions_counter += _calculateInversions(choices, aux, mid + 1, end)
        #r
        inversions_counter += merge(choices, aux, start, mid, end)

    return inversions_counter
  
def merge(choices, aux, start, mid, end):
  
    i = start     
    j = mid + 1 
    k = start     
    inversions_counter = 0
  
    while i <= mid and j <= end:
        if choices[i] <= choices[j]:
            aux.append(choices[i])
            i += 1
        else:
            aux.append(choices[j])
            inversions_counter += (mid-i + 1)
            j += 1
        k += 1
  
    while i <= mid:
        aux.append(choices[i])
        i += 1
    while j <= end:
        aux.append(choices[j])
        j += 1
    k += 1
  
    choices = copy.copy(aux)
          
    return inversions_counter
  
