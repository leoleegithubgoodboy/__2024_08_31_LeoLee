import tool
while True:

    kg=0  #清除變數
    cm=0  #清除變數
    cm,kg = tool.input_data() #呼叫funtion
    print(f'身高={cm},體重={kg}')
    BMI = tool.calculate_bmi(kg=kg,cm=cm) #引述名稱呼叫，可以不用依照順序
    print(tool.get_status(BMI)) #列印狀態
    print(f'BMI={BMI}')
    play_agin = input("還要繼續嗎?(y/n)")
    if play_agin == "n":
        break
print('程式結束')
    
