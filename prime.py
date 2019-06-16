def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while pow(p, 2) <= n:
        if prime[p]:
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1

    return [a for a in range(2, n+1) if prime[a]]
