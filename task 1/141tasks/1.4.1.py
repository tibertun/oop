import math

class Vector:
    def __init__(self, components):
        if isinstance(components, Vector):
            self.components = components.components.copy()
        else:
            self.components = list(components)

    def show(self):
        print("Vector:", self.components)

    def dimension(self):
        return len(self.components)

    def length(self):
        return math.sqrt(sum(x**2 for x in self.components))

    def average(self):
        return sum(self.components) / len(self.components)

    def max_component(self):
        return max(self.components)

    def min_component(self):
        return min(self.components)

def read_vectors(filename):
    vectors = []

    with open(filename) as f:
        for line in f:
            nums = list(map(float, line.split()))
            vectors.append(Vector(nums))
    return vectors

def analyze_vectors(vectors):
    max_dim = max(v.dimension() for v in vectors)
    candidates = [v for v in vectors if v.dimension() == max_dim]
    v_max_dim = min(candidates, key=lambda v: v.length())

    print("vector with largest dimension:")
    v_max_dim.show()
    print("dimension:", v_max_dim.dimension())
    print("length:", v_max_dim.length())

    max_len = max(v.length() for v in vectors)
    candidates = [v for v in vectors if v.length() == max_len]
    v_max_len = min(candidates, key=lambda v: v.dimension())

    print("vector with largest length:")
    v_max_len.show()
    print("length:", v_max_len.length())

    avg_len = sum(v.length() for v in vectors) / len(vectors)
    print("average length:", avg_len)

    count = sum(1 for v in vectors if v.length() > avg_len)
    print("vectors longer than average:", count)

    max_comp = max(v.max_component() for v in vectors)
    candidates = [v for v in vectors if v.max_component() == max_comp]
    v_max_comp = min(candidates, key=lambda v: v.min_component())

    print("vector with maximal largest component:")
    v_max_comp.show()

    min_comp = min(v.min_component() for v in vectors)
    candidates = [v for v in vectors if v.min_component() == min_comp]
    v_min_comp = max(candidates, key=lambda v: v.max_component())

    print("vector with minimal smallest component:")
    v_min_comp.show()


files = [
    "input11",
    "input12",
    "input13",
    "input14"
]

for file in files:
    print("Processing file:", file)
    vectors = read_vectors(file)
    analyze_vectors(vectors)