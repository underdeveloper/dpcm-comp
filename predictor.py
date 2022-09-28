import numpy as np

SAMPLE1 = [4,6,6,5,7,4,5,3,8,9,2,11,1,9,4,8,8,8,6,10,3,12,2,7,2,7,1,5,4,7,7,7,7,8,8,8,9,9,9,5] # wanted
SAMPLE2 = [5,6,5,6,5,7,4,8,3,9,2,10,1,9,2,8,6,6,6,10,1,10,1,6,1,6,1,3,5,7,9] # example
PREDICTOR_ORDER = 3

def main():

    x = SAMPLE1
    M = len(x) # SAMPLE_SIZE
    N = PREDICTOR_ORDER

    # Finding autocorellation figures
    Rxx = [0.0]*(N+1)

    for k in range(0, N+1):
        sum = 0
        for i in range(0,M-k):
            sum += (x[i] * x[i+k])
        Rxx[k] = (1/(M-k))*sum
        # print("Rxx["+str(k)+"] = ", round(Rxx[k], 4))
    
    # Creating linear equations to solve for coefficients
    a = []
    b = []
    for k in range(1,N+1):
        b.append(Rxx[k])
        a.append([Rxx[abs(i-k)] for i in range(1, N+1)])
    
    coef = np.linalg.solve(a,b)

    # Predictor output display:
    print("Jadi, predictor berupa:")
    for _ in range(0,N):
        print(format(coef[_],'.4f')+"*x[n-"+str(_+1)+"]", end=' + ' if _ < N-1 else '')
    print()
    
    # Predictor Gain output display:
    mu = FindDiff(x, coef)
    # print(mu)
    gain = PGain(x, mu)
    print("Dengan predictor gain bernilai:", gain)

def FindDiff(sample, coef):
    size = len(sample) # Sample size
    order = len(coef) # Order of coding
    diff = [0.0] * size
    for i in range(0, size):
        for j in range(0, order):
            diff[i] += coef[j]*sample[i-(j+1)] if i >= j+1 else 0 # this is weird to me

    # print("[",end='')
    # for alpha in diff:
    #     print(round(alpha, 2),end=' ')
    # print("] with length of", len(diff))

    return diff

def PGain(pixel, diff):
    # pixel and diff must have the same length of M (too lazy to clean this, teehee)
    sumPixSq = 0
    sumPixDiff = 0
    M = len(pixel) # assume same size as diff
    for _ in range(0,M):
        sumPixSq += (pixel[_]) ** 2
        sumPixDiff += (pixel[_] - diff[_]) ** 2
    # print(sumPixDiff, sumPixSq)
    return 10*(np.log10(sumPixSq/sumPixDiff))

if __name__ == "__main__":
    main()