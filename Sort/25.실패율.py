def solution(N, stages):
    answer = []
    max_stage = max(stages)
    count_list = [0]*(max_stage+1)
    length = len(stages)
    for i in range(length):
        count_list[stages[i]] += 1

    fail_rate = []
    for i in range(1, N+1):
        if(length == 0):
          fail_rate.append((0,i))
          continue
        fail_rate.append((count_list[i]/length,i))
        length -= count_list[i]
    fail_rate.sort(key=lambda x:(-x[0], x[1]))

    for item in fail_rate:
        answer.append(item[1])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))