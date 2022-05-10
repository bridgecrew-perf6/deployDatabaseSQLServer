from django.shortcuts import render
from settings.settings import conn

# Create your views here.
def home(request):
    
    cursor=conn.cursor()
    
    cursor.execute('SELECT [MessageText] FROM [Data_t].[dbo].[connectSuccess]')
    
    message = cursor.fetchall()
    
    return render (request, "connectionSQL/home.html", {"message":message})

