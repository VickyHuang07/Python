c_str = input('目前攝氏溫度為: ')
# c = int(c_str)     #原本自己寫的
c = float(c_str)     #溫度是可能有小數的, 所以要用float
f = c * 9/5 + 32
print('目前華氏溫度為:', f )
