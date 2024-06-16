# Task 1: Basic Boolean Operations
def check_truth(a, b, c):
    return (a and b) or c

print(check_truth(True, False, True))  # True

# Task 2: Logical Equivalence
def logical_equivalence(a, b):
    return a == b

print(logical_equivalence(True, True))  # True
print(logical_equivalence(True, False))  # False

# Task 3: Exclusive Or (XOR)
def xor(a, b):
    return (a or b) and not (a and b)

print(xor(True, False))  # True
print(xor(True, True))  # False

# Task 4: Conditional Greeting
def greet(flag):
    return "Hello, World!" if flag else "Goodbye, World!"

print(greet(True))  # Hello, World!
print(greet(False))  # Goodbye, World!

# Task 5: Nested Conditions
def nested_conditions(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y != z != x:
        return "All different"
    else:
        return "Neither"

print(nested_conditions(3, 3, 3))  # All same
print(nested_conditions(4, 5, 6))  # All different

# Task 6: Conditional Counting
def count_true(*args):
    return sum(args)

print(count_true(True, False, True, False, True))  # 3

# Task 7: Boolean Parity
def parity(n):
    return n % 2 == 1

print(parity(3))  # True
print(parity(4))  # False

# Task 8: Majority Vote
def majority_vote(a, b, c):
    return sum([a, b, c]) > 1

print(majority_vote(True, True, False))  # True
print(majority_vote(True, False, False))  # False

# Task 9: Boolean Switch
def switch(flag):
    return not flag

print(switch(True))  # False
print(switch(False))  # True

# Task 10: Ternary Operator Simulation
def ternary_check(condition, true_result, false_result):
    return true_result if condition else false_result

print(ternary_check(True, "Yes", "No"))  # Yes
print(ternary_check(False, "Yes", "No"))  # No

# Task 11: Validate Combination
def validate(x, y, z):
    return (x and y) or z

print(validate(True, False, True))  # True
print(validate(False, False, True))  # True

# Task 12: Condition Chain
def chain_check(x, y, z):
    if x < y < z:
        return "Increasing"
    elif x > y > z:
        return "Decreasing"
    else:
        return "Neither"

print(chain_check(1, 2, 3))  # Increasing
print(chain_check(3, 2, 1))  # Decreasing

# Task 13: Boolean Filter
def filter_true(values):
    return [v for v in values if v]

print(filter_true([True, False, True, False]))  # [True, True]

# Task 14: Conditional Multiplier
def multiplier(a, b, c, n):
    if a:
        return n * 2
    elif b:
        return n
    elif c:
        return n - 5
    else:
        return n

print(multiplier(False, False, True, 10))  # 5
print(multiplier(True, False, False, 10))  # 20
