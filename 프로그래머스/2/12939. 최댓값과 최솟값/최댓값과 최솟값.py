def solution(s):
    si = list(map(int, s.split()))
    mi = str(min(si))
    ma = str(max(si))
    result = mi + ' ' + ma
    return result