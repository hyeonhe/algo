a, b = map(int, input().split())
a_div, a_mod = divmod(a, 4)
b_div, b_mod = divmod(b, 4)

print(abs(a_div - b_div) + abs(a_mod - b_mod))
