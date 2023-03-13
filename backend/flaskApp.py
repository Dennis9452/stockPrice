from flask import Flask, jsonify, request, abort
from flask import render_template,redirect, json
from flask_cors import CORS
from flask.helpers import url_for
import traceback
import sys
from flask_sslify import SSLify
from nbaStats import NBAstats
from finance import StockPricing
from werkzeug.exceptions import HTTPException

# app = Flask(__name__, static_url_path='')
stats = NBAstats
DEBUG = True
 
app = Flask(__name__,static_url_path='')
# app.config.from_object(__name__)
# app.config['PREFERRED_URL_SCHEME'] = 'https'
CORS(app)

@app.route("/")
def home():
    print("home")
    # return jsonify('index!')
    return render_template("/index.html")

@app.route("/vue")
def vue():
    # return app.send_file("vueIndex.html")
    return app.send_static_file("index.html")

@app.route('/api/ping', methods=['GET'])
def ping_pong():
    # return app.send_file("index.html")
    return jsonify('flask!')

@app.route('/<path:fallback>')
def fallback(fallback):       # Vue Router 的 mode 为 'hash' 时可移除该方法
    if fallback.startswith('css/') or fallback.startswith('js/')\
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')


@app.route("/log", methods=['GET'])
def log():
    with open('logger.txt', 'a') as f:
        input = request.args['input']
        print(input)
        f.writelines('\n')
        f.writelines(input)
    
    f.close()
    print()
    return ""

@app.route("/channel/log/<accID>/<cdnName>/<channelNum>/<ProjectNum>/<UA>", methods=['GET','POST'])
def channelLog(accID,cdnName,channelNum,ProjectNum,UA):
    with open('channelLog.txt', 'a') as f:
        input="||"+accID+","+cdnName+","+channelNum+","+ProjectNum+","+UA;
        print(input)
        f.writelines('\n')
        f.writelines(input)

    f.close()
    print()
    return ""  

@app.route("/ppn")
def ppn():
    return render_template("/ppn.html")

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route("/realPrice", methods=['GET'])
def realPrice():
    print(request)
    sp = StockPricing()
    response = jsonify(sp.getPrice(''))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/addPrice", methods=['POST'])
def addPrice():
    print("x",request)
    if request.method == 'POST':
        print(request.get_json())
        stockId = request.get_json()['id']
    sp = StockPricing()
    try:
        return jsonify(sp.modifiedStockList("add", int(stockId)))
    except Exception as e:
        return abort_msg(e)
    
    

@app.route("/removePrice", methods=['POST'])
def removePrice():
    if request.method == 'POST':
        print(request.get_json())
        stockId = request.get_json()['id']
    sp = StockPricing()
    
    return jsonify(sp.modifiedStockList("remove", stockId))

@app.route("/getPlayer", methods=['GET'])
def getPlayer():
    result = stats.getPlayer( stats.getStats() ).tolist()
    return jsonify(player=result)

@app.route('/getStats', methods=['POST','GET'])
def getStats():
    if request.method == 'POST':
        playerList = request.get_json();
        print(playerList)
        result = stats.getTable( playerList['player'], stats.getStats()).values.tolist()
        
    return jsonify(result=result)

def abort_msg(e):
    """500 bad request for exception

    Returns:
        500 and msg which caused problems
    """
    error_class = e.__class__.__name__ # 引發錯誤的 class
    detail = e.args[0] # 得到詳細的訊息
    cl, exc, tb = sys.exc_info() # 得到錯誤的完整資訊 Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1] # 取得最後一行的錯誤訊息
    fileName = lastCallStack[0] # 錯誤的檔案位置名稱
    lineNum = lastCallStack[1] # 錯誤行數 
    funcName = lastCallStack[2] # function 名稱
    # generate the error message
    errMsg = "Exception raise in file: {}, line {}, in {}: [{}] {}. Please contact the member who is the person in charge of project!".format(fileName, lineNum, funcName, error_class, detail)
    # return 500 code
    abort(500, "fail to find target")

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8800)
    # from werkzeug.middleware.proxy_fix import ProxyFix
    # app.wsgi_app = ProxyFix(app.wsgi_app)
    # app.run()
    # app.run(debug=True,host="0.0.0.0",ssl_context=('server.crt', 'server.key'))