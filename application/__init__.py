# initial / index file

from flask import Flask

app = Flask(__name__)
app.run(debug=True)

# to import routes.py
from application import routes    