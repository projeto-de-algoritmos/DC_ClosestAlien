import random
import math
import copy
import sys
sys.setrecursionlimit(100000)

def getMedians(choicesay):
	blocks = [choicesay[i:i+5] for i in range(0, len(choicesay), 5)]
	sortedBlocks = [sorted(block) for block in blocks]
	medians = [block[len(block)//2] for block in sortedBlocks]
	return medians

def chosePivot(choicesay, k):
	medians = getMedians(choicesay)
	# median of medians
	m = medians[len(medians)//2]
	return m

def partition(choicesay, m):
	start = 0
	end = len(choicesay) - 1
	i = 0

	while i <= end:
		if choicesay[i] == m:
			i += 1
		elif choicesay[i] < m:
			choicesay[start], choicesay[i] = choicesay[i], choicesay[start]
			start += 1
			i += 1
		else:
			choicesay[end], choicesay[i] = choicesay[i], choicesay[end]
			end -= 1

	return start

def medianOfMedians(choicesay, k):
	m = chosePivot(choicesay, k)
	start = partition(choicesay, m)

	if start == (k):
		return m
	elif start > (k):
		return medianOfMedians(choicesay[0:start], k)
	else:
		return medianOfMedians(choicesay[start + 1:len(choicesay)], k - start - 1)

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
  

def inversions(choices, aux, start, end):
    inversions_counter = 0
  
    if start < end:
        mid = (start + end)//2

        #rA
        inversions_counter += inversions(choices, aux, start, mid)
        #rB
        inversions_counter += inversions(choices, aux, mid + 1, end)
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
  
instrumentos = [
    'baixo'
    , 'bateria'
    , 'violão'
    , 'guitarra'
    , 'violino'
]
choices = []
for i in range(5):
    print(f'O quanto você gosta de {instrumentos[i]}?')
    choices.append(input())

rock = [3,2,4,1,5]
ri = inversions(rock, copy.copy(rock), 0, len(rock)-1)
bossanova = [3,5,1,4,2]
bi = inversions(bossanova, copy.copy(bossanova), 0, len(bossanova)-1)
jazz = [2,4,5,3,1]
ji = inversions(jazz, copy.copy(jazz), 0, len(jazz)-1)

vi = sorted([(ri, 'rock'),(bi, 'bossa nova'),(ji, 'jazz')])
print(vi)
result = inversions(choices, copy.copy(choices), 0, len(choices)-1)

print("Number of inversions are", result)
