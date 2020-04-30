from flaskr import create_app
#import config
print(__name__)
app = create_app()
if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
