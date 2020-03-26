# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/163b859q167BRNMQAe4kMyiqeQJr4MQj4
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
# prediction function 
def ValuePredictor(to_predict_list): 
	to_predict = np.array(to_predict_list).reshape(1,-1)
	print(to_predict)
	loaded_model = pickle.load(open("model.pkl", "rb")) 
	result = loaded_model.predict(to_predict) 
	return result[0] 

@app.route('/predict', methods = ['POST']) 
def predict(): 
	if request.method == 'POST': 
		to_predict_list = request.form.to_dict()
		to_predict_list = list(to_predict_list.values())
		to_predict_list = to_predict_list[:-1]
		to_predict_list=list(map(float, to_predict_list))
		result = ValuePredictor(to_predict_list)		 
		if int(result)== 1: 
			prediction ='cancer'
		else: 
			prediction ='Income less that 50K'			
		return render_template("index.html", prediction_text =prediction) 


    
        

if __name__ == "__main__":
    app.run(debug=True)

