{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, jsonify\
import requests\
from bs4 import BeautifulSoup\
\
app = Flask(__name__)\
\
@app.route("/postal/<code>")\
def postal_lookup(code):\
    url = f"https://www.codigo-postal.pt/\{code\}/"\
    response = requests.get(url)\
    soup = BeautifulSoup(response.text, "html.parser")\
\
    rows = soup.select("table tbody tr")\
    results = []\
\
    for row in rows:\
        cols = row.find_all("td")\
        if len(cols) >= 3:\
            address = cols[0].text.strip()\
            try:\
                lat = float(cols[1].text.strip())\
                lng = float(cols[2].text.strip())\
                results.append(\{"address": address, "coords": [lat, lng]\})\
            except ValueError:\
                continue\
\
    return jsonify(results)\
}