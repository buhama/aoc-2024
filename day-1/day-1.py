
leftList = []
rightList = []

with open("input.txt", "r") as file:
    for line in file:
        left, right = line.split()
        leftList.append(int(left))
        rightList.append(int(right))

sortedLeftList = sorted(leftList)
sortedRightList = sorted(rightList)

differences = []

for i in range(len(sortedLeftList)):
    difference = abs(sortedRightList[i] - sortedLeftList[i])
    differences.append(difference)

print(sum(differences))

# part 2

def find_num_of_occurrences(num):
    return rightList.count(num)

similarity_score = 0

for num in leftList:
    similarity_score += find_num_of_occurrences(num) * num

print(similarity_score)
