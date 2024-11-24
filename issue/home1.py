#BMI計算公式: BMI=體重(Kg)/身高(m)**2
try:   
    is_add = input("您是否為成年人?(y,n)")
    if is_add == 'y':
        height = float(input("請輸入身高(公分):"))
        if height > 190 or height < 140:
            raise Exception("請接洽醫師")
        weight = float(input("請輸入體重(公斤)"))
        if weight>120 or weight<30:
            raise Exception("請接洽醫師") 
        print(f"身高{height}公分，體重{weight}公斤") 
        
        bmi  = weight/((height/100)**2)
        print(f"BMI是:{bmi:.1f}")
        if bmi >=35:
            print("您是重度肥胖")
        elif bmi>=30:
            print("您是中度肥胖")
        elif bmi>=27:
            print("您是輕度度肥胖")
        elif bmi>=24:
            print("您的體重過重")    
        elif bmi<18.5:
            print("您的體重過輕")
        else:
            print("您的體重正常")    
except ValueError:
    print("輸入格式有錯")
except Exception as e:
    print(f"異常訊息:{e}")

print("謝謝您的回應")