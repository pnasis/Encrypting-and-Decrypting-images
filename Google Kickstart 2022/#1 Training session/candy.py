# PROBLEM: You have gathered N bags of candy and you want to distribute amongst M kids. The i bag contains Ci pieces of candy. You want to make sure that
# every kid get the same amount of candy and that the number of pieces of candy they receive is the greatest possible. You can open one bag and
# mix all pieces of candy before destributing them to the kids.

# INPUT: 1)first line= number of test cases, 2)Each test case consists of two lines, i) number of candy bags & number of kids, ii)number of candy
# of each bag.

# OUTPUT: Number of case & remaining candy.

def method(case_num):
    
    # Number of bags and number of kids.
    (bags, kids) = tuple(map(int, input().split()))
    # How many candy each bag contains.
    count = list(map(int, input().split()))
    
    # Culculating total amount of candy.
    total = 0
    for i in range(bags):
        total += count[i]
    
    # Calculating using modulo, the remaining candy.   
    remaining = total % kids
    
    # Results.
    print(f"Case #{case_num}: {remaining}")
    
#Number of cases.
cases = int(input())
for i in range(cases):
    method(i+1)