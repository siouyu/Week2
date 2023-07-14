def calculate_sum_of_bonus(data):
# 表現 above average 可以拿本薪的 10% 當作 bonus
# 表現 above average 可以拿本薪的 5% 當作 bonus
    employee = data["employees"]
    total_bonus = 0
    for abc in employee:
        if abc["performance"] == "above average":
            if not isinstance(abc["salary"],int): # 先判定資料型別是否都為 int 
                # print(isinstance(abc["salary"],int)) → 結果為 false
                if "USD" in abc["salary"]: # 如果資料中混雜 string 和 int
                    salary_usd = int(abc["salary"].replace("USD", ""))
                    # print(int(abc["salary"].replace("USD", ""))) → 確認 USD 被拿掉
                    salary = salary_usd*30
                    total_bonus = total_bonus + salary*0.1
                else: # 如果資料中只有 string，將 string 轉成 int
                    salary = int(abc["salary"])
                    total_bonus = total_bonus + salary*0.1
            else: # 如果資料本來就是 int
                total_bonus = total_bonus + salary*0.1
        
        elif abc["performance"] == "average":
            if not isinstance(abc["salary"],int):
                if "USD" in abc["salary"]: 
                    salary_usd = int(abc["salary"].replace("USD", ""))
                    salary = salary_usd*30
                    total_bonus = total_bonus + salary*0.05
                else: 
                    salary = int(abc["salary"])
                    total_bonus = total_bonus + salary*0.05
            else:
                total_bonus = total_bonus + salary*0.05
    print(int(total_bonus),"NTD")

calculate_sum_of_bonus({ "employees":[ 
{
    "name":"John", 
    "salary":"1000USD", 
    "performance":"above average",
    "role":"Engineer" 
}, 
{ 
    "name":"Bob", 
    "salary":"60000",
    "performance":"average", 
    "role":"CEO" 
}, 
{ 
    "name":"Jenny", 
    "salary":"50,000", 
    "performance":"below average", 
    "role":"Sales" 
} 
] 
}) 
# call calculate_sum_of_bonus function