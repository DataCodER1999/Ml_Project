from flask import Flask
app = Flask(__name__)
@app.route('/',['GET','POST'])
def index():
    return " This Is My First ML Project"
if __name__ == '__main__':
    app.run(debug=True);