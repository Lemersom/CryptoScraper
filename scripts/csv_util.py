import csv

def read_csv(input_file: str) -> list[dict]:
    input_data = []
    try:
        with open(input_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                input_data.append({
                    "Name": row["Name"],
                    "Symbol": row["Symbol"],
                    "Invested Amount": row["Invested Amount"]
                })
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the csv file: {e}")

    return input_data

def write_csv(output_file: str, data: list[dict]) -> None:
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)