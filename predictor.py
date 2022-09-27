import numpy as np

SAMPLE_SIZE = 31 # M
sample_data = [4,6,6,5,7,4,5,3,8,9,2,11,1,9,4,8,8,8,6,10,3,12,2,7,2,7,1,5,4,7,7,7,7,8,8,8,9,9,9,5]
sample_data2 = [5,6,5,6,5,7,4,8,3,9,2,10,1,9,2,8,6,6,6,10,1,10,1,6,1,6,1,3,5,7,9]
PREDICTOR_ORDER = 1

def main():
    # Autocorrelation figure
    M = SAMPLE_SIZE
    N = 2
    x = sample_data2
    Rxx = [0]*(N+1)

    for k in range(0, N+1):
        sum = 0
        for i in range(0,M-k):
            sum += (x[i] * x[i+k])
        Rxx[k] = (1/(M-k))*sum
    
    # I GIVE UP
    a = []
    b = []
    for k in range(1,N+1):
        b.append(Rxx[k])
        a.append([Rxx[abs(i-k)] for i in range(1, N+1)])
    
    coef = np.linalg.solve(a,b)

    # Predictor:
    print("Jadi, predictor berupa:")
    for _ in range(0,N):
        print(format(coef[_],'.4f')+"*x[n-"+str(_+1)+"]", end='')
    
    # Gain:
    print()

def PGain(pixel, diff, M=SAMPLE_SIZE):
    sumPixSq = 0
    sumPixDiff = 0
    for _ in range(0,M-1):
        sumPixSq += (pixel[_]) ** 2
        sumPixDiff += (pixel[_] - diff[_]) ** 2
    return 10*np.log10(sumPixSq/sumPixDiff)

if __name__ == "__main__":
    main()

