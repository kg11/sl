from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = "secret"



@app.route('/', methods=['GET', 'POST'])
def server():
    try:
        balance = session['balance']
        count = session ['count']
    except KeyError:
        balance = session['balance']=8000
        count = session['count'] = 0

    if request.method == "GET":
        msg = " "

    elif request.method == "POST":
        if session['count'] == 5:
            session.clear()
            balance = 8000
            count = 0
            msg = "5 transactions done"
        elif request.form['action'] == 'Deposit':
            balance = balance + int(request.form['amount'])
            count = count+1
            msg='Deposit Successful' 
        elif request.form['action'] == 'Withdraw':
            if int(request.form['amount']) > 5000:
                msg = "Cant Withdraw more than 5000"
            elif int(request.form['amount']) > balance:
                msg = "Cant Withdraw more than balance"
            else:
                balance = balance - int(request.form['amount'])
                count = count + 1
                msg = 'Withdraw Successful'

    session['balance'] = balance
    session['count'] = count            
    return render_template('index.html', balance = balance, msg = msg) 


if (__name__ == "__main__"):
    app.run(debug=True)