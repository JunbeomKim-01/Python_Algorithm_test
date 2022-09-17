def p_9(N,M,S,P):
    result = 0
    start_string = S[:int(M)]
    start_index = 0
    end_index = start_index + int(M)
    DNA = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
        }

    for i in start_string:
        DNA[i] += 1
    if DNA['A'] >= int(P[0]) and DNA['C'] >= int(P[1]) and DNA['G'] >= int(P[2]) and DNA['T'] >= int(P[3]):
        result += 1
    for i in range(int(N) - int(M)):
        DNA[S[start_index + i]] -= 1
        DNA[S[end_index + i]] += 1
        if DNA['A'] >= int(P[0]) and DNA['C'] >= int(P[1]) and DNA['G'] >= int(P[2])  and DNA['T'] >= int(P[3]):
            result += 1

    print(result)
if __name__ == '__main__':
    N,M = map(str,input().split())
    S = input()
    P = list(map(str,input().split()))
    p_9(N,M,S,P)