import base64
import time
from selenium import webdriver
import MySQLdb

# import mechanize
# from ghost import Ghost
# ghost = Ghost()




def visitSite(id):
    # br = mechanize.Browser()
    # br.open("http://127.0.0.1:5001/comment/view?id=%s" % id)
    driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
    # with ghost.start() as session:
    #     page, extra_resources = ghost.open("http://127.0.0.1:5001/comment/view?id=%s" % id)
    #     assert page.http_status==200 and 'jeanphix' in ghost.content
    driver.get("http://10.10.0.:5001/comment/view?id=%s" % id)
    print('[+] Visiting site...')
    return '+'

def viewComments(db):
    cur = db.cursor()
    cur.execute("SELECT id FROM comments_comment WHERE active=false")
    for row in cur.fetchall():
        # try:
        visitSite(id=int(row[0]))
        # except:
        #     pass
    db.close()

while True:
    db = MySQLdb.connect(host="localhost",
                     user="my_awesome_shop_user",      
                     passwd="secret_password",
                     db="my_awesome_shop_db")
    viewComments(db)
    print('Waiting for next round...')
    time.sleep(3)
