def fibonacci (n):
  if n < 1:
    return [n]

  return fibonacci(n - 1) + [n]

print(fibonacci(5))