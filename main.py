from flask import Flask
from routes import bp as routes
    
def setup_routes(app):
    app.register_blueprint(routes)
    return app


app = setup_routes(Flask(__name__))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',  port=5000)