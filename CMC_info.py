from bs4 import BeautifulSoup
import pandas as pd
import requests
from fpdf import FPDF
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables
load_dotenv(find_dotenv())

def generate_crypto_report(crypto_name):
    # Base URL for CoinMarketCap
    # url1 = "https://coinmarketcap.com/currencies/"
    url1: str = os.getenv("CRYPTO_URL")
    finalUrl = str(url1) + str(crypto_name)
    print(crypto_name, 'Statistics--->')

    webpage = requests.get(url=finalUrl, params=None )


    if webpage.status_code != 200:
        print("No such cryptocurrency found")
        return

    soup = BeautifulSoup(webpage.content, "html.parser")

    # Data dictionary to store extracted information
    data = {
        "Statistic": [],
        "Value": []
    }

    # Current Price
    CurrentPrice = soup.find("span", attrs={"class":"sc-65e7f566-0 clvjgF base-text"}).text
    print("Current Price:", CurrentPrice)
    data["Statistic"].append("Current Price")
    data["Value"].append(CurrentPrice)

    # Market Cap
    market_cap_div = soup.find('div', class_='sc-c6f90d42-1 dtJGSf', string='Market cap')
    if market_cap_div:
        market_dd = market_cap_div.find_next('dd', class_='sc-65e7f566-0 dzgtSD base-text')
        market_cap_value = ''.join(market_dd.find_all(string=True, recursive=False)).strip()
        print("Market Cap:", market_cap_value)
        data["Statistic"].append("Market Cap")
        data["Value"].append(market_cap_value)

    # Volume
    volume_div = soup.find('div', class_='sc-c6f90d42-1 dtJGSf', string='Volume (24h)')
    if volume_div:
        volume_dd = volume_div.find_next('dd', class_='sc-65e7f566-0 dzgtSD base-text')
        volume_value = ''.join(volume_dd.find_all(string=True, recursive=False)).strip()
        print("Volume (24h):", volume_value)
        data["Statistic"].append("Volume (24h)")
        data["Value"].append(volume_value)

    # Circulating Supply
    circulating_supply_div = soup.find('div', class_='sc-c6f90d42-1 dtJGSf', string='Circulating supply')
    if circulating_supply_div:
        circulating_supply_value = circulating_supply_div.find_next('dd', class_='sc-65e7f566-0 dzgtSD base-text').text.strip()
        print("Circulating Supply:", circulating_supply_value)
        data["Statistic"].append("Circulating Supply")
        data["Value"].append(circulating_supply_value)

    # Total Supply
    TotalSupply_div = soup.find('div', class_='sc-c6f90d42-1 dtJGSf', string='Total supply')
    if TotalSupply_div:
        TotalSupply_value = TotalSupply_div.find_next('dd', class_='sc-65e7f566-0 dzgtSD base-text').text.strip()
        print("Total Supply:", TotalSupply_value)
        data["Statistic"].append("Total Supply")
        data["Value"].append(TotalSupply_value)

    # Max Supply
    MaxSupply_div = soup.find('div', class_='sc-c6f90d42-1 dtJGSf', string='Max. supply')
    if MaxSupply_div:
        MaxSupply_value = MaxSupply_div.find_next('dd', class_='sc-65e7f566-0 dzgtSD base-text').text.strip()
        print("Max Supply:", MaxSupply_value)
        data["Statistic"].append("Max Supply")
        data["Value"].append(MaxSupply_value)

    # Fully Diluted Market Cap
    FullyDiluted_div = soup.find('div', class_ = 'sc-c6f90d42-1 dtJGSf', string='Fully diluted market cap')
    if FullyDiluted_div:
        FullyDiluted_value = FullyDiluted_div.find_next('dd', class_='sc-65e7f566-0 dzgtSD base-text').text.strip()
        print("Fully Diluted Market Cap:", FullyDiluted_value)
        data["Statistic"].append("Fully Diluted Market Cap")
        data["Value"].append(FullyDiluted_value)

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    csv_filename = os.path.join('samples', f"{crypto_name}_statistics.csv")
    df.to_csv(csv_filename, index=False)
    print(f"Data saved to {csv_filename}")

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)

    # Add a title
    pdf.cell(200, 30, txt=f"{crypto_name.capitalize()} Statistics", ln=True, align="C")

    # Set the column headers
    pdf.cell(95, 10, txt="Statistic", border=1, align="C")
    pdf.cell(95, 10, txt="Value", border=1, align="C")
    pdf.ln()

    # Add the table rows
    for i in range(len(df)):
        statistic = df.iloc[i]["Statistic"]
        value = df.iloc[i]["Value"]
        pdf.cell(95, 10, txt=statistic, border=1, align="L")
        pdf.cell(95, 10, txt=value, border=1, align="L")
        pdf.ln()

    # Save the PDF
    pdf_filename = os.path.join('samples', f"{crypto_name}_statistics.pdf")
    # pdf_filename = f"{crypto_name}_statistics.pdf"
    pdf.output(pdf_filename)
    print(f"PDF generated: {pdf_filename}")

    

# Take user input and pass it to the function
crypto_name = input("Enter Cryptocurrency name: ")
generate_crypto_report(crypto_name)
