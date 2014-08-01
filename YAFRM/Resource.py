

class Resource:
    def __init__(self,encode_func=json.dumps,decode_func=json.loads):
        self.encode_func = encode_func
        self.decode_func = decode_func

    def __metaclass__(classname,parents,classattr):
        return type(
                classname,parents,classattr.update({
                    'get'
                    })
                )
