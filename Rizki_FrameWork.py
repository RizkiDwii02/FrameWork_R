from flask import Flask, render_template, request

app = Flask(__name__)
nama = 'Rizki'
app_name = 'For Cules'

@app.route('/')
def home():
    return f"Welcome to {app_name}!"
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)

@app.route('/data')
def data():
    user = {"name": "Lamine", "age": 17, "city": "Barcelona"}
    return render_template('data.html', user=user)

@app.route('/squad')
def squad():
    squad_list = ["Lewa", "Rapha", "Lamine", "Pedri"]
    return render_template('squad.html', squad=squad_list)

@app.route('/pengguna')
def pengguna():
    user_list = [
        {"name": "Lewa", "role": "admin"},
        {"name": "Rapha", "role": "user"},
        {"name": "Lamine", "role": "admin"},
        {"name": "Pedri", "role": "user"},
    ]
    return render_template('users.html', pengguna=user_list)

@app.route('/rating/<int:score>')
def rating(score):
    return render_template('rating.html', score=score)

@app.route('/team')
def team():
    daftar_team = [
        {"nama": "Barca", "rating": 92},
        {"nama": "Madrid", "rating": 80},
        {"nama": "City", "rating": 65},
        {"nama": "Mu", "rating": 55},
    ]
    return render_template('team.html', team=daftar_team)

if __name__ == "__main__":
    app.run(debug=False)
