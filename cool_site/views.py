import sqlite3

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse


def projects(request):
    con = sqlite3.connect("identifier.sqlite")
    cursor = con.cursor()

    rows = cursor.execute("select * from projects").fetchall()
    con.close()


    return render(request, 'projects.html', {"data": rows})


def tasks(request):
    con = sqlite3.connect("identifier.sqlite")
    cursor = con.cursor()

    rows = cursor.execute("select * from tasks").fetchall()
    con.close()


    return render(request, 'tasks.html', {"data": rows})

def employees(request):
    con = sqlite3.connect("identifier.sqlite")
    cursor = con.cursor()

    rows = cursor.execute("select * from employees").fetchall()
    con.close()

    return render(request, 'employees.html', {"data": rows})

def schedule(request):
    # con = sqlite3.connect("identifier.sqlite")
    # cursor = con.cursor()
    #
    # rows = cursor.execute("select * from schedule").fetchall()
    # con.close()
    #
    # return render(request, 'schedule.html', {"data": rows})
    return  render(request, 'schedule.html')


def index(request):
    return  render(request, 'index.html')