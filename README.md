### Status
[![Build Status](https://travis-ci.com/milror00/FreeProxyListScraper.png)](https://travis-ci.com/milror00/FreeProxyListScraper.svg?branch=master)

# Free Proxy List Scraper - http://www.freeproxylists.net/

This is a demo project that uses python - request and behave to scrape the currencies published by yahoo finance. This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

* Python 3.5 above
* requests==2.23.0
* lxml==4.5.0

Steps for installation:

1. git clone repo
1. pip install -r requirements.txt or 1. pip install poetry 2. poetry install (poetry is a lib dependency manager )
1. run the yahoo_currencies_scraper.py

Results :

|IP Address|Port                |Country code   |Anonymity      |HTTPS          |
|----------|-------------------|---------------|---------------|---------------|
|158.69.60.89|8080                |CA             |anonymous      |no             |
|209.97.159.125|80                  |US             |anonymous      |no             |
|54.210.150.116|8080                |US             |anonymous      |no             |
|36.91.48.186|8080                |ID             |elite proxy    |no             |
|12.139.101.100|80                  |US             |anonymous      |no             |
|173.249.24.52|3128                |DE             |anonymous      |no             |
|82.200.233.4|3128                |KZ             |elite proxy    |no             |
|165.227.202.9|80                  |US             |anonymous      |no             |
|192.41.13.71|3128                |US             |anonymous      |yes            |
|68.183.158.43|3128                |US             |anonymous      |no             |
|200.73.128.86|80                  |AR             |anonymous      |no             |
|58.176.150.177|80                  |HK             |anonymous      |no             |
|167.86.126.167|3128                |DE             |anonymous      |no             |
|192.41.71.204|3128                |US             |anonymous      |yes            |
|165.227.183.55|8080                |US             |anonymous      |no             |
|181.117.176.236|61358               |AR             |elite proxy    |no             |
|157.245.15.86|8080                |US             |anonymous      |no             |
|94.229.32.85|3128                |SK             |elite proxy    |no             |
|70.37.79.42|8080                |US             |anonymous      |no             |
|134.209.29.120|3128                |GB             |anonymous      |no             |
|41.85.189.66|57797               |BJ             |elite proxy    |no             |
|200.106.55.125|80                  |PE             |elite proxy    |no             |
|122.217.227.42|8080                |JP             |anonymous      |no             |
|184.90.114.134|3128                |US             |elite proxy    |no             |
|95.161.216.11|3128                |RU             |elite proxy    |no             |
|103.142.68.163|80                  |BD             |elite proxy    |no             |
|5.190.63.12|8080                |IR             |anonymous      |no             |
|103.142.68.161|80                  |BD             |elite proxy    |no             |
|187.17.19.90|61411               |BR             |elite proxy    |no             |
|94.177.247.230|8080                |DE             |anonymous      |no             |
|89.36.195.238|52808               |IR             |elite proxy    |no             |
|45.64.99.26|8080                |ID             |anonymous      |no             |
|72.169.66.157|87                  |US             |transparent    |no             |
|103.86.50.186|8080                |TH             |anonymous      |no             |
|115.127.26.1|39611               |BD             |transparent    |no             |
|178.239.152.16|8080                |IR             |transparent    |no             |
|187.60.160.194|8083                |BR             |transparent    |no             |
|36.77.230.242|8080                |ID             |transparent    |no             |
|117.239.54.92|3128                |IN             |transparent    |no             |
|103.112.212.30|83                  |IN             |transparent    |no             |
|150.107.22.220|8080                |IN             |transparent    |no             |
|180.242.106.3|8080                |ID             |transparent    |no             |
|79.100.230.17|3128                |BG             |transparent    |no             |
|103.89.235.82|83                  |IN             |transparent    |no             |
|81.236.13.23|32500               |SE             |transparent    |no             |
|45.177.145.235|999                 |AR             |transparent    |no             |
|190.0.9.2 |999                 |CO             |transparent    |no             |
|138.97.200.22|8080                |AR             |transparent    |no             |
|87.247.3.234|39489               |KZ             |transparent    |no             |
|36.65.194.112|3128                |ID             |transparent    |no             |
|103.88.221.105|35411               |IN             |transparent    |no             |
|93.126.144.210|8080                |LB             |transparent    |no             |
|88.199.164.141|8080                |PL             |transparent    |no             |
|103.11.23.0|8085                |ID             |transparent    |no             |
|14.38.255.14|80                  |KR             |transparent    |no             |
|103.46.235.1|83                  |IN             |transparent    |no             |
|103.216.147.61|8080                |IN             |transparent    |no             |
|149.202.168.208|80                  |FR             |transparent    |no             |
|103.213.116.195|8080                |ID             |transparent    |no             |
|103.89.235.229|83                  |IN             |transparent    |no             |
|103.218.102.162|8080                |IN             |transparent    |no             |
|188.40.183.188|1080                |DE             |elite proxy    |no             |
|88.198.50.103|8080                |DE             |anonymous      |no             |
|46.4.96.67|80                  |DE             |anonymous      |no             |
|136.243.92.25|1080                |DE             |elite proxy    |no             |
|167.86.92.107|3128                |DE             |anonymous      |no             |
|176.9.75.42|8080                |DE             |anonymous      |no             |
|154.16.202.22|8080                |DE             |anonymous      |no             |
|92.51.149.81|3128                |DE             |anonymous      |no             |
|144.76.214.157|1080                |DE             |elite proxy    |no             |
|186.226.183.170|34497               |BR             |elite proxy    |no             |
|78.46.81.7|1080                |DE             |elite proxy    |no             |
|161.35.70.249|8080                |DE             |anonymous      |no             |
|200.255.122.170|8080                |BR             |anonymous      |yes            |
|88.99.10.255|1080                |DE             |elite proxy    |no             |
|168.205.222.49|57643               |BR             |elite proxy    |no             |
|181.118.167.104|80                  |CL             |elite proxy    |yes            |
|103.142.68.252|80                  |BD             |elite proxy    |no             |
|79.137.44.85|3129                |ES             |elite proxy    |no             |
|77.238.79.111|8080                |BG             |elite proxy    |no             |
|200.25.254.193|54240               |CO             |elite proxy    |no             |
|203.19.92.3|80                  |AU             |anonymous      |no             |
|191.240.152.131|80                  |BR             |anonymous      |no             |
|173.249.30.197|8118                |DE             |elite proxy    |no             |
|207.154.231.213|8080                |DE             |anonymous      |no             |
|131.161.68.29|33716               |BR             |elite proxy    |no             |
|195.4.164.127|8080                |DE             |anonymous      |no             |
|68.183.208.248|80                  |DE             |anonymous      |no             |
|191.240.152.133|80                  |BR             |anonymous      |no             |
|188.40.183.185|1080                |DE             |elite proxy    |yes            |
|197.211.245.50|53281               |ZW             |elite proxy    |no             |
|144.76.214.153|1080                |DE             |elite proxy    |yes            |
|200.108.183.2|8080                |BR             |elite proxy    |no             |
|144.76.214.156|1080                |DE             |elite proxy    |no             |
|173.212.202.65|80                  |DE             |elite proxy    |no             |
|82.119.170.106|8080                |DE             |elite proxy    |yes            |
|186.42.175.138|35150               |EC             |elite proxy    |no             |
|186.64.120.69|80                  |CL             |anonymous      |no             |
|88.99.10.249|1080                |DE             |elite proxy    |yes            |
|147.78.160.10|8080                |AL             |anonymous      |no             |
|88.99.10.250|1080                |DE             |elite proxy    |no             |
|169.57.157.146|80                  |BR             |elite proxy    |no             |
|186.159.3.41|30334               |CO             |elite proxy    |no             |
|85.10.219.100|1080                |DE             |elite proxy    |no             |
|35.220.131.188|80                  |--             |anonymous      |no             |
|203.202.245.58|80                  |BD             |anonymous      |no             |
|5.189.133.231|80                  |DE             |elite proxy    |no             |
|201.64.22.51|80                  |BR             |anonymous      |no             |
|103.28.121.58|3128                |BD             |anonymous      |yes            |
|77.56.156.148|80                  |CH             |anonymous      |no             |
|103.79.183.157|53281               |BD             |elite proxy    |no             |
|195.4.168.40|8080                |DE             |anonymous      |no             |
|200.25.254.135|56897               |CO             |elite proxy    |no             |
|200.73.128.5|8080                |AR             |anonymous      |yes            |
|85.10.219.99|1080                |DE             |elite proxy    |no             |
|46.4.96.87|80                  |DE             |anonymous      |no             |
|88.99.220.70|3128                |DE             |elite proxy    |no             |
|80.187.140.26|8080                |DE             |elite proxy    |yes            |
|203.202.245.62|80                  |BD             |anonymous      |no             |
|169.57.157.148|8123                |BR             |elite proxy    |no             |
|181.129.127.234|57985               |CO             |elite proxy    |no             |
|181.129.52.154|54351               |CO             |elite proxy    |no             |
|188.40.183.187|1080                |DE             |elite proxy    |no             |
|200.55.218.202|53281               |CL             |elite proxy    |no             |
|144.76.214.155|1080                |DE             |elite proxy    |no             |
|94.230.155.57|38786               |CZ             |elite proxy    |no             |
|200.35.56.161|35945               |CO             |elite proxy    |no             |
|181.211.245.74|44267               |EC             |elite proxy    |no             |
|157.245.63.182|8118                |SG             |anonymous      |no             |
|165.227.19.100|8080                |US             |anonymous      |no             |
|139.99.105.186|80                  |CA             |anonymous      |no             |
|91.230.199.174|34333               |UA             |elite proxy    |yes            |
|124.219.176.139|39589               |JP             |elite proxy    |no             |
|120.89.46.151|8080                |PH             |elite proxy    |yes            |
|78.108.66.26|3128                |RU             |elite proxy    |no             |
|167.86.66.178|3128                |DE             |anonymous      |yes            |
|192.41.71.221|3128                |US             |anonymous      |yes            |
|95.79.55.196|53281               |RU             |anonymous      |yes            |
|185.49.130.81|60839               |TR             |elite proxy    |no             |
|103.250.153.198|59451               |IN             |elite proxy    |no             |
|36.72.155.120|8080                |ID             |elite proxy    |no             |
|103.29.221.209|48377               |IN             |elite proxy    |no             |
|163.172.190.160|8811                |FR             |anonymous      |yes            |
|103.242.44.80|8080                |MN             |elite proxy    |no             |
|176.113.157.149|56744               |UA             |elite proxy    |no             |
|202.61.49.52|48298               |PK             |elite proxy    |no             |
|102.164.214.225|55034               |ZA             |elite proxy    |no             |
|103.86.192.74|8080                |BD             |elite proxy    |no             |
|175.100.18.45|57716               |KH             |elite proxy    |no             |
|96.87.184.101|43705               |US             |elite proxy    |no             |
|103.140.24.21|34925               |BD             |elite proxy    |no             |
|1.179.206.161|59033               |TH             |elite proxy    |no             |
|37.17.38.196|53281               |BY             |elite proxy    |no             |
|212.24.53.118|3128                |RU             |elite proxy    |no             |
|117.102.119.150|47704               |ID             |elite proxy    |no             |
|181.129.140.226|36733               |CO             |elite proxy    |no             |
|202.55.169.141|3128                |ID             |anonymous      |no             |
|51.158.119.88|8811                |FR             |anonymous      |no             |
|98.158.58.200|8080                |US             |anonymous      |no             |
|186.29.163.97|49787               |CO             |elite proxy    |no             |
|5.160.150.44|8080                |IR             |transparent    |no             |
|134.35.27.222|8080                |YE             |transparent    |no             |
|178.239.152.20|8080                |IR             |transparent    |no             |
|42.3.51.34|80                  |HK             |anonymous      |no             |
|185.198.184.14|48122               |ES             |elite proxy    |no             |
|178.20.137.178|43980               |CZ             |elite proxy    |no             |
|217.162.74.172|80                  |CH             |anonymous      |no             |
|131.117.162.8|8080                |YE             |transparent    |no             |
|46.35.91.211|8080                |YE             |transparent    |no             |
|198.143.178.30|3128                |US             |transparent    |no             |
|184.82.25.11|8080                |TH             |transparent    |no             |
|139.59.1.14|3128                |IN             |anonymous      |no             |
|85.10.219.96|1080                |DE             |elite proxy    |no             |
|119.28.215.215|3023                |HK             |anonymous      |yes            |
|188.156.240.240|8118                |HU             |elite proxy    |no             |
|201.182.153.214|53281               |BR             |elite proxy    |no             |
|92.222.180.156|8080                |FR             |anonymous      |no             |
|188.165.16.230|3129                |FR             |elite proxy    |no             |
|45.64.179.189|53281               |IN             |elite proxy    |no             |
|54.233.177.80|8080                |BR             |anonymous      |no             |
|51.38.123.159|8000                |FR             |anonymous      |no             |
|188.40.183.190|1080                |DE             |elite proxy    |yes            |
|5.252.161.48|8080                |GB             |anonymous      |no             |
|188.40.183.184|1080                |DE             |elite proxy    |no             |
|163.172.98.25|80                  |GB             |elite proxy    |no             |
|45.77.65.24|3128                |DE             |anonymous      |no             |
|203.202.254.206|32938               |BD             |elite proxy    |no             |
|160.0.204.218|8080                |ZA             |transparent    |no             |
|88.99.10.254|1080                |DE             |elite proxy    |no             |
|47.75.90.57|80                  |HK             |anonymous      |no             |
|177.75.4.34|80                  |BR             |elite proxy    |no             |
|119.11.240.78|58899               |ID             |elite proxy    |no             |
|159.8.114.37|8123                |FR             |elite proxy    |no             |
|151.240.93.142|8080                |IR             |transparent    |no             |
|46.105.191.85|80                  |FR             |anonymous      |no             |
|46.4.96.137|3128                |DE             |anonymous      |no             |
|81.144.138.35|3128                |GB             |anonymous      |no             |
|82.81.169.142|80                  |IL             |anonymous      |no             |
|144.91.100.154|3129                |DE             |elite proxy    |no             |
|134.35.169.72|8080                |YE             |transparent    |no             |
|168.205.92.131|8080                |AR             |anonymous      |no             |
|91.52.23.75|8080                |DE             |anonymous      |yes            |
|88.198.24.108|8080                |DE             |anonymous      |no             |
|190.214.13.90|21776               |EC             |elite proxy    |no             |
|37.19.95.140|8080                |IR             |transparent    |no             |
|60.251.33.225|80                  |TW             |anonymous      |no             |
|159.138.1.185|80                  |HK             |anonymous      |no             |
|209.97.150.167|8080                |US             |anonymous      |no             |
|192.99.244.148|8080                |CA             |anonymous      |no             |
|198.199.120.102|3128                |US             |anonymous      |no             |
|142.93.4.1|3128                |US             |anonymous      |no             |
|198.199.86.11|8080                |US             |anonymous      |no             |
|112.133.214.244|80                  |IN             |anonymous      |no             |
|35.169.12.194|8080                |US             |anonymous      |no             |
|165.227.43.101|3128                |CA             |anonymous      |no             |
|147.78.163.38|8080                |AL             |anonymous      |no             |
|191.240.152.129|80                  |BR             |anonymous      |no             |
|5.56.133.225|34567               |GB             |transparent    |no             |
|125.16.18.182|80                  |IN             |anonymous      |no             |
|167.71.5.83|8080                |NL             |anonymous      |no             |
|165.227.216.208|8080                |US             |anonymous      |no             |
|34.95.132.229|8080                |US             |anonymous      |no             |
|77.94.137.243|3128                |SI             |anonymous      |no             |
|191.240.152.130|80                  |BR             |anonymous      |no             |
|63.82.52.254|8080                |US             |anonymous      |no             |
|176.9.119.170|8080                |DE             |anonymous      |no             |
|188.226.141.61|3128                |NL             |anonymous      |no             |
|178.205.105.117|3128                |RU             |anonymous      |no             |
|45.9.144.2|8080                |IR             |transparent    |no             |
|77.82.148.26|8080                |RU             |transparent    |no             |
|191.240.152.134|80                  |BR             |anonymous      |no             |
|51.38.184.52|8080                |FR             |anonymous      |no             |
|52.179.231.206|80                  |US             |anonymous      |no             |
|194.5.206.231|8080                |NL             |anonymous      |no             |
|18.163.28.22|1080                |HK             |anonymous      |no             |
|118.69.50.154|443                 |VN             |anonymous      |no             |
|165.227.43.144|80                  |CA             |anonymous      |no             |
|118.193.34.56|8080                |HK             |anonymous      |no             |
|60.251.33.224|80                  |TW             |anonymous      |no             |
|188.166.83.17|3128                |NL             |anonymous      |no             |
|52.69.132.45|8080                |JP             |anonymous      |no             |
|198.46.223.156|8080                |US             |anonymous      |no             |
|191.96.42.80|3128                |US             |anonymous      |no             |
|103.4.112.18|80                  |HK             |anonymous      |no             |
|159.203.61.169|3128                |CA             |anonymous      |no             |
|200.89.178.118|8080                |AR             |anonymous      |yes            |
|162.243.108.129|3128                |US             |anonymous      |no             |
|203.82.36.105|8080                |PH             |elite proxy    |yes            |
|157.119.207.35|8080                |IN             |elite proxy    |no             |
|188.226.141.211|3128                |NL             |anonymous      |no             |
|138.197.157.32|8080                |CA             |anonymous      |no             |
|78.130.145.167|39825               |BG             |elite proxy    |no             |
|37.120.192.154|8080                |NL             |anonymous      |no             |
|191.241.34.222|8089                |BR             |elite proxy    |no             |
|139.162.78.109|3128                |JP             |anonymous      |no             |
|183.88.193.11|8080                |TH             |elite proxy    |no             |
|36.89.8.235|8080                |ID             |elite proxy    |no             |
|45.33.90.184|8080                |US             |elite proxy    |yes            |
|103.61.101.74|54478               |IN             |elite proxy    |no             |
|138.68.240.218|8080                |US             |anonymous      |no             |
|162.249.248.218|53281               |US             |elite proxy    |yes            |
|202.152.38.75|52740               |ID             |elite proxy    |no             |
|197.216.2.18|8080                |AO             |elite proxy    |no             |
|128.199.238.162|44344               |SG             |elite proxy    |yes            |
|46.175.185.239|36853               |UA             |elite proxy    |no             |
|203.82.36.107|8080                |PH             |elite proxy    |yes            |
|103.142.68.230|80                  |BD             |elite proxy    |no             |
|185.171.24.244|808                 |TR             |elite proxy    |no             |
|144.217.101.242|3129                |CA             |elite proxy    |yes            |
|62.122.201.241|46176               |UA             |elite proxy    |no             |
|138.68.60.8|3128                |US             |anonymous      |no             |
|62.176.1.194|32076               |RU             |transparent    |no             |
|213.239.218.54|8118                |DE             |transparent    |no             |
|170.81.35.26|36681               |CR             |transparent    |no             |
|201.149.100.17|8085                |BR             |transparent    |no             |
|200.186.53.98|58855               |BR             |transparent    |no             |
|118.174.232.106|50491               |TH             |transparent    |no             |
|103.92.212.65|43399               |BD             |transparent    |no             |
|41.73.240.188|8080                |NG             |transparent    |no             |
|192.200.200.120|3128                |US             |transparent    |no             |
|186.46.120.230|59282               |EC             |elite proxy    |yes            |
|185.74.38.93|41258               |IT             |elite proxy    |yes            |
|185.252.30.81|8080                |IR             |anonymous      |yes            |
|194.213.43.166|32422               |CZ             |elite proxy    |yes            |
|89.251.70.61|38408               |RU             |elite proxy    |yes            |
|88.99.10.251|1080                |DE             |elite proxy    |yes            |
|18.136.144.138|3838                |SG             |elite proxy    |yes            |
|131.221.64.152|23500               |AR             |elite proxy    |yes            |
|185.134.23.197|80                  |GB             |anonymous      |no             |
|119.81.71.27|8123                |SG             |elite proxy    |no             |
|117.58.241.164|52636               |BD             |elite proxy    |yes            |
|119.81.199.83|8123                |SG             |elite proxy    |no             |
|169.57.1.84|8123                |MX             |elite proxy    |no             |
|187.87.38.28|53281               |BR             |elite proxy    |yes            |
|41.217.219.49|54302               |MW             |elite proxy    |yes            |
|188.40.183.191|1080                |DE             |elite proxy    |yes            |
|203.19.88.59|80                  |AU             |anonymous      |no             |
|128.199.244.47|44344               |SG             |elite proxy    |yes            |
|119.81.199.81|8123                |SG             |elite proxy    |no             |
|36.89.165.89|43139               |ID             |elite proxy    |no             |
