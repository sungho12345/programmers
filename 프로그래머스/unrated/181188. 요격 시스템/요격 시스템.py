def solution(targets):
    targets.sort(key = lambda x: x[1]) # 뒤에 요소를 기준으로 정렬
    shoot = -1
    cnt = 0
    for target in targets: 
        if target[0] >= shoot : # 뒤의 요소와 다음꺼 앞의 요소를 비교함
            cnt += 1
            shoot = target[1]
    return cnt