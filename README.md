## Skiptracer - OSINT scraping framework
![python](https://img.shields.io/badge/python-2.7-green.svg) ![version](https://img.shields.io/badge/version-0.2.0-brightgreen.svg) ![licence](https://img.shields.io/badge/license-GPLv3-lightgrey.svg) [![](https://images.microbadger.com/badges/image/xshuden/skiptracer.svg)](https://microbadger.com/images/xshuden/skiptracer "Get your own image badge on microbadger.com") [![](https://images.microbadger.com/badges/version/xshuden/skiptracer.svg)](https://microbadger.com/images/xshuden/skiptracer "Get your own version badge on microbadger.com")

![screen](https://i.imgur.com/gG0KZ0F.png)

Initial attack vectors for recon usually involve utilizing pay-for-data/API (Recon-NG), or paying to utilize transforms (Maltego) to get data mining results. Skiptracer utilizes some basic python webscraping (BeautifulSoup) of PII paywall sites to compile passive information on a target on a ramen noodle budget.

Docker Installation
----
```
$ docker run -it --name skiptracer xshuden/skiptracer 
OR
$ docker run --rm -it --name skiptracer xshuden/skiptracer  # container is deleted when you're done
```

Installation
----
```
$ git clone https://github.com/xillwillx/skiptracer.git skiptracer
$ cd skiptracer
```
__Install requirements__
```
$ pip install -r requirements.txt
```
__Run__
```
$ python skiptracer.py
```

Usage
----
Full details on how to use Skiptracer are on the wiki located [here](https://github.com/xillwillx/skiptracer/wiki)

To-Do
----
Skiptracer is intedned to be a community driven application. If you are interested in helping out drop us a note.

* Finish converting to Python3 - Py2 EoL is 1/1/20
* Add more API support
* More Options from other countries so not so U.S.-centric results
* Bypass some of the methods being used to block scapers, i.e. headless selenium
* Ideas?
