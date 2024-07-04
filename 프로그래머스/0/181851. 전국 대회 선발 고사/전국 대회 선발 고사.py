def solution(rank, attendance):
    attendable_students = [idx for idx, flag in enumerate(attendance) if flag]
    a, b, c, *_ = sorted(attendable_students, key=lambda x: rank[x])
    return 10000 * a + 100 * b + c


    