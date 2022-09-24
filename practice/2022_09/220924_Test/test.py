from itertools import combinations, permutations, product

def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

items = [1, 2, 3, 4, 5]
list(permutations(items, 2))
list(combinations(items, 2))
list(product(*items))

letters = ["A", "B", "C"]
pairs = list(zip(items, letters))
numbers, letters = zip(*pairs)

dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}

for key in dict: 
    print(dict)

for val in dict.values():
    print(val)

for key, val in dict.items():
    print("key={key}, value={value}").format(key=key, value=val)
    