def pow_by_squaring(x, n):

    # 2**T = n => T = log(n), where T is the number of computation steps.
    # That said pow_by_squaring is O(log(n))

    if n == 0:
        return 1
    
    if n == 1:
        return x
    
    k = n//2

    aux_power = pow_by_squaring(x, k)

    power = aux_power * aux_power

    if n%2:
        power *= x

    return power  

