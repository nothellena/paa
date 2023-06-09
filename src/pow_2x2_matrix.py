def multiply_matrix_2x2(X, Y):
    
    a = X[0][0] * Y[0][0] + X[0][1] * Y[1][0]
    b = X[0][0] * Y[0][1] + X[0][1] * Y[1][1]
    c = X[1][0] * Y[0][0] + X[1][1] * Y[1][0]
    d = X[1][0] * Y[0][1] + X[1][1] * Y[1][1]

    return [[a,b],[c,d]]

def pow_2x2_matrix(matrix, n):

    if n == 0:
        return [[1,0],[0,1]]
    
    if n == 1:
        return matrix
    
    aux_power = pow_2x2_matrix(matrix, n//2)

    power_matrix = multiply_matrix_2x2(aux_power, aux_power)

    if n%2:
       power_matrix = multiply_matrix_2x2(power_matrix, matrix) 

    return power_matrix