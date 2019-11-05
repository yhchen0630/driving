#台灣及美國考取汽車駕照年齡
country = input('請問你是哪國人？')
age = input('請輸入你幾歲？')
age = int(age)
if country == '台灣':
    if age < 18:
        print('你還不能考駕照')
    else:
        print('你可以考駕照')
elif country =='美國':
    if age >= 16:
        print('你們可以考駕照')
    else:
        print('你還不能考駕照')
else:
    print('只有美國台灣二選一')