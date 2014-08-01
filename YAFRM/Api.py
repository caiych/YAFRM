import flask
import json
from flask.views import View,MethodView
from flask import request

class Api:
    def __init__(self,app):
        self.app = app
    def register(self,base_url,handle_obj,encode_func=json.dumps,decode_func=json.loads):
        def wrap(con):
            if type(con) == str:
                return con
            else:
                return encode_func(con)

        def get_all(self):
            print self.handle_obj.get_all
            res = self.handle_obj.get_all()
            return wrap(res)

        def delete_all(self):
            res = self.handle_obj.delete_all()
            return wrap(res)

        def create(self):
            print request.data,"!!"
            return wrap(self.handle_obj.create(decode_func(request.data)))

        def get(self,id):
            res = self.handle_obj.get(id)
            return wrap(res)
        
        def update(self,id):
            return wrap(self.handle_obj.update(id,decode_func(request.data)))

        def delete(self,id):
            return wrap(self.handle_obj.delete(id))

        checklist = [
                (
                    ('get',get_all), 
                    ('delete',delete_all),
                    ('post',create),
                    ),
                (
                    ('get',get),
                    ('put',update),
                    ('delete',delete),
                    )
                ]

        View = []
        i = 0
        for check in checklist:
            tmp = {'handle_obj':handle_obj}
            for to,frm in check:
                if hasattr(handle_obj,frm.__name__):
                    tmp[to] = frm
                i += 1
            View.append(type('View'+str(i),(MethodView,),tmp))
                

        self.app.add_url_rule(base_url+'/',view_func=View[0].as_view('V1'))
        self.app.add_url_rule(base_url+'/<id>/',view_func=View[1].as_view('V2'),methods=['GET','PUT','DELETE'])


