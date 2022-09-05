index = int(input())  # 과목 수
test = list(map(int, input().split()))
max_score = max(test)
new_point = []
for score in test :
    new_point.append(score/max_score *100)  # 새로운 점수 생성
_avg = sum(new_point)/index
print(_avg)