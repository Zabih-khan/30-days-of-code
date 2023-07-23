list1 = [1,2,3,4,4,4]
dp = {}
for i in list1:
    if i not in dp:
        dp[i] = 0
    print(dp)
    dp[i] = dp[i] + 1
count = 0
for k,v in dp.items():
    if v==1:
        count += 1
print("The number of non-repeated element :",count)




