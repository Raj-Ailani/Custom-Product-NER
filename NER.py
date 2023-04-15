import spacy
import flask
from flask import jsonify,request

app = flask.Flask(__name__)

@app.route('/getproducts',methods=["POST"])
def get_all_item():
    nlp = spacy.load("output/model-last/")
    sentence = request.json['sentence']
    doc =nlp(sentence)
    output = []
    for ent in doc.ents:
        output.append(ent.text)
        
    output = jsonify(output)
    return output

if __name__ == '__main__':
    app.run(debug=True)