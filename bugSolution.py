def function_iterative(x):
    result = 0
    for _ in range(x):
        result += 1
    return result

print(function_iterative(5))
print(function_iterative(100000))