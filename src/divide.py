
def divide(x, y):

    """Integer division as defined in Dasgupta et. al. Time-complexity: O(n²).

    Args
        x: integer
        y: integer greater than zero
    
    Returns
        q: quotient
        r: remainder    
    """

    if y == 0:
        print("Error: quotient must be greater than zero.")
        return

    if x == 0:
        return 0, 0

    q, r = divide(x//2, y)
    q, r = 2 * q, 2 * r

    if x%2 != 0:
        r+=1
    if r >= y:
        r-=y
        q+=1

    return q, r