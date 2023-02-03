from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    script = subprocess.Popen(['python', 'script.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = script.communicate()
    return "Script output: " + stdout.decode() + "\nError: " + stderr.decode()

if __name__ == '__main__':
    app.run(debug=True)
