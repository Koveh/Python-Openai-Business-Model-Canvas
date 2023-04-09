from flask import Flask, render_template, url_for
import json

app = Flask(__name__, template_folder='templates')

@app.route('/')
def bmc():
    with open("data/bmc.json") as f:
        bmc_data = json.load(f)
    return render_template('bmc.html', bmc=bmc_data)

if __name__ == '__main__':
    app.run(debug=True)