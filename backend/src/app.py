from flask import Flask,request,make_response
import requests as req
import json
api_key = "475ed4e3ec47ac29afec98aa34919965"



def toDegCen(temp:float)->float:
    temp = temp - 273
    return temp


def gen_url(city:str)->str:
    url ="https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    return url


def get_city() -> str: #in testing we can patch thish with another function
    data =  request.args #returns a bite type
    args = args.to_dict()
    try:
        city = args["city"]
        return {"message" : city}
    except:
        return {"message" : "NULL"}

def get_param_from_request_json(fieldName : str) -> str:
    dataField = ''
    data = request.json
    if data.get(fieldName) != None:
        dataField = data.get(fieldName)
    
    return dataField

def create_app():
    app = Flask(__name__)

    @app.route("/test_json_data", methods = ['GET'])
    def test():
        data = get_param_from_request_json('test_param')
        resp = make_response()
        resp.data = data.encode()
        return resp

        
    @app.route("/",methods=["GET"])
    def index():
        resp = make_response()
        resp.data = b"ok"
        return resp




    @app.route("/get_weather", methods = ["GET"])
    def data():
       
        
        city = get_param_from_request_json('city')
        if len(city) == 0:
            return 
        

        url = gen_url(city=city)
        print (url)
        data_original = json.loads(req.get(url).text)
        if (data_original):
            data =(data_original)["main"]
            temp = toDegCen(data["temp"])
            feels_like = toDegCen(data["feels_like"])
            humidity = data["humidity"]
            wind = data_original["wind"]["speed"]
            in_short = data_original["weather"][0]["description"]

            obj = {
                "city":city,
                "in_short":in_short,
                "temp":temp,
                "feels_like":feels_like,
                "humidity":humidity,
                "wind":wind

            }
            return obj
    
    
    
    
    
    return app









app = create_app()


