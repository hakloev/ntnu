from math import exp

def main():
    numbers = []
    with open('sample-data.txt')  as f:
        for l in f.readlines():
            numbers.append(float(l.strip()))
    alpha, mid = sorted(numbers), int(len(numbers)/2)
    n, p = alpha[:mid], alpha[mid:]
    means = [sum(n)/len(n), sum(p)/len(p)]
    print(means)
    
    for iteration in range(1000):
        if not iteration%5 and iteration <= 10: print(str(iteration)+"\t", means)
        expected = [[E(numbers, means, i, j) for i in range(len(numbers))] for j in range(len(means))]
        temp = [nextHypothesis(expected, numbers, j) for j in range(len(means))]
        if temp == means: break
        means = temp
    print(str(iteration)+"\t", means)
        
        
def E(numbers, means, i, j):
    return exp(-0.5*(numbers[i] - means[j])**2) / sum([exp(-0.5*(numbers[i] - means[n])**2) for n in range(len(means))])


def nextHypothesis(expected, numbers, j):
    return sum([expected[j][i]*numbers[i] for i in range(len(numbers))]) / sum(expected[j])

main()
