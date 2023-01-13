def minTime(files, numCores, limit):
    answer = 0
    not_parrel = 0
    files = sorted(files, reverse=True)
    for t in files:
        if limit > 0 and (t % numCores == 0):
            answer += int(t / numCores)
            limit -= 1
        else:
            answer += t

    return int(answer)

if __name__ == '__main__':
