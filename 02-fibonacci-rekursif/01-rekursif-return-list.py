def fibonacci (n):
  if n < 1:
    return [n]

  return [n] + fibonacci(n - 1)

print(fibonacci(5))
