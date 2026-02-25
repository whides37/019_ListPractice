import math

num = float(input("半径を計算したい数字を入力してね:"))

menseki = num * num * math.pi
print("その円の面積は、だいたい", round(menseki, 2))
print(f"その円の面積は、だいたい {menseki:.2f}")

age = int(input("年齢を入力してね:"))

if age <20:
    print("あなたは未成年者ですね")
elif 20 <= age < 100:
    print("あなたは成年者ですね")
elif age > 100:
    print("あなたは大長寿ですね")
