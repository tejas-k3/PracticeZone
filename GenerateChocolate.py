"""
Que : You are given 1 chocolate at the beginning. You can do two spells
on it, spell 1 generates (2x - 1) chocolates and spell 2 does (2x + 1)
where x is the number of chocolates before the spell. Now, you've to
construct a sequence of spells, such that after using them in order,
you will have exactly 'n' chocolates. You can use two spells in any
order at most 40 times in total.
Input : Each test contains multiple test cases. The first line contains
a single int t (1 <= t <= 10^4) ~ the no of test cases. In each testcase
there will be one line with a single int n (2 <= n <= 10^9)

Output : For each test case, output the following ->
IF it's possible to reach n with constraints, print two lines
line one is total number of spells used
line two is spells used in their order

Sample I/O:                 Sample O/P:
4                           -1
2                           1
3                           2
7                           2
17                          2
                            2 2
                            4
                            2 1 1 1

"""
def generate_chocolates(n):
    spells = []
    steps = 0
    if n%2 == 0:
        return -1, []
    # Odd number logic
    # n = 1, 1
    # l = 0
    # r = 1
    # 
    while n > 1 and steps <= 40:
        left_condition = (n - 1)//2 # n = 2x +1 
        right_condition = (n + 1)//2 # n = 2x - 1
        # print("N", n, " left ", left_condition, " right ", right_condition)
        if left_condition % 2 == 1:
            n = left_condition
            spells.append(2)
        elif right_condition % 2 == 1:
            n = right_condition
            spells.append(1)
        steps += 1
    
    if n == 1 and steps <= 40:
        return steps, spells[::-1]
    else:
        return -1, []

# Example usage
steps = []
spell_sequence = []
test_cases = int(input("Enter the number of test cases: "))
for _ in range(test_cases):
    num_chocolates = int(input())
    a, b = generate_chocolates(num_chocolates)
    steps.append(a)
    spell_sequence.append(b)
print("######################")
for i in range(test_cases):
    print(steps[i])
    if steps[i] == -1:
        continue
    print(spell_sequence[i])
