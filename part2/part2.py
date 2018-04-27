#from os import listdir
#
#lvlfiles = [file for file in listdir("input")]
#
#for lvlfile in lvlfiles:
#    with open(f"input/{lvlfile}") as currentfile:
#        file_content = currentfile.read().replace('\n', ' ').split(' ')
#        print(file_content)
from collections import defaultdict

def check_asteroid(max_x, max_y, matrix):
    for x in range(max_x):
        for y in range(max_y):
            if (matrix[x][y] != 0): # If it isn't 0, check adjacents
                if x > 0:
                    if matrix[x-1][y] != 0:
                        return True
                if x < max_x:
                     if matrix[x+1][y] != 0:
                        return True
                if y > 0:
                    if matrix[x][y-1] != 0:
                        return True
                if y < max_y:
                    if matrix[x][y+1] != 0:
                        return True
    return False

processed_dict = {}
asteroid_list = []


def normalize(max_x, max_y, matrix):
    # Remove all files without significative numbers:
    matrix_copy = matrix[:]
    for x in matrix_copy:
        if x.count(0) == max_y:
            matrix.remove(x)

    # Then remove all columns without significative numbers:
    matrix = [list(x) for x in zip(*matrix)]
    matrix_copy = matrix[:]
    for x in matrix_copy:
        if sum(x) == 0:
            matrix.remove(x)

    matrix = [list(x) for x in zip(*matrix)]
    for row in range(len(matrix)):
        for item in range(len(matrix[0])):
            if matrix[row][item] != 0:
                matrix[row][item] = 1

    return matrix

with open("part2/input/lvl2-4.inp") as currentfile:
    file_content = currentfile.read().replace('\n', ' ').split(' ')[2:]
    image_number = file_content.pop(0)
    for num in range(int(image_number)):
        newdict = {}
        newdict["timestamp"] = int(file_content.pop(0))
        newdict["x"] = int(file_content.pop(0))
        newdict["y"] = int(file_content.pop(0))
        matrix = [[int(file_content.pop(0)) for x in range(newdict["y"])] for y in range(newdict["x"])] 
        result = check_asteroid(newdict["x"], newdict["y"], matrix)
        if result:
            normalized_matrix = normalize(newdict["x"], newdict["y"], matrix)
            if normalized_matrix not in asteroid_list:
                asteroid_list.append(normalized_matrix)
            processed_dict[newdict["timestamp"]] = normalized_matrix

with open("part2/output/lvl2-4.out", "w") as currentfile:
    maxlen = 0
    last_dict = []
    for asteroid in asteroid_list:
        shared_stamps = [i for i,j in processed_dict.items() if j == asteroid]
        shared_stamps.append(len(shared_stamps))
        shared_stamps =[shared_stamps[0]] + shared_stamps[-2:]
        last_dict.append(shared_stamps)
        if len(shared_stamps) > maxlen:
            maxlen = len(shared_stamps)

    print(last_dict)
    for item in last_dict:
        currentfile.write(" ".join([str(num) for num in item]) + "\n")

    