count=0
t=361
while true:
    count+=1
    data=random.normalvariate(0,1)
    if round(data)==t:       
        print(count,"恭喜抽到荣耀水晶！")
        break
    elif count==361:
        print(count,"恭喜抽到荣耀水晶！")
        break
    else:
        print(count,"很遗憾呢...")       
        if count == 354:
            t =6
        elif count >= 355:
            t -= 1
        elif count >= 300:
            t -= 6
