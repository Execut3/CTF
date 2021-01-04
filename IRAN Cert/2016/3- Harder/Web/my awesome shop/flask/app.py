#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for, render_template_string, make_response, current_app 
from flaskext.mysql import MySQL
import urlparse
import binascii

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'my_awesome_shop_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'secret_password'
app.config['MYSQL_DATABASE_DB'] = 'my_awesome_shop_db'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
flag2 = 'APACTF{!f_there_were_no_character_limits_you_m4y_even_get_a_remote_sh3ll_on_my_server!}'


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        cur = mysql.connect().cursor()
        cur.execute('''SELECT username FROM auth_user''')
        rv = cur.fetchall()
        cur.close()
    except:
        print 'Exception happened in index function'
    return render_template('index.html')


@app.route('/update-budget', methods=['POST'])
def update_budget():
    if request.method == 'POST':
        try:
            username = request.form['username']
            identifier = request.form['identifier']
            budget = request.form['budget']
            try:
                int(budget)
                if not budget or not username or not identifier:
                    return "Error in input..."
            except:
                return "Not valid parameters"
    
            db = mysql.connect()
            cur = db.cursor()
            cur.execute('''SELECT id FROM auth_user WHERE username=%s''', (username))
            rv = cur.fetchall()
            
            if rv:
                try:
                    id = int(rv[0][0])
                except:
                    db.close()
                    return redirect(url_for('index'))
    
                query = (
                        "UPDATE app_shopuser SET budget=%s WHERE identifier=%s AND user_id=%s"
                    )
                data = (str(budget), str(identifier), str(id))
                cur.execute(query, data)
                rv = cur.fetchall()
            db.commit()
            db.close()
        except:
            print "Exception happened in update_budget function"
    return redirect(url_for('index'))


@app.route('/comments', methods=['GET'])
def comments():
    try:
        db = mysql.connect()
        cur = db.cursor()
        query = (
            "SELECT comments_comment.id, auth_user.username, comments_comment.content FROM auth_user "
            "INNER JOIN comments_comment ON auth_user.id=comments_comment.user_id "
            "WHERE comments_comment.active=false")
        data = ()
        cur.execute(query, data)
        rv = cur.fetchall()
        db.close()
        comments = []
        for r in rv:
            comments.append({'id': str(r[0]), 'username': str(r[1]), 'comment': str(r[2])})
    except:
        print "Exception happened in comments function"
    return render_template('comments.html', comments=comments)


@app.route('/comment/view', methods=['GET'])
def view_comment():
    db = mysql.connect()
    cur = db.cursor()
    try:
        id = request.args.get('id', 0)
        id = int(id)

        query = (
            "SELECT content FROM comments_comment WHERE id=%s"
            )
        data = (id)
        cur.execute(query, data)
        rv = cur.fetchall()
        if rv:
            comment = rv[0][0]
            query = (
                "UPDATE `comments_comment` SET `active`=1 WHERE `id`=%s"
                )
            data = (id)
            cur.execute(query, data)
            db.commit()
            return render_template('comment.html', comment=comment)
    except:
        print 'Execption happened'
        pass
    db.close()
    return redirect(url_for('comments'))


@app.route('/users/view', methods=['GET'])
def users_view():
    db = mysql.connect()
    cur = db.cursor()
    query = (
            "SELECT alias, identifier, budget FROM app_shopuser"
            )
    cur.execute(query)
    rv = cur.fetchall()
    users = []
    for r in rv:
        try:
            users.append("<td id=\"{0}\">'alias': {1}, 'budget': {2}, 'identifier': {3}</td>".format(r[1][:8], r[0], r[2],r[1][:8]))
        except:
            continue
    template = "<html><head></head><body><div><h1>List of registered users in my shop</h1>%s</div></body></html>"
    if users:
        template = template % '<br>'.join(users)
    else:
        template = template % '<br> No user found<br>'
    db.close()
    return render_template_string(template, **globals())


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
