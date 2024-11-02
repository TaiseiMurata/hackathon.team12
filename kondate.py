from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# メニュー項目とそれぞれの価格を辞書で定義
menu_items = {
    "主食": [
        {"name": "ごはん1杯", "price": 110, "calories": 200, "nutrients": {"protein": 4, "carbs": 45, "fat": 1}},
        {"name": "食パン2枚", "price": 130, "calories": 210, "nutrients": {"protein": 6, "carbs": 40, "fat": 3}},
        {"name": "うどん大盛り", "price": 220, "calories": 220, "nutrients": {"protein": 7, "carbs": 40, "fat": 1}},
        {"name": "そば", "price": 140, "calories": 190, "nutrients": {"protein": 6, "carbs": 41, "fat": 0.8}},
        {"name": "チャーハン", "price": 220, "calories": 450, "nutrients": {"protein": 8, "carbs": 70, "fat": 20}},
    ],
    "汁物": [
        {"name": "味噌汁", "price": 70, "calories": 50, "nutrients": {"protein": 3, "carbs": 6, "fat": 1}},
        {"name": "コーンスープ", "price": 120, "calories": 100, "nutrients": {"protein": 2, "carbs": 22, "fat": 3}},
        {"name": "コンソメスープ", "price": 130, "calories": 80, "nutrients": {"protein": 1, "carbs": 5, "fat": 4}},
        {"name": "トマトスープ", "price": 110, "calories": 70, "nutrients": {"protein": 2, "carbs": 14, "fat": 1}},
        {"name": "豚汁", "price": 140, "calories": 120, "nutrients": {"protein": 4, "carbs": 8, "fat": 5}},
    ],
    "小鉢": [
        {"name": "ひじきの豆の煮物", "price": 140, "calories": 120, "nutrients": {"protein": 7, "carbs": 18, "fat": 5}},
        {"name": "漬物", "price": 100, "calories": 20, "nutrients": {"protein": 1, "carbs": 4, "fat": 0}},
        {"name": "冷奴", "price": 120, "calories": 100, "nutrients": {"protein": 8, "carbs": 5, "fat": 4}},
        {"name": "ポテトサラダ", "price": 130, "calories": 150, "nutrients": {"protein": 3, "carbs": 20, "fat": 8}},
        {"name": "きんぴらごぼう", "price": 110, "calories": 80, "nutrients": {"protein": 2, "carbs": 12, "fat": 2}},
    ],
    "おかず": [
        {"name": "熟成焼き魚", "price": 250, "calories": 300, "nutrients": {"protein": 25, "carbs": 0, "fat": 20}},
        {"name": "ハンバーグサラダ", "price": 350, "calories": 400, "nutrients": {"protein": 30, "carbs": 15, "fat": 25}},
        {"name": "エビフライ2本", "price": 280, "calories": 350, "nutrients": {"protein": 20, "carbs": 20, "fat": 18}},
        {"name": "みそ鶏の照り焼き", "price": 320, "calories": 280, "nutrients": {"protein": 30, "carbs": 8, "fat": 14}},
        {"name": "野菜たっぷりシチュー", "price": 290, "calories": 320, "nutrients": {"protein": 25, "carbs": 10, "fat": 22}},
    ],
    "飲み物": [
        {"name": "烏龍茶", "price": 100, "calories": 0, "nutrients": {"protein": 0, "carbs": 0, "fat": 0}},
        {"name": "オレンジジュース", "price": 150, "calories": 120, "nutrients": {"protein": 2, "carbs": 28, "fat": 0}},
        {"name": "ブラックコーヒー", "price": 200, "calories": 5, "nutrients": {"protein": 0, "carbs": 0, "fat": 0}},
        {"name": "抹茶ラテ", "price": 180, "calories": 90, "nutrients": {"protein": 4, "carbs": 12, "fat": 3}},
        {"name": "レモネード", "price": 160, "calories": 100, "nutrients": {"protein": 1, "carbs": 25, "fat": 0}},
    ]
}

@app.route('/')
def index():
    # 初回アクセス時はメニューとエラーメッセージを空で渡す
    return render_template('kon.html', menu=None, total=0, error=None)

@app.route('/set_budget', methods=['POST'])
def set_budget():
    budget = int(request.form['budget'])  # ユーザーが入力した予算を取得
    
    # 予算内でランダムにメニューを選択する
    selected_menu = {}
    total_price = 0
    error = None
    
    for category, items in menu_items.items():
        affordable_items = [item for item in items if item[1] <= budget - total_price]
        if affordable_items:
            item, price = random.choice(affordable_items)
            selected_menu[category] = (item, price)
            total_price += price
        else:
            error = "予算内でメニューを選ぶことができませんでした。"
            selected_menu = {}
            total_price = 0
            break
    
    return render_template('kon.html', menu=selected_menu, total=total_price, error=error)

if __name__ == '__main__':
    app.run(debug=True)
