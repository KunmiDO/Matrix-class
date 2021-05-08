def get_row(matrix, row):
    return matrix[row]


def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == column_number:
                column.append(matrix[i][j])
    return column


def dot_product(vector_one, vector_two):
    total = 0
    for i in range(len(vector_one)):
        number = vector_one[i] * vector_two[i]
        total += number
    return total


def matrix_multiplication(matrixA, matrixB):
    ### TODO: store the number of rows in A and the number
    ###       of columns in B. This will be the size of the output
    ###       matrix
    ### HINT: The len function in Python will be helpful
    m_rows = len(matrixA)
    p_columns = len(matrixB[0])

    # empty list that will hold the product of AxB
    result = []

    for i in range(m_rows):
        row_result = []
        vector1 = get_row(matrixA, i)
        for j in range(p_columns):
            vector2 = get_column(matrixB, j)
            # number = dot_product(vector1, vector2)
            row_result.append(dot_product(vector1, vector2))
        result.append(row_result)
    print(result)
    return result


def transpose(matrix):
    matrix_transpose = []
    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)):
            number = matrix[i][j]
            new_row.append(number)
        matrix_transpose.append(new_row)
    print(matrix_transpose)
    return matrix_transpose


def matrix_transpose_multiplication(matrixA, matrixB):
    product = []

    ## TODO: Take the transpose of matrixB and store the result
    ##       in a new variable
    matrixT = transpose(matrixB)

    ## TODO: Use a nested for loop to iterate through the rows
    ## of matrix A and the rows of the tranpose of matrix B
    for i in range(len(matrixA)):
        new_row = []
        for j in range(len(matrixT)):
            number = dot_product(matrixA[i], matrixT[j])
            new_row.append(number)
        product.append(new_row)
    ## TODO: Calculate the dot product between each row of matrix A
    ##         with each row in the transpose of matrix B

    ## TODO: As you calculate the results inside your for loops,
    ##       store the results in the product variable

    ## TODO:
    print(product)
    return product


def identity_matrix(n):
    identity = []
    for i in range(n):
        new_row = []
        for j in range(n):
            if j == i:
                new_row.append(1)
            else:
                new_row.append(0)
        identity.append(new_row)
    # TODO: Write a nested for loop to iterate over the rows and
    # columns of the identity matrix. Remember that identity
    # matrices are square so they have the same number of rows
    # and columns

    # Make sure to assign 1 to the diagonal values and 0 everywhere
    # else
    print(identity)
    return identity

def inverse_matrix(matrix):
    '''
    Return the inverse of 1x1 or 2x2 matrices.

    Raises errors if the matrix is not square, is larger
    than a 2x2 matrix, or if it cannot be inverted due to
    what would be a division by zero.
    '''

    inverse = []

    # Check if not square
    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix must be square')

    # Check if matrix is larger than 2x2.
    if len(matrix) > 2:
        raise NotImplementedError('this functionality is not implemented')

    # Check if matrix is 1x1 or 2x2.
    # Depending on the matrix size, the formula for calculating
    # the inverse is different.
    if len(matrix) == 1:
        inverse.append([1 / matrix[0][0]])
    elif len(matrix) == 2:
        # If the matrix is 2x2, check that the matrix is invertible
        if matrix[0][0] * matrix[1][1] == matrix[0][1] * matrix[1][0]:
            raise ValueError('The matrix is not invertible.')
        else:
            # Calculate the inverse of the square 1x1 or 2x2 matrix.
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
            d = matrix[1][1]

            factor = 1 / (a * d - b * c)

            inverse = [[d, -b], [-c, a]]

            for i in range(len(inverse)):
                for j in range(len(inverse[0])):
                    inverse[i][j] = factor * inverse[i][j]

    return inverse