import os
from datetime import datetime
import scraper
import csv_util
import xlsx_util

def create_output_folder(folder: str) -> None:
    """
    Creates the specified output folder if it does not already exist.

    Args:
        folder (str): Path to the folder to create.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)


def get_input_file(folder: str) -> None:
    """
    Retrieves the first CSV or XLSX file found in the specified folder.

    Args:
        folder (str): Path to the input folder.

    Returns:
        str | None: Full path to the input file if found, otherwise None.
    """
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.csv', '.xlsx'))]
    if not files:
        print(f"No input files found in {folder}. Please add a CSV or XLSX file.")
        return None
    return os.path.join(folder, files[0])


def read_input_file(input_file: str) -> list[dict]:
    """
    Reads data from a CSV or XLSX input file.

    Args:
        input_file (str): Path to the input file.

    Returns:
        list[dict]: List of dictionaries containing the file's data.
    """
    extension = os.path.splitext(input_file)[1].lower()

    if extension == '.csv':
        return csv_util.read_csv(input_file)
    elif extension == '.xlsx':
        return xlsx_util.read_xlsx(input_file)
    else:
        print("Error: Unsupported file format. Please provide a CSV or XLSX file.")
        return []


def write_output_file(output_file: str, data: list[dict]) -> None:
    """
    Writes data to a CSV or XLSX output file.

    Args:
        output_file (str): Path to the output file.
        data (list[dict]): Data to write to the file.
    """
    extension = os.path.splitext(output_file)[1].lower()

    if extension == '.csv':
        csv_util.write_csv(output_file, data)
    elif extension == '.xlsx':
        xlsx_util.write_xlsx(output_file, data)
    else:
        print("Error: Unsupported output file format. Please provide a CSV or XLSX file.")


def main():
    input_folder = "input/"
    output_folder = "output/"

    input_file = get_input_file(input_folder)
    if not input_file:
        return
    
    input_data = read_input_file(input_file)
    if not input_data:
        print("No data to process.")
        return

    create_output_folder(output_folder)

    # Determine the output file path
    extension = os.path.splitext(input_file)[1].lower()
    timestamp = datetime.today().strftime("%Y-%m-%d %H-%M-%S")
    output_file = os.path.join(output_folder, f"output {timestamp}{extension}")
    
    # Scrape data
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