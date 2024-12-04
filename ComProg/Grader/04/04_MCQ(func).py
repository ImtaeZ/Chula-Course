def grade_mcq(sol, ans):
    counter = 0
    if len(sol) == len(ans):
        for i in range(len(sol)):
            if sol[i] == ans[i]:
                counter += 1
    else:
        return -1
    return counter

exec(input())