import flask 
from flask import request
from main import app, db
from main.models import Entry
from sqlalchemy import desc
import datetime

@app.route('/', methods=['get'])
def show_entries():
    entries_head = Entry.query\
        .order_by(desc(Entry.date))\
        .limit(5)\
        .all()
    return flask.render_template('entry.html', entries_head=entries_head)

@app.route('/added', methods=['POST'])
def add_entry():
    entry= Entry(\
        jcode=flask.request.form['jcode']\
        ,temp=flask.request.form['temp']\
        ,date =datetime.datetime.now())
    db.session.add(entry)
    db.session.commit()
    added_jcode = request.form.get('jcode')
    added_result = db.session.query(Entry)\
        .filter(Entry.jcode == added_jcode)\
        .order_by(desc(Entry.date))\
        .limit(10)\
        .all()
    return flask.render_template('added.html', added_jcode=added_jcode, added_result=added_result)

@app.route('/logs-specify', methods=['get'])
def specify_logs():
    return flask.render_template('logs-specify.html')

@app.route('/logs-result', methods=['post'])
def sort_logs():
    specified_jcode = request.form.get('jcode') 
    sorted_result = db.session.query(Entry)\
        .filter(Entry.jcode == specified_jcode)\
        .order_by(desc(Entry.date))\
        .all()
    return flask.render_template('logs-result.html', specified_jcode=specified_jcode, sorted_result=sorted_result)



# SQLクエリの書き方
# 本来の記述はsessionを使う。           db.session.query(Entry).all()
# 'Entry'クラスが持つヘルパー機能のため   Entry.query.all() 　に省略可能
#   'Entry'         クラス名＝テーブル名
#   .query          クエリ（指示）
#   .order_by()     並び順を指定
#   desc(Entry.date)    'date'カラムの降順で
#   .all()          全件取得