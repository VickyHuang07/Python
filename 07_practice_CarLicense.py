# 2-10 程式練習
driving_str = input('請問你有開過車嗎? ')
if driving_str != '有' and driving_str != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit

age_str = input('請問你的年齡: ')
age = int(age_str)
if driving_str == '有':
    if age >= 18:
        print('祝行車平安!')
    else:
        print('奇怪, 你怎麼能開車?')
elif driving_str == '沒有':
    if age >= 18:
        print('你可以駕照了, 嘗試看看呀!')
    else:
        print('很好, 再過幾年就可以去考駕照了!')