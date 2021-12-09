def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


# The following generator computes an approximation of the value of pi
# according to Leibniz's expansion series
def pi_series():
    odds = odd_numbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


iterations = input("Please enter the desired number of iterations")
while True:
    if not iterations.isnumeric():
        iterations = input("Please enter a numeric value")
        continue
    iterations = int(iterations)
    break

approx_pi = pi_series()

for i in range(iterations):
    print(next(approx_pi))
