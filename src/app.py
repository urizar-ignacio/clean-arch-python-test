from flask import Flask
from flask_restful import Api

from src.gateway.endpoint import Department, HiredEmployee, Jobs

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!</p>"

api.add_resource(Department, '/api/departments/')
api.add_resource(HiredEmployee, '/api/hired_employees/')
api.add_resource(Jobs, '/api/jobs/')

if __name__ == "__main__":
    app.run(debug=True)
