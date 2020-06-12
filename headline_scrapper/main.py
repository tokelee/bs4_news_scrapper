import requests, sys
from headline_scrapper import creation_date, date
from bs4 import BeautifulSoup as bsoup


def punch_scraper(url='https://punchng.com/topics/news/page/0/'):   
    response = requests.get(url)
    soup = bsoup(response.text, 'html.parser')
    
    #getting all h3 tags in the body
    headlines = soup.find_all('h2', {'class','seg-title'})
    summary = soup.find_all('div', {'class','seg-summary',})
    time = soup.find_all('span', {'class','pull-right'})

    headlines_list = [line.string for line in headlines]
    #summary_list = [str(line.string)[29:11] for line in summary]
    summary_list = []
    for line in summary:
        line = str(line)
        summary_list.append(line[29:-11])
    time_list = [line.string for line in time]

    each_news = list(
                    map(
                        lambda headlines_list,summary_list,time_list:
                        'HEADLINE: ' + str(headlines_list) + '\n\n' +
                        'SUMMARY: ' + str(summary_list) + '\n\n' +
                        'TIME: ' + str(time_list) + '\n\n\n\n',
                        headlines_list,summary_list,time_list
                        ))
    
    with open(f'Punch-{creation_date}.txt', 'w') as text_file:
        for news in each_news:
            text_file.write(news)
            text_file.flush()
        text_file.close()
        print(f'Scrapped {len(each_news)} News At The Punch Page Successfully')
    

def vanguard_scraper(url='https://www.vanguardngr.com/category/national-news'):
    response = requests.get(url)
    soup = bsoup(response.text, 'html.parser')

    headlines = soup.find_all('a', {'rel':'bookmark'})
    summary = soup.find_all('div', {'class':'entry-content'})
    #time = soup.find_all('time', {'class','entry-date published'})

    time_list = []

    headlines_list = [line.string for line in headlines]
    
    for line in headlines_list:      
        if line == date:
            headlines_list.remove(line)
            news_time = line.string
            time_list.append(str(news_time))
    
    summary_list = [summary[i].p.text for i in range(len(summary))]
    
    each_news = list(
                    map(
                        lambda headlines_list,summary_list,time_list:
                        'HEADLINE: ' + str(headlines_list) + '\n\n' +
                        'SUMMARY: ' + str(summary_list) + '\n\n' +
                        'TIME: ' + str(time_list) + '\n\n\n\n',
                        headlines_list,summary_list,time_list
                        ))
    
    with open(f'Vanguard-{creation_date}.txt','w', encoding='utf-8') as text_file:
        for news in each_news:
            text_file.write(news)
            text_file.flush()
        text_file.close()
        print(f'Scrapped {len(each_news)} News At The Vanguard Page Successfully')

def guardian_scraper(url = 'https://guardian.ng/'):
    response = requests.get(url)
    soup = bsoup(response.text, 'html.parser')

    headlines = soup.find_all('span', {'class':'title'})
    headlines_list = [line.string for line in headlines]
    time_list = [date for i in range(len(headlines))]

    each_news = list(
                    map(
                        lambda headlines_list,time_list:
                        'HEADLINE: ' + str(headlines_list) + '\n\n' +
                        'TIME: ' + str(time_list) + '\n\n\n\n',
                        headlines_list,time_list
                        ))
    
    with open(f'Guardian-{creation_date}.txt','w') as text_file:
        for news in each_news:
            text_file.write(news)
            text_file.flush()
        text_file.close()
        print(f'Scrapped {len(each_news)} News At The Guardian Page Successfully')
