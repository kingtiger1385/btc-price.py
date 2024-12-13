from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# تابعی برای دریافت قیمت بیت‌کوین از API
def get_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'  # API برای دریافت قیمت بیت‌کوین
    response = requests.get(url)  # ارسال درخواست به API
    data = response.json()  # دریافت داده‌ها به فرمت JSON
    price = data['bpi']['USD']['rate']  # استخراج قیمت بیت‌کوین به دلار
    return price

# مسیر روت اصلی (صفحه HTML)
@app.route('/')
def home():
    return render_template('index.html')  # بارگذاری صفحه اصلی

# مسیر برای دریافت قیمت بیت‌کوین (API)
@app.route('/get_price')
def get_price():
    price = get_bitcoin_price()  # دریافت قیمت بیت‌کوین
    return jsonify({'price': price})  # بازگرداندن قیمت به صورت JSON

if __name__ == '__main__':
    app.run(debug=True)
