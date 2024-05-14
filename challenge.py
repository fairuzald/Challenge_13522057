def calculate_tour_length(matrix, tour):
    length = 0
    for i in range(len(tour) - 1):
        length += matrix[tour[i]][tour[i+1]]
    length += matrix[tour[-1]][tour[0]] 
    return length

def generate_permutations(elements):
    if len(elements) == 0:
        return []
    if len(elements) == 1:
        return [elements]
    
    perms = []
    for i in range(len(elements)):
        elem = elements[i]
        rest = elements[:i] + elements[i+1:]
        for perm in generate_permutations(rest):
            perms.append([elem] + perm)
    return perms

def tsp(matrix):
    num_cities = len(matrix)
    all_tours = generate_permutations(list(range(num_cities)))
    
    min_weight = float('inf')
    best_tour = None
    
    for tour in all_tours:
        length = calculate_tour_length(matrix, tour)
        if length < min_weight:
            min_weight = length
            best_tour = tour

    res = [i+1 for i in best_tour]
    res.append(res[0])
            
    return res, min_weight

matrix1 = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]

matrix2 = [
    [float('inf'), 20, 30, 10,11],
    [15, float('inf'), 16, 4, 2],
    [3, 5, float('inf'), 2, 4],
    [19, 6, 18, float('inf'), 3],
    [16, 4, 7, 16, float('inf')]
]

matrix3 = [
    [float('inf'), 12, 10, 0, 0, 0, 12], 
    [12, float('inf'), 8, 12, 0, 0, 0],   
    [10, 8, float('inf'), 11, 3, 0, 9],   
    [0, 12, 11, float('inf'), 11, 10, 0],   
    [0, 0, 3, 11, float('inf'), 6, 7],   
    [0, 0, 0, 10, 6, float('inf'), 9],   
    [12, 0, 9, 0, 7, 9, float('inf')],    
]

matrices = [matrix1, matrix2, matrix3]

for idx, matrix in enumerate(matrices):
    print("=====================================")
    print("================Matrix:"+ idx + 1+"================")
    print("=====================================")
    best_tour, min_weight = tsp(matrix)
    print("Best tour:", end=" ")
    for i in range(len(best_tour) - 1):
        if i == len(best_tour) - 2:
            print(best_tour[i], end="\n")
        else:
            print(best_tour[i], end=" -> ")
    print("Minimum length:", min_weight)
    print("\n")