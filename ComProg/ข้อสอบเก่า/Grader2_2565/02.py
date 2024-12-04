def match(word, pattern, include_chars, exclude_chars):
    word_check = []
    if len(word) != len(pattern):
        return False
    for i in range(len(word)):
        if pattern[i] != '?' and word[i] != pattern[i]:
            return False
        if pattern[i] == '?' and word[i] in exclude_chars:
            return False
        if pattern[i] == '?':
            word_check.append(word[i])
            
    for c in include_chars:
        if c not in word_check:
            return False
        else:
            word_check.remove(c)
            
    return True

exec(input())