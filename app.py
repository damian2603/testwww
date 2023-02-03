from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    input_data = request.form['input_data']
    result = subprocess.run(['python', 'script.py', input_data], stdout=subprocess.PIPE)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
