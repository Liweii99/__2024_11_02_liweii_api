class BMI():
    def __init__(self,name:str,height:float,weight:float):
        self.name=name
        self.height = height
        self.weight = weight
    def get_BMI(self)->float:
        BMI_issue = round(self.weight/ ((self.height/100)**2),2)
        return BMI_issue

    def get_status(self)->str:
        bmi = self.get_BMI()
        if bmi >= 35 :
            return '重度肥胖'
        elif bmi >= 30 :
            return'中度肥胖'        
        elif bmi >= 27 :
            return'輕度肥胖'
        elif bmi >= 24 :
            return'體重過重'
        elif bmi >= 18.5 :
            return'正常範圍'
        else :
            return'體重過輕'
   
while(True):
    try:
        name = input("姓名:")
        height = float(input("請輸入身高(公分):"))
        weight = float(input("請輸入體重(公斤):"))
        p1 = BMI(name=name,height=height,weight=weight)   
        break
    except Exception:
        print('輸入格式錯誤,請重新輸入!')
    
print(f"您的BMI值是{p1.get_BMI()}\n您的體重是{p1.weight}\n您的身體質量指數屬於")
print(p1.get_status())
print("程式結束")