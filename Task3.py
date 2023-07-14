# 不定參數資料， data 裡想放什麼都可以
def func(*data):
    middle_name = {}
    for name in data:
        # print(name) # 依序一一印出所有人的名字
        if name[1] in middle_name:
            middle_name[name[1]].append(name)
        else:
            middle_name[name[1]] = [name]
    for key, value in middle_name.items():
        if len(value) == 1:
            print(value[0])
            return
    print("沒有")
func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有