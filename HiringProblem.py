def hireAssistant(candidates):
    best=0
    numberOfHired=0
    for i in candidates:
        if i>best:
            best=i
            numberOfHired+=1
    return numberOfHired
def randomizedHireAssistant(candidates):
    candidateList=candidates
    randomizeInPlace(candidateList)
    return hireAssistant(candidateList)
def randomizeInPlace(array):
    n = len(array)
    for i in range(n):
        swap(array,i,randint(0,n-i-1)+i)
def swap(array,a,b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

from random import randint
candidateRanks=[2, 4, 6, 3, 9, 5, 7, 8]
print("Rank order in which candidates come in :",candidateRanks)
numberOfHiredCandidates =hireAssistant(candidateRanks)
print("Number of hired candidates :",numberOfHiredCandidates)
numberOfHiredCandidatesRandom = randomizedHireAssistant(candidateRanks)
print("After randomized algorithms, number of hire candidates :",numberOfHiredCandidatesRandom)