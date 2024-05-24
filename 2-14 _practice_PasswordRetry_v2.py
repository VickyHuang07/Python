# 2-14 password retry

password = 'a123456'
default_try_num = 3  #最大嘗試次數
try_attempts = 0     #目前嘗試次數

while try_attempts < default_try_num:
    keyin_str = input('請輸入密碼: ')
    try_attempts += 1

    if keyin_str == password:
        print('登入成功!')
        break
    elif try_attempts == default_try_num:
        print('已達最大嘗試登入次數, 離開系統.')
        break
    else:
        print('密碼錯誤, 還剩', default_try_num-try_attempts,'次嘗試機會!')
        
    
