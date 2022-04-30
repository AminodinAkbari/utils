#this function can use as a decorator help u to get how many times spend to get queries from DB
from django.db import reset_queries
import datetime
from django.db import connection
time = datetime
def debugger(func):
    def wrapper(*args,**kwargs):
        reset_queries()
        start_time = time.time()
        value = func(*args,**kwargs) 
        end_time = time.time()
        queries = len(connection.queries)
        print(f"\n-------------\nConection Numbers: {queries} \n taketime = {(end_time-start_time):.3f}\n-----------\n")
        return value
    return wrapper
#***********************************************************************************************
