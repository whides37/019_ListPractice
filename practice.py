import math

#入力受付した文字を数字に変換するのを忘れない。
num = float(input("半径を計算したい数字を入力してね: "))

menseki = int(num * num * math.pi)
print("その円の面積は、だいたい", menseki)

