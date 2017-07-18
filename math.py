import json

def index(req, a, b, mode):
	
    try:
	
        success = True
    
        if mode == 'add':
            result = int(a) + int(b)

        if mode == 'sub':
            result = int(a) - int(b)

    except ValueError:

        success = False
        result = None	
  
    return_info = ({'result' : result, 'success' : success})
    
    return json.dumps(return_info)