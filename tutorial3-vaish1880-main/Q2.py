# The following are daily returns for two stocks over a 10 day period. 
# Write a block of code to loop through the data and output in to a the list 'signs' (for each day) a value [1,0,-1]
# 1 if the return of both stocks is positive
# 0 if the return of both stocks have different signs
# -1 if the return of both stocks is negative

y=[-0.00382,  0.00067, -0.01656,  0.00572, -0.00301,  0.00316,
       -0.00449,  0.00428, -0.00131, -0.00744]
x=[-0.00311,  0.0149 , -0.00297, -0.01792, -0.01105, -0.00427,
        0.00511, -0.00924, -0.00204,  0.00094]

signs=[]
corr=0

# The correlation coefficient between x and y is given by:
# sum(x * y) / sqrt(sum(x^2) * sum(y^2))
# Loop through the data to calculate the sum of x * y, the sum of  𝑥^2  and the sum of  𝑦^2 .
# Set the value of the variable 'corr' equal to the correlation coefficient between the two series.
# Note that we can calculate square of a number x in python by  x**2 , and the square root of x by  x**0.5.


# Using the formula above, write a function to calculate the correlation between two lists of floats. 
# Include a docstring in your function. 
# The correlation between any series and itself is of course 1. Use this knowledge to test your function.

# The following is a list of 3 sub-lists, each of which represent the returns on three additional stocks.
# Append the returns on stocks x and y from above to this list to give a list of 5 sets of returns.

stock_returns =[
    [-0.00472, -0.00201,  0.00062,  0.00212,  0.00544, -0.00773,
        0.01668,  0.01039,  0.00603,  0.02005],
    [-0.00045,  0.00883, -0.01242, -0.01848,  0.01741,  0.0159 ,
        0.02529, -0.0011 , -0.00241,  0.00024],
    [-0.00257,  0.004  , -0.00309, -0.00531,  0.00262,  0.00421,
       -0.00156, -0.00985, -0.00776, -0.00361]]

# Write a block of code that calls your function above to calculate the correlation betweeen each pair of stocks. 
# Ouput this in a list of lists 'corr_mtx'. The 'outer' list should contain 5 inner lists of length 5, 
# representing the correlation between each stock and each of the other stocks (i.e. including itself) 
# (i.e. this is a correlation matrix, with each row of the matrix held in a seperate list).

corr_mtx = []

# (DIFFICULT!) Using while loops and the break statement, loop through the matrix in 'corr_mtx' to find 
# the first pairwise correlation coeffcient greater than .45, and report the numbers of the two correlated stocks 
# and their correlation coefficient (Ignore correlations between stock x and itself). 
# Set a the tuple 'my_pair' to hold these values i.e. my_pair = (stock #1, stock #2, correlation_coeff)
# If no such correlated pair is found set my_pair to be 'None'.


y = [-0.00382,  0.00067, -0.01656,  0.00572, -0.00301,  0.00316,
     -0.00449,  0.00428, -0.00131, -0.00744]
x = [-0.00311,  0.0149 , -0.00297, -0.01792, -0.01105, -0.00427,
      0.00511, -0.00924, -0.00204,  0.00094]

signs = []

for i in range(len(x)):
    if x[i] > 0 and y[i] > 0:
        signs.append(1)
    elif x[i] < 0 and y[i] < 0:
        signs.append(-1)
    else:
        signs.append(0)

def compute_correlation(a, b):
    sum_xy = sum(a[i] * b[i] for i in range(len(a)))
    sum_x2 = sum(a[i]**2 for i in range(len(a)))
    sum_y2 = sum(b[i]**2 for i in range(len(b)))
    return sum_xy / ((sum_x2 * sum_y2) ** 0.5)
corr = compute_correlation(x, y)

stock_returns = [
    [-0.00472, -0.00201,  0.00062,  0.00212,  0.00544, -0.00773,
        0.01668,  0.01039,  0.00603,  0.02005],
    [-0.00045,  0.00883, -0.01242, -0.01848,  0.01741,  0.0159 ,
        0.02529, -0.0011 , -0.00241,  0.00024],
    [-0.00257,  0.004  , -0.00309, -0.00531,  0.00262,  0.00421,
       -0.00156, -0.00985, -0.00776, -0.00361]
]

stock_returns.append(x)
stock_returns.append(y)

corr_mtx = []

for i in range(len(stock_returns)):
    row = []
    for j in range(len(stock_returns)):
        row.append(compute_correlation(stock_returns[i], stock_returns[j]))
    corr_mtx.append(row)
my_pair = None
i, j = 0, 0

while i < len(corr_mtx):
    j = i + 1  
    while j < len(corr_mtx[i]):
        if corr_mtx[i][j] > 0.45:
            my_pair = (i, j, corr_mtx[i][j])
            break  
        j += 1
    if my_pair:
        break 
    i += 1
    if not my_pair:
        my_pair = None
     

print("Signs list:", signs)
print("Correlation coefficient between x and y:", corr)
print("Correlation matrix:")
for row in corr_mtx:
    print(row)
print("First pairwise correlation > 0.45:", my_pair)




