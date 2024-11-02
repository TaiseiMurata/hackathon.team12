from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# メニュー項目とそれぞれの価格を辞書で定義
menu_items = {  # 名前　価格　カロリーの順番です。
    "主食": [
        ("ごはん1杯", 110, 200),
        ("食パン2枚", 130, 210),
        ("うどん大盛り", 220, 220),
        ("そば", 300, 190),
        ("チャーハン", 450, 450),
        ("おにぎり", 120, 180),
        ("焼きおにぎり", 130, 200),
        ("ラーメン", 500, 500),
        ("カレーライス", 300, 600),
        ("パスタ", 400, 450)
    ],
    "汁物": [
        ("味噌汁", 70, 50),
        ("コーンスープ", 120, 100),
        ("コンソメスープ", 130, 80),
        ("トマトスープ", 110, 70),
        ("豚汁", 140, 120),
        ("ワカメスープ", 90, 40),
        ("クリームスープ", 130, 120),
        ("中華スープ", 100, 60),
        ("オニオンスープ", 110, 70),
        ("にんじんスープ", 120, 80)
    ],
    "小鉢": [
        ("ひじきと大豆の煮物", 140, 120),
        ("漬物", 100, 20),
        ("冷奴", 120, 100),
        ("ポテトサラダ", 130, 150),
        ("きんぴらごぼう", 110, 80),
        ("ナスのお浸し", 120, 50),
        ("カボチャの煮物", 130, 110),
        ("ほうれん草の胡麻和え", 110, 70),
        ("きゅうりの浅漬け", 100, 15),
        ("もやしナムル", 90, 30)
    ],
    "おかず": [
        ("熟成焼き魚", 250, 300),
        ("ハンバーグサラダ", 350, 400),
        ("エビフライ2本", 280, 350),
        ("みそ鶏の照り焼き", 320, 280),
        ("野菜たっぷりシチュー", 290, 320),
        ("唐揚げ", 300, 350),
        ("焼肉盛り合わせ", 700, 800),
        ("肉じゃが", 250, 250),
        ("天ぷら盛り合わせ", 350, 400),
        ("厚焼き玉子", 150, 200)
    ],
    "飲み物": [
        ("烏龍茶", 100, 0),
        ("オレンジジュース", 150, 120),
        ("ブラックコーヒー", 200, 5),
        ("抹茶ラテ", 180, 90),
        ("レモネード", 160, 100),
        ("アイスティー", 130, 30),
        ("ミルク", 120, 80),
        ("グレープフルーツジュース", 140, 110),
        ("ジンジャーエール", 150, 100),
        ("レモン水", 90, 10)
    ]
}


def select_menu(budget):
    selected_menu = {}
    total_price = 0
    error = None
    
    if budget < 100 : error = "予算内でメニューを選ぶことができませんでした。"
    
    for category, items in menu_items.items():
        affordable_items = [item for item in items if item[1] <= budget - total_price]
        if affordable_items:
            item, price = random.choice(affordable_items)
            selected_menu[category] = (item, price)
            total_price += price
        else:
            # error = "予算内でメニューを選ぶことができませんでした。"
            # selected_menu = {}
            # total_price = 0
            break
    
    return selected_menu, total_price, error

@app.route('/')
def index():
    # 初回アクセス時はメニューとエラーメッセージを空で渡す
    return render_template('kon.html', menu=None, total=0, error=None)

@app.route('/set_budget', methods=['POST'])
def set_budget():
    budget = int(request.form['budget'])  # ユーザーが入力した予算を取得
    selected_menu, total_price, error = select_menu(budget)
    
    return render_template('kon.html', menu=selected_menu, total=total_price, error=error)

if __name__ == '__main__':
    app.run(debug=True)
