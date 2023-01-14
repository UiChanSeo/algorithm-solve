def solution(participant, completion):
    participant.sort()
    completion.sort()

    #print(participant, completion)

    len1 = len(participant)

    pos1 = 0
    cnt = 2

    midPos = mid = int(len1/2)

    while mid >= 1:
        if mid == 1 :
            if midPos == (len1 -1):
                return participant[midPos]
            else:
                if completion[midPos] == participant[midPos+1]: #left
                    mid =
                    return participant[midPos]
                else:
                    return participant[midPos+1]

        else:
            mid = int(mid/2)
            if participant[midPos] == completion[midPos]:
                midPos = midPos + mid
            else:
                midPos = midPos - mid
