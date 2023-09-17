import pyperclip
import re
import math


def classic():
    paste_text = pyperclip.paste()
    result_text = (
        paste_text.replace("-", "")
        .replace("#", "")
        .replace(" ", "")
        .replace("\n", "")
        .replace("\r", "")
        .replace("\t", "")
        .replace(">", "")
        .replace("", "")
    )
    print("\n合計文字数　　　　　：" + str(len(result_text)) + "\n")

    hirakana = re.sub("[^\u3041-\u309F\u30A1-\u30FF]", "", result_text)
    hirakana_percent = len(hirakana) / len(result_text)
    print("ひらカナ使用率　　　：" + str("{:.0%}".format(hirakana_percent)))

    kanji = re.sub("[^\u4E00-\u9FFF]", "", result_text)
    kanji_percent = len(kanji) / len(result_text)
    print("漢字使用率　　　　　：" + str("{:.0%}".format(kanji_percent)))

    alphabet = re.sub("[^\u0041-\u007A]", "", result_text)
    alphabet_percent = len(alphabet) / len(result_text)
    print("アルファベット使用率：" + str("{:.0%}".format(alphabet_percent)))

    kigou = re.sub(
        "[\u3041-\u309F\u30A1-\u30FF\u4E00-\u9FFF\u0041-\u007A]", "", result_text
    )
    kigou_percent = len(kigou) / len(result_text)
    print("記号使用率　　　　　：" + str("{:.0%}".format(kigou_percent)) + "\n")

    if kanji_percent <= 0.19:
        print("漢字が少ないよ\n")

    elif kanji_percent >= 0.20 and kanji_percent <= 0.30:
        print("漢字率がちょうどいいよ\n")

    else:
        print("漢字が多いよ\n")


# パスを取得・開く
file_path = "D:\Git\hoshipaso\Archive\dictionary_choice.md"
print(file_path)
with open(file_path, encoding="utf-8") as f:
    text = f.read()

# 文字数カウント
print(f"合計文字数：{len(text)}文字")

hirakana = re.sub("[^\u3041-\u309F\u30A1-\u30FF]", "", text)
hirakana_percent = math.floor(len(hirakana) / len(text) * 100)
print(f"ひらカナ使用率：{hirakana_percent}%")
