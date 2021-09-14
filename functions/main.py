from flask import Flask, request, json
from flask import Flask, request
import pickle

model_file = 'model/decision_tree.pkl'

def make_prediction(request):
    # carregando modelo
    model = pickle.load(open(model_file,"rb"))

    #recebendo o Post
    data =  request.get_json(force=True)

    #x = np.array(data["data"]).reshape(1,2)
    print(data)
    x = [data["data"]]
    #fazendo a predicao
    
    prediction = model.predict(x)[0]
    result = {"result": prediction}

    return json.dumps(result)

def main():
    app = Flask(__name__)
    app.route('/',methods=["POST"])(lambda:make_prediction(request))
    app.run(debug=True)

if __name__ == '__main__':    
    main()

