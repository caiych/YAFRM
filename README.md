YAFRM
=====

Yet Another Flask-Restful Module

Use semantic function names to construct RESTFUL api.


##Example

~~~.python
import flask
from YAFRM import Api

app = flask.Flask(__name__)
api = Api(app)

class Resource:
    def get_all(self):
        return 'get_all'

    def delete_all(self):
        return 'delete_all'

    def create(self,obj):
        return 'create'+str(obj)

    def get(self,id):
        return 'get'+str(id)

    def update(self,id,obj):
        return 'update'+str(id)+str(obj)

    def delete(self,id):
        return 'delete'+str(id)

api.register('/baseurl',Resource())

app.run(debug=True)
~~~

##A little explaination

`Api` object take a `Flask application` object to construct.

Call the `register` method of `Api` object to register 
URL for a resource.

`register` method is like this:

~~~.python
def register(self,base_url,handle_obj,encode_func=json.dumps,decode_func=json.loads):
~~~

If the method of your `handle_obj` does not return a string,
then we pass it to `encode_func` to construct a string to return to the client.

And `decode_func` is used to parse the body of the HTTP body and pass it to 
your `handle_obj` method.


