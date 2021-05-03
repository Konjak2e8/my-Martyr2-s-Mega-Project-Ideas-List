s = '#' + '#'.join(input()) + '#'
p = [0] * len(s)
Max = 0
ans = 0
for i in range(len(s)):
    if i < Max:
        p[i] = min(Max - i, p[pos * 2 - i])
    else:
        p[i] = 1
    while i - p[i] >= 0 and i + p[i] < len(s) and s[i - p[i]] == s [i + p[i]]:
        p[i] += 1
    if i - 1 + p[i] > Max:
        Max = i - 1 + p[i]
        pos = i
    ans = max(ans, p[i])
print(ans-1)
