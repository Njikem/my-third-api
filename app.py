from flask import Flask, request, jsonify, make_response
from dbhelpers import run_statement
from helpers import check_endpoint_info

app = Flask(__name__)



#Philosopher

@app.get('/api/philosopher')
def get_philosopher(): 

    try: 
        results = run_statement("CALL get_philosopher()", [])
        print(results)
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except Exception as err:
        print(err)
        return make_response("f{err}", 400)
    

@app.post('/api/philosopher')
def insert_new_philosopher():
    valid_check = check_endpoint_info(request.json, ['name', 'bio', 'date_of_birth', 'date_of_death', 'image_url'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL insert_new_philosopher(?, ?, ?, ?, ?)", [request.json.get("name"), request.json.get("bio"), request.json.get("date_of_birth"), request.json.get("date_of_death"), request.json.get("image_url")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
   


#Quote


@app.get('/api/quote')
def get_quote():

    valid_check = check_endpoint_info(request.json, ["philosopher_id"])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL get_quote(?)", [request.json.get("philosopher_id")])
    if(type(results) == list):
       return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, Something went wrong"), 500)
    

@app.post('/api/quote')
def insert_quote():
    valid_check = check_endpoint_info(request.json, ["philosopher_id", "content"])
    print(valid_check)
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL insert_quote(?, ?)", [request.json.get("philosopher_id"), request.json.get("content")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
   










app.run(debug=True)