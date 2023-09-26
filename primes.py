def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n //= 2
    
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
    
    if n > 2:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    
    return factors

def cumulative_prime_factors_dictionary(start, end):
    cumulative_factors = {}
    for num in range(int(start), int(end)+1):
        factors = prime_factors(num)
        for factor, frequency in factors.items():
            if factor in cumulative_factors:
                cumulative_factors[factor] += frequency
            else:
                cumulative_factors[factor] = frequency
    
    return cumulative_factors

#start = int(input())
#end = int(input())
#result = cumulative_prime_factors_dictionary(start, end)

j=int(input())
for z in range(j):
    o = input()
    parts=o.split(" ")
    p=parts[0]
    q=parts[1]
    result1=cumulative_prime_factors_dictionary(1,q)
    result2=cumulative_prime_factors_dictionary(1,int(p)-1)
    unique1=set(result1.keys())
    unique2=set(result2.keys())
    print(len(unique1) - len(unique2))

    

    


                


