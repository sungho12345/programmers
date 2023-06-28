def solution(r1, r2):
    answer = 0
    i, j = r2, r1
    for x in range(r2+1):
        while (i**2 + x**2) > r2**2:
            i -= 1
        while (j-1)**2 + x**2 >= r1**2 and j-1:
            j -= 1
        answer += i-j+1
    return answer*4