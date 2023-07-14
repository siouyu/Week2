def get_number(index):
    if (index+1) % 2 == 0: # 判斷奇數偶數
        i = (index+1) // 2
        # print(i) # i 是指第幾個偶數項目
        print(1+i*3)
    else:
        i = (index+1) // 2
        print(i*3)
        return
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15
# get_number(16)