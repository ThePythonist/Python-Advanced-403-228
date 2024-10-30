def multiplier(x, y):
    if y == 1:
        return x
    else:
        return x + multiplier(x, y - 1)


print(multiplier(4, 4))

# 3 + 3 + 3 + 3 + 3

# ===================================================

# x, y = 3, 5
# output = 0
# while y > 1:
#     output += x
#     y -= 1
# else:  # 1 bar ejra mishe
#     output += x
#
# print(output)
