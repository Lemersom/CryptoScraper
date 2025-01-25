import os
from datetime import datetime
import scraper
import csv_util
import xlsx_util

def create_output_folder(folder: str) -> None:
    if not os.path.exists(folder):
        os.makedirs(folder)

def read_input_file(input_file: str) -> list[dict]:
    extension = os.path.splitext(input_file)[1].lower()

    if extension == '.csv':
        return csv_util.read_csv(input_file)
    elif extension == '.xlsx':
        return xlsx_util.read_xlsx(input_file)
    else:
        print("Error: Unsupported file format. Please provide a CSV or XLSX file.")
        return []

def write_output_file(output_file: str, data: list[dict]) -> None:
    extension = os.path.splitext(output_file)[1].lower()

    if extension == '.csv':
        csv_util.write_csv(output_file, data)
    elif extension == '.xlsx':
        xlsx_util.write_xlsx(output_file, data)
    else:
        print("Error: Unsupported output file format. Please provide a CSV or XLSX file.")


def main():
    input_file = "input/input.xlsx"
    output_folder = "output/"
    timestamp = datetime.today().strftime("%Y-%m-%d %H-%M-%S")
    output_file = os.path.join(output_folder, f"output {timestamp}{os.path.splitext(input_file)[1]}")

    create_output_folder(output_folder)
    
    input_data = read_input_file(input_file)
    if not input_data:
        print("No data to process.")
        return
    
    results = []
    for entry in input_data:
        crypto_data = scraper.scrape_crypto_data(entry['Symbol'])
        if crypto_data:
            results.append({
                "Name": entry["Name"],
                "Symbol": entry["Symbol"],
                "Invested Amount": entry["Invested Amount"],
                **crypto_data
            })
    
    if results:
        write_output_file(output_file, results)
        print(f"Scraping completed. Data written to {output_file}")
    else:
        print("No data scraped.")
    

if __name__ == "__main__":
    main()