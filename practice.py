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

# 課題5:2つの数を受け取って「大きい方の数」を返す関数 max_number(a, b) を作ってみよう。

def max_number(a, b):
    return max(a, b) #大きい値を返す関数

num1 = float(input("１つめの数字を入力してね:"))
num2 = float(input("２つめの数字を入力してね:"))

print(max_number(num1, num2))

#リストver

numbers = [3, 7, 2, 10]
print(max(numbers))

# 課題6:文字列操作。ユーザーが入力した文字列を「全部大文字にする」「文字数を数える」「逆順にする」

def to_upper(word: str) -> str:
    return word.upper()

def count_length(word: str) -> int:
    return len(word)

def reverse_string(word: str) -> str:
    return word[::-1]

word1 = str(input("大文字にしたい文字を入力してね:"))
print(to_upper(word1))

word2 = str(input("文字数を数えたい文字列を入力してね:"))
print(count_length(word2))

word3 = input("並びを逆にしたい文字列を入力してね:")
print(reverse_string(word3))


