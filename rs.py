#coding=utf8
import random
import os
from bs4 import BeautifulSoup
from itertools import cycle
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import flask
app = Flask(__name__)

# ================================================================
TITLE = "Random Selector"
port = 5000

@app.route('/rs/',methods=['GET'])
def rs():
    if request.method == 'GET' and request.args.get('opt'):
        slot_candidate = request.args.get('opt')
        # print [slot_candidate]
        if len(slot_candidate) > 0:
            slot_candidate = slot_candidate.replace("|","\n")
            # print [slot_candidate]
            return handler_core(slot_candidate)

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
    html = render_template('rs.html',slot_list=slot_list,slot_candidate=slot_candidate,title=title,base_url=request.base_url,debug_info=None)
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
    slot_candidate = u"\n".join([u"45大街",u"華越",u"金鮨"])
    return handler_core(slot_candidate=slot_candidate,title="NCCU Restaurant Selector")

@app.route('/rs/age3/ch/')
def age3_ch():
    slot_candidate = u"\n".join([u"英國",u"法國",u"德國",u"俄國",u"荷蘭",u"西班牙",u"葡萄牙",u"鄂圖曼",u"阿茲特克",u"易落魁",u"蘇族",u"中國",u"日本",u"印度"])
    return handler_core(slot_candidate=slot_candidate,title="Age 3 civilization Selector")

@app.route('/rs/age3/en/')
def age3_en():
    slot_candidate = u"\n".join([u"British",u"French",u"Germans",u"Russians",u"Dutch",u"Spanish",u"Portuguese",u"Ottomans",u"Aztec",u"Iroquois",u"Sioux",u"Chinese",u"Japanese",u"Indians"])
    return handler_core(slot_candidate=slot_candidate,title="Age 3 civilization Selector")

@app.route('/rs/age3y/',methods=['GET'])
def age3y():
    language = request.args.get('language')
    language = language if language else 'ch'

    if language == 'en':
        slot_list = [u"British",u"French",u"Germans",u"Russians",u"Dutch",u"Spanish",u"Portuguese",u"Ottomans",u"Aztec",u"Iroquois",u"Sioux",u"Chinese",u"Japanese",u"Indians"]
    if language == 'ch':
        slot_list = [u"英國",u"法國",u"德國",u"俄國",u"荷蘭",u"西班牙",u"葡萄牙",u"鄂圖曼",u"阿茲特克",u"易落魁",u"蘇族",u"中國",u"日本",u"印度"]

    slot_number = request.args.get('slot_number')
    slot_number = slot_number if slot_number and 1 <= int(slot_number) <= 4 else 1

    # font_size = 140 * ( 1.22 - 0.22 * float(slot_number) )
    # height = 200 * ( 1.15 - 0.15 * float(slot_number))
    font_size = 140 * 0.73 ** ( int(slot_number)-1 )
    height = 200 * 0.83 ** ( int(slot_number)-1 )

    return render_template('age3y.html',font_size=font_size,height=height,slot_list=slot_list,slot_number=slot_number,language=language)
# ================================================================


if __name__ == "__main__":
    # app.run(debug=True)

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
