import json
from functools import wraps

def  to_json (func) :
	@wraps (func)
	def function(*args, **kwargs):
		return json.dumps(func(*args,**kwargs))
	return function 

@to_json
def get_data():
   return {'data':42}
  
get_data()