from flask import Flask, render_template
from P4 import P4, P4Exception

app = Flask(__name__)

@app.route('/sync')
def sync():
    p4 = P4()

    try:
        p4.connect()
        p4.run_sync()
    except P4Exception:
        print "\n".join(p4.errors)
        return "Error:\n" + "\n".join(p4.errors)

    return "Sync'd"

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
