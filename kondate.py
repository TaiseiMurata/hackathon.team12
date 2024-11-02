from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# メニュー項目とそれぞれの価格を辞書で定義
menu_items = {
    "主食": [
        ("ごはん1杯", 110),
        ("食パン2枚", 130),
        ("うどん大盛り", 220),
        ("そば", 140),
        ("チャーハン", 220),
    ],
    "汁物": [
        ("味噌汁", 70),
        ("コーンスープ", 120),
        ("コンソメスープ", 130),
        ("トマトスープ", 110),
        ("豚汁", 140),
    ],
    "小鉢": [
        ("ひじきの豆の煮物", 140),
        ("漬物", 100),
        ("冷奴", 120),
        ("ポテトサラダ", 130),
        ("きんぴらごぼう", 110),
    ],
    "おかず": [
        ("熟成焼き魚", 250),
        ("ハンバーグサラダ", 350),
        ("エビフライ2本", 280),
        ("みそ鶏の照り焼き", 320),
        ("野菜たっぷりシチュー", 290),
    ],
    "飲み物": [
        ("烏龍茶", 100),
        ("オレンジジュース", 150),
        ("ブラックコーヒー", 200),
        ("抹茶ラテ", 180),
        ("レモネード", 160),
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
