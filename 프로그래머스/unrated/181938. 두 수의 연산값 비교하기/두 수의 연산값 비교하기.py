def solution(a, b):
    A = int(f"{a}{b}")
    B = 2 * a * b
    if A > B:
        return A
    elif A < B:
        return B
    elif A == B:
        return A