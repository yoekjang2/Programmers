def solution(code):
    mode = 0
    ret = ""
    for index, i in enumerate(code):
        if i == '1' and mode == 0:
            mode = 1
        elif i == '1' and mode == 1:
            mode = 0
        elif i != '1' and i != '0':
            if mode == 0 and index%2 ==0:
                ret += i
            elif mode == 1 and index%2 !=0:
                ret += i
    if ret == "":
        ret = "EMPTY"
    return ret
                
            
        