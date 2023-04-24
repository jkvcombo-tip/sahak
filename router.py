from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getRouter():
    return{'R1':'192.168.10.1', 'R2':'192.168.10.2', 'R3':'192.168.10.3'}

if __name__ == "__main__":
    app.run()