# K번째 수
def solution(array, commands):
    answer = []
    for x in range(0, len(commands)):
        list1 = array[commands[x][0]-1:commands[x][1]]
        list1.sort()
        answer.append(list1[commands[x][2]-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)