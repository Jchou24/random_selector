#coding=utf8
import random
import os
from bs4 import BeautifulSoup
from itertools import cycle
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

# ================================================================
TITLE = "Random Selector"
port = 5000

@app.route('/rs/')
def rs():
    return handler_core("Apple\nOrange\nBanana")

def handler_core(slot_candidate,title=TITLE):
    slot_candidate.strip()
    split_candidate = slot_candidate.split('\n')
    random.shuffle(split_candidate)
    split_candidate.append("")
    # print split_candidate
    render_coler = ["#FFCE29","#FFA22B","#FF8645","#FF6D3F","#FF494C","#FF3333","#FF0000"]
    cle = cycle(render_coler)
    slot_list = [ (idx+1,sc,cle.next()) for idx,sc in enumerate(split_candidate) ]
    # print slot_list

    # html = render_template('rs.html',slot_list=slot_list,slot_candidate=slot_candidate,title=title,debug_info=str(REDIS_URL))
    html = render_template('rs.html',slot_list=slot_list,slot_candidate=slot_candidate,title=title,port=port,debug_info=port)
    return html

@app.route('/rs/rs_handler/',methods=['POST'])
def rs_handler():
    slot_candidate = request.form['slot_candidate']
    title = request.form['title'] if request.form['title'] else TITLE
    html = handler_core(slot_candidate,title)
    soup = BeautifulSoup(html)
    body = str(soup.find("body"))
    # print html
    return body

@app.route('/rs/nccu_eat/')
def nccu_eat():
    slot_candidate = u"\n".join([u"45大街",u"華越",u"驚奇"])
    # slot_candidate = "\n".join(["d","s","a"])
    return handler_core(slot_candidate=slot_candidate,title="NCCU Restaurant Selector")
# ================================================================


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
