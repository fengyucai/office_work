def squareroot(n):
    root = n / 2    # initial guess
    for k in range(20):   #  iterations
        root = (1/2) * (root + n/root)
    return root

n = int(input('Please enter a integer (n > 0): ')) 
print('The square root of %d is %s' % (n, squareroot(n)))

