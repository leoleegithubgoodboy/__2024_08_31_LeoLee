def input_data()->tuple[int,int]:
    while True:
        try:    
            cm = int(input("請輸入身高(公分):"))
            if cm > 300:
                    raise Exception("超過300公分")
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
        except Exception as e:
            print(f'輸入錯誤{cm}')
            continue
    while True:
        try:    
            kg = int(input("請輸入體重(公斤):"))
            if kg > 300:
                raise Exception("超過300公分")
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
        except Exception as e:
            print(f'輸入錯誤{kg}')
            continue
    return (cm,kg)  #tuple

def get_status(BMI:float)->str:
    
    if BMI >=35:
        return ("重度肥胖：BMI≧35")
    elif BMI >=30:
        return ("中度肥胖：30≦BMI")
    elif BMI >=27:
        return ("輕度肥胖：27≦BMI")
    elif BMI >=24:
        return ("過重")
    elif BMI >=18.5:
        return ("正常範圍")
    else:
        return ("體重過輕")
    
while True:
    
    kg=0  #清除變數
    cm=0  #清除變數
    cm,kg = input_data() #呼叫funtion
    print(f'身高={cm},體重={kg}')
    cm=(cm/100)*(cm/100)
    BMI=kg/cm
    print(get_status(BMI))
    #print(f'BMI={BMI}')
    play_agin = input("還要繼續嗎?(y/n)")
    if play_agin == "n":
        break
print('程式結束')
    
