# Defining the Function
def simple_intrest(p, n, r):
    """
    This Function takes following inputs
    p = principal in INR
    n = no of years
    r = rate of intrest in %p.a.
    Output = Intrest and Amount
    """
    I = (p * n * r) / 100
    A = p + I
    return I, A


# Take input from user
p = float(input("Please enter principal in INR"))
n = float(input("Please enter no of Years"))
r = float(input("Please enter rate of intrest in %"))

# Call the Function
I, A = simple_intrest(p, n, r)

# Print the result
print(f"Simple_intrest : {I:.2f}INR")
print(f"Amount : {A:.2f}INR")
