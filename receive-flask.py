from flask import Flask, request, redirect, render_template, url_for
from flask_mail import Mail, Message
import send
from flask import send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        number = request.form['phone']
        print("POST", str(number))
        send.send_sms(number)
        # return render_template('index2.html',)
        return redirect("https://www.myflexigift.com/standby.html#/", code=302)
    else: 
        return render_template('index2.html',)

if __name__ == '__main__':
    app.run(port=3000)
