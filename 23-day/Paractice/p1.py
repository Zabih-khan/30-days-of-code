# def nsplit(n,s):
#     lst = []
#     st = ""
#     count = 0
#     for i in s:
#         st += i
#         count = count + 1
#         if count == n or i == len(s)-1:
#             lst.append(st)
#             st = ""
#             count = 0
#     print(lst)
#
# str = "Umair"
# nsplit(1,str)
# nsplit(2,str)
# # nsplit(1,str)
# # nsplit(1,str)
# # nsplit(4,str)

def nsplit(n,s):
     lst = []
     str = ''
     count = 0
     for i in s:
         count = count + 1
         str += i
         if count == n:
               lst.append(str)
               count = 0
               str = ""
     print(lst)

s = "umair"
nsplit(1,s)


