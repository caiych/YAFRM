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

    def delete(sefl,id):
        return 'delete'+str(id)

api.register('/note',Resource())

app.run(debug=True)
