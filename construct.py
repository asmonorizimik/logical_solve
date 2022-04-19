# def construct(ransom_note, magazine):
#     d = {}
#     for letter in magazine:
#         if letter in d:
#             d[letter] += 1
#         else:
#             d[letter] = 1
#     for char in ransom_note:
#         if char not in d and d[char]== 0:
#             return False
#         d[char] -= 1
#     return True
# print(construct(input("enter note"),input("enter megazine")))


