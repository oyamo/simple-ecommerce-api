from . import app
from flask import jsonify, request
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError, MethodNotAllowed, BadRequest
import json
# Custom App Error Handler
class EcommerceException(Exception):
    """Evokes custom error and returns it to the consumer in json format"""
    def __init__(self, name = None, description=None):
        super(Exception,self).__init__()
        self.name = name
        self.description = description



def handleException(err):
    code = 500
    url = request.url
    data = {'status':500, 'error':{
        'url':url,
        'code':code
    }}
    
    if isinstance(err, (HTTPException, NotFound, InternalServerError, MethodNotAllowed)):
        code = err.code
        name = err.name
        description = err.description
        data['status'] = code
        data['error']['name'] = name
        data['error']['code'] = code
        data['error']['description'] = description
    elif isinstance(err, EcommerceException):
        data['error']['name'] = err.name
        data['error']['description'] = err.description
    else:
        data['error']['name'] = 'Internal Server Error'
        data['error']['code'] = code
        data['error']['description'] = 'Server Error beyond API client scope'
    
    return jsonify(data)

app.register_error_handler(HTTPException, handleException)
app.register_error_handler(NotFound, handleException)
app.register_error_handler(InternalServerError, handleException)
app.register_error_handler(MethodNotAllowed, handleException)
app.register_error_handler(BadRequest, handleException)
app.register_error_handler(EcommerceException, handleException)

