# Cryptocurrency Statistics Scraper

This Python project scrapes cryptocurrency data from CoinMarketCap and generates a detailed report in both CSV and PDF formats. The report includes the current price, market cap, volume, circulating supply, total supply, max supply, and fully diluted market cap for a specified cryptocurrency.

## Features

- Scrape real-time cryptocurrency data from CoinMarketCap.
- Export data to a CSV file.
- Generate a PDF report with the scraped data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system.
- An active internet connection to fetch data from CoinMarketCap.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/aniketchaudharicodes/WebScrapping.git
    cd WebScrapping
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add the CoinMarketCap URL:

    ```
    CRYPTO_URL=https://coinmarketcap.com/currencies/
    ```

## Usage

1. Run the script:

    ```bash
    python CMC_info.py
    ```

2. Enter the name of the cryptocurrency when prompted:

    ```
    Enter Cryptocurrency name: bitcoin
    ```

3. The script will output the statistics and generate a CSV file and a PDF report in the `samples` directory.

## Output

- **CSV File:** Contains the scraped data in tabular form.
- **PDF Report:** A formatted PDF report of the cryptocurrency statistics.

## Example

For `bitcoin`, the script will generate:

- `samples/bitcoin_statistics.csv`
- `samples/bitcoin_statistics.pdf`

## Sample PDF Report
| Statistics           | Value                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Current Price | $58,931.53 |
| Market Cap | $1,164,184,510,476 |
| Volume (24h) | $12,897,107,618 |
| Circulating Supply | 19,747,740 BTC |
| Total Supply | 19,747,740 BTC |
| Max Supply | 21,000,000 BTC |
| Fully Diluted Market Cap | $1,238,008,740,240 |


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
