"""
view.py
"""
from django.http import HttpResponse
import MySQLdb
# Create your views here.


def db_connect(request):
    """
    db db_connect
    connecting to the database
    importing MYsql for connectivity

    """
    print("request", request.user)
    try:
        db_con = MySQLdb.connect(host='localhost', db='tutorial', user='root', charset='utf8', passwd='Yukisha123@')
        print("db connectivity ", db_con)
        print("db connectivity ", type(db_con))
    except Exception as error_db_Con:
        print("error_db_Con", error_db_Con)

    return HttpResponse({"ok": "ok"})
