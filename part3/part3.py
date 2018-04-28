#from os import listdir
#
#lvlfiles = [file for file in listdir("input")]
#
#for lvlfile in lvlfiles:
#    with open(f"input/{lvlfile}") as currentfile:
#        file_content = currentfile.read().replace('\n', ' ').split(' ')
#        print(file_content)
from collections import defaultdict
from operator import itemgetter

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

with open("part3/input/lvl3-1.inp") as currentfile:
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

with open("part3/output/lvl3-1.out", "w") as currentfile:
    maxlen = 0
    last_dict = []
    real_last_dict = []
    for asteroid in asteroid_list:
        shared_stamps = [i for i,j in processed_dict.items() if j == asteroid]
        #shared_stamps.append(len(shared_stamps))
        last_dict.append(shared_stamps)

    print(last_dict)
    for subset in last_dict:
        for number in subset:
            number_index = subset.index(number)
            if number_index > 0:
                k = number - subset[number_index - 1]
                if k > 1:
                    if set([number - k, number, number + k, number + 2*k]).issubset(subset):
                        flag = True
                        iterations = 4
                        while(flag):
                            test_subset = [number - k + (j * k) for j in range(iterations)]
                            if set(test_subset).issubset(subset):
                                iterations += 1
                            else:
                                flag = False
                        print("MAXITERS: " + str(iterations))
                        print(str([number - k + (j * k) for j in range(iterations)]))

                            



        
     #   currentfile.write(" ".join([str(num) for num in item]) + "\n")

    