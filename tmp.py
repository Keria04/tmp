import math
import random
import json
import os


class DataGenerator:
    def __init__(self, seed=42):
        self.seed = seed
        random.seed(seed)

    def generate_numbers(self, n):
        nums = []
        for _ in range(n):
            nums.append(random.randint(1, 1000))
        return nums

    def generate_matrix(self, n, m):
        matrix = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(random.randint(0, 9))
            matrix.append(row)
        return matrix


class MathUtils:

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

    @staticmethod
    def fibonacci(n):
        if n <= 1:
            return n
        return MathUtils.fibonacci(n - 1) + MathUtils.fibonacci(n - 2)

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        return a * b // MathUtils.gcd(a, b)


class SortAlgorithms:

    @staticmethod
    def bubble_sort(arr):
        arr = arr[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortAlgorithms.quick_sort(left) + middle + SortAlgorithms.quick_sort(right)

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = SortAlgorithms.merge_sort(arr[:mid])
        right = SortAlgorithms.merge_sort(arr[mid:])

        return SortAlgorithms._merge(left, right)

    @staticmethod
    def _merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


class FileManager:

    def __init__(self, base_dir="data"):
        self.base_dir = base_dir
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

    def save_json(self, name, data):
        path = os.path.join(self.base_dir, name)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def load_json(self, name):
        path = os.path.join(self.base_dir, name)
        with open(path, "r") as f:
            return json.load(f)

    def save_text(self, name, text):
        path = os.path.join(self.base_dir, name)
        with open(path, "w") as f:
            f.write(text)

    def read_text(self, name):
        path = os.path.join(self.base_dir, name)
        with open(path, "r") as f:
            return f.read()


class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)

                for neighbor in self.graph.get(node, []):
                    queue.append(neighbor)

        return order

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        order = [start]

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                order.extend(self.dfs(neighbor, visited))

        return order


def matrix_multiply(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)

    result = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += A[i][k] * B[k][j]

    return result


def count_words(text):
    words = text.split()
    counter = {}

    for w in words:
        w = w.lower()
        counter[w] = counter.get(w, 0) + 1

    return counter


def random_walk(steps=100):
    x = 0
    y = 0

    path = []

    for _ in range(steps):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])

        x += dx
        y += dy

        path.append((x, y))

    return path


def simulate_game(rounds=50):
    score = 0

    for i in range(rounds):
        player = random.randint(1, 6)
        computer = random.randint(1, 6)

        if player > computer:
            score += 1
        elif player < computer:
            score -= 1

    return score


def long_loop():
    total = 0

    for i in range(100):
        for j in range(50):
            for k in range(10):
                total += (i * j + k) % 7

    return total


def error_prone_function(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return None


def generate_large_structure():
    data = []

    for i in range(200):
        item = {
            "id": i,
            "value": random.randint(1, 1000),
            "flag": random.choice([True, False]),
            "tags": [random.randint(0, 5) for _ in range(5)]
        }
        data.append(item)

    return data


def main():

    gen = DataGenerator()

    nums = gen.generate_numbers(50)

    sorted_nums = SortAlgorithms.quick_sort(nums)

    primes = [x for x in nums if MathUtils.is_prime(x)]

    matrix1 = gen.generate_matrix(5, 5)
    matrix2 = gen.generate_matrix(5, 5)

    product = matrix_multiply(matrix1, matrix2)

    g = Graph()

    for i in range(10):
        g.add_edge(i, random.randint(0, 9))

    bfs_order = g.bfs(0)
    dfs_order = g.dfs(0)

    fm = FileManager()

    fm.save_json("numbers.json", sorted_nums)

    text = "this is a test this is only a test"
    counts = count_words(text)

    path = random_walk(200)

    score = simulate_game()

    structure = generate_large_structure()

    print("sorted:", sorted_nums[:5])
    print("primes:", primes[:5])
    print("bfs:", bfs_order)
    print("dfs:", dfs_order)
    print("word counts:", counts)
    print("game score:", score)
    print("structure size:", len(structure))


if __name__ == "__main__":
    main()