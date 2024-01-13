#name:Jack Wyeth
def fibo(n):
        if n<=1:
            return n
        else:    
            return fibo(n-1) + fibo(n-2) 

def fibo_calls(n,calls):  
    #it exists in our dict   
    if n in calls:
        calls[n] += 1
    #it does not so we start its existence
    else:
        calls[n] = 1
    #end of the line for the fibo calculations
    if n <= 1:
        return n
    else:
        return fibo_calls(n - 1, calls) + fibo_calls(n - 2, calls)
            
def naive_matrix_mult(S, P):
    a = len(S)
    b = len(S[0])
    g = len(P)
    h = len(P[0])
    #intialize Q
    Q = [[0 for x in range(h)] for y in range(a)]
    for m in range(a):
        for r in range(h):
            Q[m][r] = 0
            for k in range(g):
                Q[m][r] += S[m][k] * P[k][r]
                
    return Q

def main(): 
    #method 1
    fibo_OG=int(input())
    fibo_final=fibo(fibo_OG)
    print(fibo_final)
    #make a dictionary that tracks how many times the value "n" is called
    calls={}
    fibo_calls(fibo_OG,calls)
    #use sorted so it appears in descending order going top down
    #.items lists the dict in a format that makes it for loop enabled
    for key, value in sorted(calls.items()):
     print(f"fibo({key}) : {value}")

#Method 2
    S = [[1, 1],
         [1, 0]]
    P = [[1, 0], 
         [0, 1]]

    
    M = 0
    for i in range(fibo_OG-1):
        P = naive_matrix_mult(P, S)
        M +=8  # every iteration we do 8 
      
    print(f"{M}")

if __name__ == "__main__":
    main() 
