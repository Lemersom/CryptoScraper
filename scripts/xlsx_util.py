from openpyxl import Workbook, load_workbook

def read_xlsx(input_file: str) -> list[dict]:
    input_data = []
    try:
        workbook = load_workbook(input_file)
        sheet = workbook.active

        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_dict = {headers[i]: row[i] for i in range(len(headers))}
            input_data.append(row_dict)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the xlsx file: {e}")
    
    return input_data

def write_xlsx(output_file: str, data: list[dict]) -> None:
    workbook = Workbook()
    sheet = workbook.active

    headers = list(data[0].keys())
    sheet.append(headers)

    for row in data:
        sheet.append(list(row.values()))
    
    workbook.save(output_file)