# Python Flask

This is the first lesson in the workshop to get you familar with Python Flask

## Hello World

This is the obligatory 'Hello World' program in Flask. It is a simple service which only has one route and says 'Hello World'

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
```

That's how easy it is to build a web service using Flask. You can run it with:

```sh
  flask run -h 0.0.0.0
```

**Note:** because we are working in a Virtual Machine we must pass the parameter `-h 0.0.0.0` to Flask to make it bind to all network adapters so that the ports we forwarded in the `Vagrantfile` will work from our host computer. Otherwise Flask will only bind to the `loopback 127.0.0.1` adapter and will not be accessible outside of the VM.

You should see:

```l
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Now open a brower to http://localhost:5000 and you will see `Hello World`

## JSON Hello World

RESTful services exchange data using XML or JSON. Let's modify the service to send back JSON data instead of text.

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/hello')
def hello():
    return jsonify(name='hello', version='1.0', message='Hello World')
```

We have added a second route `/hello` that returns the following JSON when called:

```
{
  message: "Hello World",
  name: "hello",
  version: "1.0"
}
```

Try it: http://localhost:5000/hello

You can see how easy it is to startb building an API using Flask.
