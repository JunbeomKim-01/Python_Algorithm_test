def p_2(index,test):
    max_score = max([int(x) for x in test])  # 최대값
    _points = []  # 새로운 값을 넣을 리스트
    for score in test:
        _points.append(int(score) / max_score * 100)  # 새로운 값을 계산하여 리스트에 추가
    _avg = sum(_points) / int(index)  # 평균 계산
    print(_avg)

if __name__ == '__main__':
    index = input()  # 과목 수
    test = list(map(str, input().split()))
    p_2(index,test)