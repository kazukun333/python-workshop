import random

fortunes = ["大吉", "中吉", "小吉", "吉", "末吉"]

name = input("あなたの名前は？ ")

result = random.choice(fortunes)

print(f"{name}さんの今日の運勢は...")
print(f"✨ {result} ✨")
