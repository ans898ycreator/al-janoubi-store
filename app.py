from flask import Flask, render_template

app = Flask(__name__)

# 1. الصفحة الرئيسية للمتجر
@app.route('/')
def home():
    return render_template('index.html')

# صفحة عروض يلا لودو الرئيسية
@app.route('/yalla-ludo')
def yalla_ludo():
    return render_template('yalla_ludo.html')

# 2. صفحة شحن جواهر يلا لودو (الأيدي)
@app.route('/yalla-ludo-id')
def yalla_ludo_id():
    return render_template('yalla_ludo_id.html')

# 3. صفحة شحن جواهر يلا لودو (داخل الحساب)
@app.route('/yalla-ludo-account')
def yalla_ludo_account():
    return render_template('yalla_ludo_account.html')

# 4. صفحة شحن كوينزات يلا لودو
@app.route('/yalla-ludo-coins')
def yalla_ludo_coins():
    return render_template('yalla_ludo_coins.html')

# 5. صفحة تفعيل VIP يلا لودو
@app.route('/yalla-ludo-vip')
def yalla_ludo_vip():
    return render_template('yalla_ludo_vip.html')

# 6. صفحة تأمين رويال يلا لودو (الجديدة)
@app.route('/royal')
def royal_insurance():
    return render_template('yalla_ludo_royal.html')

if __name__ == '__main__':
    app.run(debug=True)