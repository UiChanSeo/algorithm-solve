def solution(s):

    news = s.lower()
    news = news.split(' ')
    news1 = []

    for it in news:
        if len(it) > 0 and it[0].isalpha():
            temp = list(it)
            temp[0] = temp[0].upper()
            news1.append(''.join(temp))
        else:
            news1.append(it)
    return " ".join(news1)
