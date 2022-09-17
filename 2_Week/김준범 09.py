def solve09(N,M,S,P):
    result = 0
    start_string = S[:M]
    start_index = 0
    end_index = start_index + M
    DNA = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
        }
    for i in start_string:
        DNA[i] += 1
    if DNA['A'] >= P[0] and DNA['C'] >= P[1] and DNA['G'] >= P[2] and DNA['T'] >= P[3]:
        result += 1
    for i in range(N - M):
        DNA[S[start_index + i]] -= 1
        DNA[S[end_index + i]] += 1
        if DNA['A'] >= P[0] and DNA['C'] >= P[1] and DNA['G'] >= P[2] and DNA['T'] >= P[3]:
            result += 1
    print(result)


data = "9 8\nCCTGGATTG\n2 0 1 1"
N, M = map(int, data.split('\n')[0].split(" "))
S = data.split('\n')[1]
P = list(map(int,data.split('\n')[2].split()))


solve09(N,M,S,P)

#test
# def p_9(N,M,S,P):
#     result = 0
#     start_string = S[:int(M)]
#     DNA = {용
#         'A': 0,
#         'C': 0,
#         'G': 0,
#         'T': 0
#         }
#     for i in start_string:
#         DNA[i] += 1
#     if DNA['A'] >= int(P[0]) and DNA['C'] >= int(P[1]) and DNA['G'] >= int(P[2]) and DNA['T'] >= int(P[3]):
#         result += 1
#     start_index = 0
#     end_index = start_index + int(M)
#
#     for i in range(int(N) - int(M)):
#         DNA[S[start_index + i]] -= 1
#         DNA[S[end_index + i]] += 1
#         if DNA['A'] >= int(P[0]) and DNA['C'] >= int(P[1]) and DNA['G'] >= int(P[2])  and DNA['T'] >= int(P[3]):
#             result += 1
#     print(result)
# if __name__ == '__main__':
#     N,M = map(str,input().split())
#     S = input()
#     P = list(map(str,input().split()))
#     p_9(N,M,S,P)