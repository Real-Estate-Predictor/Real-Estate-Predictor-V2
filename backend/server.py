from flask import Flask
app = Flask(__name__)
from project.controllers import predict, home

def register_blueprints(app):
    # app.register_blueprint(user.user_bp, url_prefix='/user')
    # app.register_blueprint(houseData.houseData_bp, url_prefix='/houseData')
    app.register_blueprint(predict.predict_bp, url_prefix='/predict')
    app.register_blueprint(home.home_bp, url_prefix='/home')

    print('blueprints register successfully')

################################

try:
    register_blueprints(app)
    # print(app.url_map) # for debugging path
except Exception as e:
    print('ERROR - Cannot register blueprint')
    print(e)

################################

if __name__ == '__main__':
    app.run(port=8000, debug=True)