from flask import Flask, render_template, request

app = Flask(__name__)

PORT=5001

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            message = "Fields cannot be empty"
        elif username == "admin" and password == "1234":
            message = "Login Successful"
        else:
            message = "Invalid Credentials"

    return f"""
    <html>
    <body>
        <h2>Login Form</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
        <p>{message}</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT, debug=True)