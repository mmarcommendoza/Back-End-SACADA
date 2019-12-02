#!/usr/bin/env python-NEW OWNER
from pycomm.ab_comm.slc import Driver as SlcDriver
import logging
import threading
from timeit import default_timer as timer

import json
import random
import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

kk=0
kk2=0
kk3=1
start=0
eficiencia=0

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test-address")
def testAddress():
    global start
    global kk
    global kk2
    global kk3
    global eficiencia
    # p = SlcDriver()
    # if p.open('10.130.28.92'):
    #     kk = p.read_tag('C48:0.ACC') #contador
    #     kk2 = p.read_tag('C48:2.ACC') #contador acumulkado
    #     if kk2>=1: #start new code (everything with kk2 wo;; need to be replaced with new variable)
    #         if start==0 and kk3==1:
    #             start = timer()
    #             kk3=0 
    #         start2 = (timer()-start)/3600 
    #         eficiencia = (kk2/(1500*start2))*100
    #     kk3 = 0 #p.read_tag('B45:0', 11) #rest btn
    # p.close()
    #HTLM values
    x = {
        "address": "Test",
        "pre": kk,
        "contador_acumulado": kk2,
        "eficiencia": int (eficiencia)
    }

    return jsonify(x)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3001), debug=True)
