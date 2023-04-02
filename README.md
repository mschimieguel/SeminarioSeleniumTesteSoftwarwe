## Requirements For Windows Systems

Python3

Get the Python 3.11 on the [Microsoft Store](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=en-us&gl=us)
`sudo apt-get install python3`

### Librarys
For installing Python Librarys do you need the pip installed.You can install it with the following commands:

`sudo apt install python3-pip`

#### Pandas
To manage data scrapped from sites and export it for excel sheets.

`pip3 install pandas`

####  BeautifulSoup
To scrap the web sites contents.

`pip3 install beautifulsoup4`

####  Selenium
Is the responsable for automating the tasks in the browser.

`pip3 install selenium`

### ChromeDriver

you will need to download latest executable from git repository 
[Geckodriver](https://github.com/mozilla/geckodriver/releases).

Next you will need to add the directory containing the executable to the system path.
you can do the following to append it to your system’s search path :

`export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step`

Now you can run this code:
```
from selenium import webdriver
browser = webdriver.Firefox()
```
Then a Mozila Firefox automated browser will opening.

