import numpy as np

SAMPLE_SIZE = 31 # M
sample_data = [4,6,6,5,7,4,5,3,8,9,2,11,1,9,4,8,8,8,6,10,3,12,2,7,2,7,1,5,4,7,7,7,7,8,8,8,9,9,9,5]
sample_data2 = [5,6,5,6,5,7,4,8,3,9,2,10,1,9,2,8,6,6,6,10,1,10,1,6,1,6,1,3,5,7,9]
PREDICTOR_ORDER = 1

def main():

    M = SAMPLE_SIZE
    N = 2
    x = sample_data2

    # Finding autocorellation figures
    Rxx = [0.0]*(N+1)

    for k in range(0, N+1):
        sum = 0
        for i in range(0,M-k):
            sum += (x[i] * x[i+k])
        Rxx[k] = (1/(M-k))*sum
    
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
        print(format(coef[_],'.4f')+"*x[n-"+str(_+1)+"]", end='')
    print()
    
    # Predictor Gain output display:
    mu = FindDiff(x, coef)
    # print(mu)
    gain = PGain(x, mu, M)
    print(gain)

def FindDiff(sample, coef):
    size = len(sample) # Sample size
    order = len(coef) # Order of coding
    diff = [0.0] * size
    for i in range(0, size):
        for j in range(0, order):
            diff[i] += coef[j]*sample[i-(j+1) if i > j+1 else 0]

    print("[",end='')
    for alpha in diff:
        print(round(alpha, 4),end=' ')
    print("] with length of", len(diff))

    return diff

def PGain(pixel, diff, M=SAMPLE_SIZE):
    # pixel and diff must have length M
    sumPixSq = 0
    sumPixDiff = 0
    for _ in range(0,M):
        sumPixSq += (pixel[_]) ** 2
        sumPixDiff += (pixel[_] - diff[_]) ** 2
    return 10*(np.log10(sumPixSq/sumPixDiff))

if __name__ == "__main__":
    main()

