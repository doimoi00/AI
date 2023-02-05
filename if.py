menupans={'커피':500,'술':5000,'안주':12000}

jumnuns=input("주문해주세요. '커피':500,'술':5000,'안주':12000 입니다 >>>")
moneys=int(input("입금해주세요>>>"))


if jumnuns =='커피':
    if moneys > 500:

        print("그래 줄께, 거스럼 돈은 {}이다" .format(moneys-500))
    
    elif moneys == 500:

        print("그래 줄께, 거스럼 돈은 없다")

    
    else:
        print("돈 더 내라 {}가 부족하다" .format(500-moneys))


if jumnuns =='술':
    if moneys > 5000:

        print("그래 줄께, 거스럼 돈은 {}이다" .format(moneys-5000))
    
    elif moneys == 5000:

        print("그래 줄께, 거스럼 돈은 없다")


    else:
        print("돈 더 내라 {}가 부족하다" .format(5000-moneys))

        
if jumnuns =='안주':
    if moneys > 12000:

        print("그래 줄께, 거스럼 돈은 {}이다" .format(moneys-12000))
    
    elif moneys == 12000:

        print("그래 줄께, 거스럼 돈은 없다")



    else:
        print("돈 더 내라 {}가 부족하다" .format(12000-moneys))

##############################################################################