import csv

def read_csv(input_file: str) -> list[dict]:
    """
    Reads a CSV file and returns a list of dictionaries containing specific fields.

    Args:
        input_file (str): Path to the input CSV file.

    Returns:
        list[dict]: A list of dictionaries with keys 'Name', 'Symbol', and 'Invested Amount'.
                    Returns an empty list if an error occurs.
    """
    input_data = []
    try:
        with open(input_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                input_data.append({
                    "Name": row.get("Name", ""),
                    "Symbol": row.get("Symbol", ""),
                    "Invested Amount": row.get("Invested Amount", "")
                })
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the csv file: {e}")

    return input_data


def write_csv(output_file: str, data: list[dict]) -> None:
    """
    Writes a list of dictionaries to a CSV file.
    
    Args:
        output_file (str): Path to the output CSV file.
        data (list[dict]): A list of dictionaries to write, where keys are used as headers.
    """
    if not data:
        print("Error: No data to write to the CSV file.")
        return
    
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"An error occurred while writing to the csv file: {e}")