from django.shortcuts import render
import matplotlib as mpl 
import matplotlib.pyplot as plt
import mpld3
import requests
import pandas as pd


def index(request):
     return render(request,'index.html')

def get_data():
     url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"


     headers = {
     'x-rapidapi-key': "c2d96daf15mshff016f7faac1f93p1d399cjsn0e7e7622dfc7",
     'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
     }

     return requests.request("GET", url, headers=headers)

def statewise(request):
     api_response =get_data()
     json = api_response.json()

     df = pd.DataFrame(json)

     df2= df.T

     df2.columns

     df2 = df2.drop(['active', 'confirmed', 'deaths', 'deltaconfirmed', 'deltadeaths',
       'deltarecovered', 'lastupdatedtime', 'migratedother', 'recovered',
       'state', 'statecode', 'statenotes', 'State Unassigned'], axis=1)

     df2.reset_index(drop=True, inplace=False)

     active_X = []
     confirmed_X = []
     death_X=[]
     states = list(df2.columns)
     for state in states:
          active_X.append(int(df2[state][2]['active']))
          confirmed_X.append(int(df2[state][2]['confirmed']))
          death_X.append(int(df2[state][2]['deaths']))

     aX = plt.figure(figsize=(12,5))
     plt.bar(states, active_X)
     plt.xlabel('States')
     plt.ylabel('Active cases')
     plt.title("Active Cases Statewise")
     plt.xticks(rotation =90)
    

     
     cX = plt.figure(figsize=(12,5))
     plt.bar(states, confirmed_X)
     plt.xlabel('States')
     plt.ylabel('Confirmed cases')
     plt.title("Confirmed Cases Statewise")
     plt.xticks(rotation =90)


     dX =plt.figure(figsize=(12,5))
     plt.bar(states, death_X)
     plt.xlabel('States')
     plt.ylabel('Death cases')
     plt.title("Death Cases Statewise")
     plt.xticks(rotation =90)
     plt.yticks(rotation =30)




     html_fig_active = mpld3.fig_to_html(aX,template_type="general")
     #mpld3.save_html(aX,"covinfo\\templates\\axhtml.html")
     html_fig_confirmed = mpld3.fig_to_html(cX,template_type="general")
     html_fig_deaths = mpld3.fig_to_html(dX,template_type="general")

     plt.close(html_fig_active)
     plt.close(html_fig_confirmed)
     plt.close(html_fig_deaths)
     return render(request, "state.html", {'active_page' : 'state.html', 'div_figureActive' : html_fig_active,"div_figureConfirmed":html_fig_confirmed,"div_figureDeath":html_fig_deaths})


def tests(request):
     return render(request,"tests.html")


def world(request):
     return render(request,"world.html")