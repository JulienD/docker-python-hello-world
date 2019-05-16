from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():    
	html = "<h3>Hello {name}!</h3>" \
           "<p>Flask inside Docker!</p>"
	return html.format(name=os.getenv("NAME", "World"))    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
