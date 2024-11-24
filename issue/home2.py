def input_data(): 
    while True:
        try:    
            cm = int(input("請輸入身高(公分):"))
            if cm > 300:
                raise Exception("超過300公分")
            break
        except ValueError:
            print('輸入格式錯誤,請重新輸入')
            continue
        except Exception as e:
            print(f'限300內,您的值{cm}請重新輸入')
            continue
    while True:
        try:    
            kg = int(input("請輸入體重(公斤):"))
            if kg > 300:
                raise Exception("超過300公斤")
            break
        except ValueError:
            print('輸入格式錯誤,請重新輸入')
            continue
        except Exception as e:
            print(f'限300內,您的值{kg}請重新輸入')
            continue
    return cm,kg

def get_status(bmi:float)->str:
    if BMI >=35:
        print("重度肥胖:BMI≧35")
    elif BMI >=30:
        print("中度肥胖:30≦BMI")
    elif BMI >=27:
        print("輕度肥胖:27≦BMI")
    elif BMI >=24:
        print("過重")
    elif BMI >=18.5:
        print("正常範圍")
    else:
        print("體重過輕")

while True:
    kg=0  
    cm=0  
    cm,kg = input_data() 

    print(f'身高={cm},體重={kg}')
    cm=(cm/100)*(cm/100)
    BMI=round((kg/cm),2)
    print(f'BMI={BMI}')
    get_status(BMI) 
    
    play_again = input("還要繼續嗎?(y,n)")
    if play_again == "n":
        break

print('程式結束')