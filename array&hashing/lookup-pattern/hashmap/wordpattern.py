def wordPattern(s, pattern):
    word = s.split()

    if len(word) != len(pattern):
        return False

    s_to_pattern = {}
    pattern_to_s = {}

    for c, w in zip(pattern, word):

        if c in s_to_pattern and s_to_pattern[c] != w:
            return False

        if w in pattern_to_s and pattern_to_s[w] != c:
            return False

        s_to_pattern[c] = w
        pattern_to_s[w] = c

    return True

a = wordPattern("hi my my hi", "abba")
print(a)