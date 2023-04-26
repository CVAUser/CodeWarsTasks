def count_change(money, coins):
    result = 0
    sum = 0
    if(sum == money):
        result += 1
    else: 
        for i in range(len(coins)):
            if (money % coins[i] == 0):
                result += 1
            # sum = sum + coins[i]
            result = result + count_change(money, coins[i+1:])
        # print(result)
    return result

print(count_change(10, [5,2,3]))