from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
      <form action="/" method="POST">
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
		<label for="rot"> Rotate by: </label>
		   <input type="text" name="rot" value="0"/>
		   <!input type="textarea" name ="text"/>
           <textarea  name="text" id="text"> </textarea>
		   <input type="submit" value="Submit Query">
      </form>
    </head>
    <body>
      <!-- create your form here -->
    </body>
</html>
"""

@app.route("/", methods=['GET'])
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot= int(request.form['rot'])
    text= request.form['text']
    cipher= "<h1>"+rotate_string(text,rot)+"</h1>"

    return cipher
app.run()