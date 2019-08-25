from __future__ import unicode_literals
from flask import Flask, request, jsonify, send_file, send_from_directory, safe_join, abort
import youtube_dl
import os
 
dirpath = os.getcwd()

app = Flask(__name__)

@app.route('/')
def easter_egg():
    return 'WWWWWOOOOOWWWWWW, you found it. LOL.....'

@app.route('/ripper',methods=['POST'])
def ripper_post():
    content = request.json
    url = content['url']
    id = getUrlId(url)
    run_youtube(url,id)
    return send_from_directory(dirpath,filename=id+'.mp4', as_attachment=True)

@app.route('/ripper/<id>')
def ripper_get(id):
    url = 'https://www.youtube.com/watch?v='+id
    run_youtube(url,id)
    return send_from_directory(dirpath,filename=id+'.mp4', as_attachment=True)

def getUrlId(url):
    start = url.index('v=')+2
    end = url.index('&',start) if url.index('&',start)>=0 else len(url)
    return url[start:end]


def run_youtube(url,id):
    ydl_opts = {'outtmpl':id+'.mp4'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])