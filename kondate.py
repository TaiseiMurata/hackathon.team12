from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# メニュー項目とそれぞれの価格を辞書で定義
menu_items = {
    "主食": [("ご飯", 100), ("パン", 150), ("うどん", 150)],
    "汁物": [("味噌汁", 70), ("スープ", 120), ("コンソメスープ", 130)],
    "小鉢": [("サラダ", 150), ("おひたし", 100), ("冷奴", 120)],
    "おかず": [("焼き魚", 250), ("ハンバーグ", 350), ("エビフライ", 280)],
    "飲み物": [("お茶", 100), ("ジュース", 150), ("コーヒー", 200)]
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
