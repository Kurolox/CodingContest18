#from os import listdir
#
#lvlfiles = [file for file in listdir("input")]
#
#for lvlfile in lvlfiles:
#    with open(f"input/{lvlfile}") as currentfile:
#        file_content = currentfile.read().replace('\n', ' ').split(' ')
#        print(file_content)

def check_asteroid(max_x, max_y, matrix):
    for x in range(newdict["x"]):
        for y in range(newdict["y"]):
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

processed_list=[]

with open("part1/input/lvl1-4.inp") as currentfile:
    file_content = currentfile.read().replace('\n', ' ').split(' ')[2:]
    image_number = file_content.pop(0)
    for num in range(int(image_number)):
        newdict = {}
        newdict["timestamp"] = int(file_content.pop(0))
        newdict["x"] = int(file_content.pop(0))
        newdict["y"] = int(file_content.pop(0))
        matrix = [[int(file_content.pop(0)) for x in range(newdict["x"])] for y in range(newdict["y"])] 
        result = check_asteroid(newdict["x"], newdict["y"], matrix)
        if result:
            processed_list.append(int(newdict["timestamp"]))
                
with open("part1/output/lvl1-4.out", "w") as currentfile:
    sorted_list = sorted(processed_list)
    for item in sorted_list:
        currentfile.write(f"{item}\n")
