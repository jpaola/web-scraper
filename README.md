# web-scraper

A Python script to scrape book related data from the https://books.toscrape.com sandbox site and uploads the results onto an excel sheet.

# Execution

Make sure you have `Python` and it's package manager `PyPi` are installed on your machine.
Additionally, this program runs on `Python 3.11.4` and uses `pip 25.0.1`.

Run `python3 --version` and `python3 -m pip --version` to check what you have installed on your machine.

Using `pip` install `requests`, `beautifulsoup4`, `pandas`, and `openpyxl`.

```
python3 -m pip install requests beautifulsoup4 pandas openpyxl
```

Once you have every package installed, run the script as follows:

```
python3 scraper.py
```

Visit `https://packaging.python.org/en/latest/tutorials/installing-packages/` for additional help and support regarding Python and package management.
