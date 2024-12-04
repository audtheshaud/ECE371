import random
import statistics
import math
from scipy.stats import norm




def generate_rand(length):
    return ''.join(random.choice('01') for _ in range(length))

def run_test(numbers):
    ones = numbers.count('1')
    zeros = numbers.count('0')
    length = len(numbers)

    if ones + zeros != length or ones == 0 or zeros == 0:
        print("sequence must contain only both 1s & 0s")

    # count all the runs (same number in a row)
    runs = 1
    for i in range(1,length):
        if numbers[i] != numbers[i-1]: 
            runs += 1 #when numbers change, add to runs count

    # expected runs + variance ( from formula )
    expected_runs = (2 * ones * zeros / length) + 1
    variance_runs = (2 * ones * zeros *(2 * ones * zeros - length)) / (length**2 * (length - 1))
    
    z = (runs - expected_runs) / math.sqrt(variance_runs)

    #P value
    p_value = 2 * (1 - norm.cdf(abs(z))) # 2 tailed test

    return p_value, runs, expected_runs, z

#sample_rand = generate_rand(500)
#numbers collected from altera
true_rand = ["0000110100", "0000001110", "1010110011", "1110100011", "1010110011", "0111011011", "0101010011", "0000111011", "0101110011", "0101111111"]
total_rand = ""

#make number into 1 long string to be calculated on
for string in true_rand:
    total_rand += string 

print(total_rand)
p_value, runs, expected_runs, z = run_test(total_rand)

print(f"Runs: {runs}")
print(f"Expected Runs: {expected_runs:.2f}")
print(f"Z-Statistic: {z:.3f}")
print(f"P-Value: {p_value:.3f}")

alpha = .5

if p_value < alpha:
    print("reject null hypothesis: sequence not random")
else:
    print("fail to reject null hypothesis: the sequence could be random")