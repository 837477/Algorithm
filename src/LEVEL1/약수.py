def solution(n):
    divisors = []
    divisors_back = [] 

    for i in range(1, int(n**(1/2)) + 1): 
        if n % i == 0:            
            divisors.append(i)
            if i != n // i: 
                divisors_back.append(n//i)

    return sum(divisors + divisors_back[::-1])