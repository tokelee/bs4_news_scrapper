NOTE:- PLEASE CHANGE THE desktop_path VARIABLE TO YOUR OWN DESKTOP PATH IF YOU WISH TO RUN THIS CODE ON YOUR OWN MACHINE, YOU CAN GET THE VARIABLE ASSIGNMENT AT THE PROJECT'S (__init__.py) file. 
CHANGE desktop_path = 'C:\\Users\\HP\\Desktop' to desktop_path = '{Your PC desktop path}' e.g 'C:\\Users\\DEL\\Desktop'

THIS PACKAGE IS SETUP TO SCRAP THREE NIGERIAN NEWS PAPERS NAMELY:
i.      The Guardian
ii.     The Punch
iii.    The Vanguard

Modules Used are
i.      BeautifulSoup
ii.     Requests

It Scraps the News papers homepage and returns there Headlines, time and Summary in the following files respectively
i.      ../desktop/Headlines/{date-scrapepd}/Guardian-{date-scrapepd}.txt
ii.     ../desktop/Headlines/{date-scrapepd}/Punch-{date-scrapepd}.txt
iii.    ../desktop/Headlines/{date-scrapepd}/Vanguard-{date-scrapepd}.txt

TREE EXAMPLE
../desktop
    /Headlines
        /June-06-2020
            /Guardian-June-06-2020.txt

From the explanations above, when the project runs, it locates your desktop and creates a folder named (Headlines) then inside the (Headlines) folder it creates another folder (date-scrapepd i.e today's date)[this folder is created to uniquely identify each headlines scrapped in a particular day], then inside the (date-scrapped) folder it creates our scrapped files with the name of there company and date e.g(Guardian-12-06-2020.txt).

execute the code with ---> python3 run.py or python run.py