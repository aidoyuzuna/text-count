import re
import math


# Morkdown記号除外
def markdown(md):
    md_text = (
        md.replace("-", "")
        .replace("#", "")
        .replace(" ", "")
        .replace("\n", "")
        .replace("\r", "")
        .replace("\t", "")
        .replace(">", "")
        .replace("", "")
    )
    return md_text


# テキストカウント
def text_count(tc):
    print(f"合計文字数：{len(tc)}文字")


# ひらがな・カタカナ使用率計算
def hirakana(hk):
    hirakana_text = re.sub("[^\u3041-\u309F\u30A1-\u30FF]", "", hk)
    hirakana_percent = math.floor(len(hirakana_text) / len(hk) * 100)
    print(f"ひらカナ使用率：{hirakana_percent}%")


# 漢字使用率
def kanji(ks):
    kanji_text = re.sub("[^\u4E00-\u9FFF]", "", ks)
    kanji_percent = math.floor(len(kanji_text) / len(ks) * 100)
    print(f"漢字使用率：{kanji_percent}%")

    if kanji_percent <= 0.19:
        print("漢字が少ないよ")

    elif kanji_percent >= 0.20 and kanji_percent <= 0.30:
        print("漢字率がちょうどいいよ")

    else:
        print("漢字が多いよ")


# パスを取得・開く
file_path = "D:\Git\hoshipaso\Archive\dictionary_choice.md"
print(file_path)
with open(file_path, encoding="utf-8") as f:
    text = f.read()

# Markdown記号処理
result_text = markdown(text)

# カウント処理
text_count(result_text)
hirakana(result_text)
kanji(result_text)
