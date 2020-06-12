import os
from datetime import datetime

time = datetime.now()
creation_date = time.strftime('%d-%m-%y')

#this date was used in the vanguard_scraper function
date = time.strftime('%B %d, %Y')

desktop_path = 'C:\\Users\\HP\\Desktop' #YOU MIGHT NEED TO CHANGE THIS DESKTOP PATH TO YOUR SYSTEM'S DESKTOP PATH


os.chdir(desktop_path)
if 'Headlines' not in os.listdir():
    headline_path = desktop_path+'\\Headlines'
    os.mkdir(headline_path)

#changing directory to our headline folder on our desktop
headline_path = desktop_path+'\\Headlines'
os.chdir(headline_path)

if time.strftime('%B-%d-%Y') not in os.listdir():
    #creating a new folder where we will be storing news every single day
    news_folder = headline_path + '\\' +time.strftime('%B-%d-%Y')
    os.mkdir(news_folder)

#changing to our news folder
news_folder = headline_path +'\\' + time.strftime('%B-%d-%Y')
os.chdir(news_folder)


from headline_scrapper import main