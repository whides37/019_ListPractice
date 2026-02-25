# 課題1:半径 r を入力すると、円の面積を計算して表示するプログラムを書いてみよう。

import math

num = float(input("半径を計算したい数字を入力してね:"))

menseki = num * num * math.pi
print("その円の面積は、だいたい", round(menseki, 2))
print(f"その円の面積は、だいたい {menseki:.2f}")


# 課題2:ユーザーに年齢を入力してもらい、条件分岐を表示するプログラムを作る。

age = int(input("年齢を入力してね:"))

if age <20:
    print("あなたは未成年者ですね")
elif 20 <= age < 100:
    print("あなたは成年者ですね")
elif age > 100:
    print("あなたは大長寿ですね")

# 課題3:1〜10 の数字を順番に表示するプログラムを書こう。

for i in range(1, 11):
    # print(i)　#改行あり、カンマなし
    print(i, end=",")#改行なし、カンマ区切り
    # print(",".join(str(i) for i in range(1, 11))) #改行なし、カンマ区切り、最後のカンマなし
    
# 課題4:リスト操作。[3, 1, 4, 1, 5, 9] というリストの昇順、合計値、要素数を求めるプログラムを書こう。

list = [3, 1, 4, 1, 5, 9]

print(sorted(list))
print(sum(list))
print(len(list))
