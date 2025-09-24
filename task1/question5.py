def fibonacci(num):
    if num==2:
        return [1, 1]
    return fibonacci(num-1).append(fibonacci(num-1)[-1]+fibonacci(num-1)[-2])

print(fibonacci(5))