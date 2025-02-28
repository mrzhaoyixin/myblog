import os
import sys
from flask import Flask
def create_app(test_config=None):
    #print("creating an app...")
    #create and configure the app
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='123456',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
            )
    
    if test_config is None:
        #Load the instance config ,if it exists, when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        #Load the test config if passed in
        app.config.from_mapping(test_config)
    
    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    #a simple page that say hello
    @app.route('/hello')
    def hello():
        return 'Hello'
    from .views import db
    db.init_app(app)
    print("database inited....")
    from .views import auth
    app.register_blueprint(auth.bp)
    from .views import blog
    #导入蓝图并注册
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    print("app created....")
    return app
