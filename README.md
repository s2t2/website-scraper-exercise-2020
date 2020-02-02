#  Web Scraper Exercise 2020

Solutions for the following exercises:

 + [Website Scraper Exercise](https://github.com/prof-rossetti/intro-to-web-dev/blob/master/exercises/web-scraper/exercise.md)
 + [Website Scraper Exercise - CSV Challenge](https://github.com/prof-rossetti/intro-to-web-dev/blob/master/exercises/web-scraper/csv-challenge.md)
 + [API Client Exercise](https://github.com/prof-rossetti/intro-to-web-dev/blob/master/exercises/api-client-py/exercise.md)

## Setup

Fork [this remote repository](https://github.com/s2t2/website-scraper-exercise-2020/), then clone or download your forked repository onto your local computer, for example onto the Desktop. Then navigate there from the command-line:

```sh
cd ~/Desktop/web-scraper-exercise-2020
```

Create and activate a new virtual environment within which to install Python and third-party Python packages:

```sh
conda create -n scraper-env python=3.7 # (first time only)
conda activate scraper-env
```

Install third-party Python packages:

```sh
pip install requests beautifulsoup4 selenium
```

## Usage

```sh
python scraper.py
```

```sh
python api_client.py
```

```sh
python web_driver.py
```
