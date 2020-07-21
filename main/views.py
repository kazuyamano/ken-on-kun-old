import flask 
from main import app, db
from main.models import Entry
from sqlalchemy import desc

@app.route('/')
def show_entries():
    entries = Entry.query.all() 
        #Entry  テーブル名
        #.query クエリ（指示）
        #.all() 全件取得
        #別の書き方: session.query(Entry).all()
    entries_head = Entry.query.order_by(desc(Entry.date)).limit(5).all()
        #.order_by()    並び順を指定
        #desc(Entry.date)   'date'カラムの降順
    return flask.render_template('entries.html', entries=entries, entries_head=entries_head)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(jcode = flask.request.form['jcode'],temp = flask.request.form['temp'])
    db.session.add(entry)
    db.session.commit()
    return flask.redirect(flask.url_for('show_entries'))
