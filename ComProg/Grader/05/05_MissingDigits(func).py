def missing_digits(t):
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    for number in t:
        if number in num_list:
            num_list.remove(number)
    return [int(e) for e in num_list]

exec(input())
