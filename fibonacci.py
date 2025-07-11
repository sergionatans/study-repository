import matplotlib.pyplot as plt

# Usando loop
def fibonacci_loop(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usando recursão
def fibonacci_recursao(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursao(n-1) + fibonacci_recursao(n-2)

n = 10
valores = list(fibonacci_loop(n))
# Imprimindo os primeiros 10 termos usando o loo
print("Sequência de Fibonacci (loop):")
for numero in fibonacci_loop(10):
    print(numero, end=" ")
print("\n")

# Imprimindo o 10º termo usando a recursão
print("10º termo da Sequência de Fibonacci (recursão):", fibonacci_recursao(10 - 1))

plt.plot(range(n), valores, marker='o')
plt.title('gráfico com sequência de Fibonacci')
plt.xlabel('Índice(x)')
plt.ylabel('Valor(y)')
plt.grid(True)
plt.show()