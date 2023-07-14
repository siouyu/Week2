def find_and_print(messages):
    # 有實際提到自己年紀或達到台灣法定年齡、現在是大學生（假設沒有跳級）、有投票權的人都算 17 歲以上
    older_than_17 = []
    for name, message in messages.items():
        if "years old" in message or "legal age" in message or "college" in message or "vote" in message:
            older_than_17.append(name)
    for name in older_than_17:
        print(name)
messages = {
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
}
# Call the function to find and print the names of individuals who are most likely older than 17
find_and_print(messages)
