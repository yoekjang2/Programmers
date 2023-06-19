def solution(str1, str2):
    result = ""
    for i, j in zip(str1, str2):
        result += i + j
    return result