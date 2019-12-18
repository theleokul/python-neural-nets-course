# This line ask the application to import Flask module from flask package.
# Flask used to create instances of web application.
from flask import Flask

# This line create an instance of your web application. __name__ is a special variable in python,
# it will equal to “__main__” if the module(python file) being executed as the main program.
app = Flask(__name__)


# This line define the routes. For example if we set route to “/” like above,
# the code will be executed if we access localhost:5000/.
# You could set the route to “/hello” and our “hello world” will be shown if we access localhost:5000/hello
@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    # This line mean that your flask app will being run if we run from app.py.
    # Notice also that we are setting the debug parameter to true.
    # That will print out possible Python errors on the web page helping us trace the errors.
    app.run(debug=True)
