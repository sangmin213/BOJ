def gcd(a, b): # a > b
    if b==0:
        return a
    return gcd(b, a%b)

def find_val(M, N, gcd_val): # M > N
    for i in range(N//gcd_val+1):
        if (M*i+x-y)%N == 0:
            return M*i+x
    return -1

def main():
    N = int(input())
    mylist = []
    
    for n in range(N):
        mylist.append(map(int,input().split()))
    for M, N, x, y in mylist:
        result = -1
        if M>N: result = find_val(M, N, gcd(M,N))
        else:   result = find_val(N, M, gcd(N,M))

        print(result)

    return

if __name__ == '__main__':
    main()