# 2-14 password retry

password = 'a123456'
default_try_num = 3  #最大嘗試次數
rest_try_num = 3     #目前嘗試次數

while rest_try_num <= default_try_num and rest_try_num > 0:
    keyin_str = input('請輸入密碼: ')
    if keyin_str != password:
        rest_try_num = rest_try_num - 1
        if rest_try_num == 0:
            print('密碼錯誤! 多次嘗試密碼錯誤, 自動離開系統.')
            break
        else:
            print('密碼錯誤! 還有',  rest_try_num, '次機會')
    else:
        print('登入成功')
        break



        
    
