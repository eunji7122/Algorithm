def solution(participant, completion):
    answer = ''

    # tmp_list = participant.copy()
    #
    # for i in participant:
    #     if i in completion:
    #         tmp_list.remove(i)
    #         completion.remove(i)
    #
    # answer = tmp_list[0]
    count = {}
    for i in participant:
        try:
            count[i] += 1
        except:
            count[i] = 1
    tmp = [k for k, v in count.items() if v == 2]
    if len(tmp) != 0:
        answer = tmp[0]
        return answer
    if answer == '':
        answer = list(set(participant) - set(completion))
        return answer[0]
    return -1


print(solution(["kiki", "eden", "leo"], ["eden", "kiki"]))
