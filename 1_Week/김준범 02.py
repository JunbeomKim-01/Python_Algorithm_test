index = int(input())  # 과목 수
test = list(map(int, input().split()))
max_score = max(test) # 최대값
_points = [] # 새로운 값을 넣을 리스트
for score in test :
    _points.append(score/max_score *100) #새로운 값을 계산하여 리스트에 추가
_avg = sum(_points)/index #평균 계산
print(_avg)