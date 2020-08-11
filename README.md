## Steps to run project
- First make sure you have `python` install along with `pip` and `virtualenv`. Usually pip is installed along python and to install virtualenv: pip install virtualenv
- clone the repo
- create virtualenv: `virtualenv venv` or `virtualenv -p python3 venv`
- activate virtualenv: for linux(`source venv/bin/activate`) and for windows(`source venv/Scripts/activate`)
- install all necessary libraries in venv: `pip install -r requirements.txt` (all necessary libraries for project are in requirements.txt file)
- change the year to get data of that specific year
- finally run the project: `scrapy crawl hamro_patro`
