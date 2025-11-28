## 📈 NEPSE Scraper

1. A Python web scraping project to fetch and track stock market data from NEPSE (Nepal Stock Exchange).
2. Scrapes company symbols, latest price, open/high/low, quantity, and other trading info, then stores it in JSON for easy tracking over time.

## 🚀 Features

1) Scrapes all listed companies on NEPSE.

2) Extracts:
-  Symbol
-  Company Name
-  Latest Trading Price (LTP)
-  % Change
-  Open, High, Low prices
-  Quantity traded
-  Saves data to JSON (Nepse.json) for persistent storage.
-  Ready for automation to track market data over time.

## 🛠️ Installation & Run

1) clone the repository
 - git clone git@github.com:Aayam-Rimal/Nepse-scraped.git

2) Create a virtual environment

3) install the dependency
-  pip install -r requirements.txt

4) Run the file locally

## Automation

This scraper is designed for scheduled execution via cron (Linux/macOS). 

Example cron setup (3 PM, Monday–Thursday):

- Uses a virtual environment to isolate dependencies.
- Appends daily market data to `Nepse.json`.
- Logs output and errors to `scraper.log`.

> Note: Adjust paths according to your local setup.




