# main.py в основном репозитории
from fibonacci_project.recursive import fib_recursive
from fibonacci_project.iterative import fib_iterative
from fibonacci_project.memoization import fib_memo

def main():
    n = 10  # Пример для вычисления числа Фибоначчи

    print(f"Рекурсивное вычисление F({n}) = {fib_recursive(n)}")
    print(f"Итеративное вычисление F({n}) = {fib_iterative(n)}")
    print(f"Мемоизация F({n}) = {fib_memo(n)}")

if __name__ == "__main__":
    main()
