from flask import Flask, render_template
from routes.user_bp import user_bp
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config')
db = MySQL(app)

app.register_blueprint(user_bp, url_prefix='/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
 