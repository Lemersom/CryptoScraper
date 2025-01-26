# CryptoScraper

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Lemersom/CryptoScraper/blob/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/Lemersom/CryptoScraper/blob/main/README.pt-br.md)

CryptoScraper is a Python-based tool that fetches cryptocurrency data using Yahoo Finance. It allows users to provide an input file (CSV or XLSX) containing cryptocurrency symbols, scrape relevant data like prices and market cap, and output the results in the same format as the input file.

## Technologies

- **Python**: The core programming language.
- **BeautifulSoup**: For web scraping.
- **OpenPyXL**: For reading and writing XLSX files.
- **CSV Module**: For reading and writing CSV files.
- **Requests**: For making HTTP requests.
- **PyInstaller**: For generating a standalone executable.

## For Users

1. **Download the Executable**  
   Get the executable from the [Releases](https://github.com/Lemersom/CryptoScraper/releases/latest) or the [bin folder](https://github.com/Lemersom/CryptoScraper/tree/main/bin).

2. **Prepare the Input File**  
   Place a single `input.csv` or `input.xlsx` file in the `input/` directory. Ensure the file includes the following columns:
   - **Name**: Name of the cryptocurrency.
   - **Symbol**: Cryptocurrency ticker symbol (e.g., BTC-USD, SOL-USD).
   - **Invested Amount**: Amount you invested.

   > Note: Make sure the `input/` folder exists in the same directory as the `.exe`.

3. **Run the Program**  
   Execute the `.exe` file. The program will:
   - Read the input file from the `input/` folder.
   - Fetch cryptocurrency data from Yahoo Finance.
   - Save the results in a new output file located in the `output/` folder.
     - If the `output/` folder does not exist, it will be created automatically.

4. **Examples**  
   Sample input and output files can be found in the [input/](https://github.com/Lemersom/CryptoScraper/tree/main/input) and [output/](https://github.com/Lemersom/CryptoScraper/tree/main/output) folders on the repository.

## For Developers

1. **Install Python**  
   Ensure Python is installed on your system.

2. **Clone the Repository**  
   Clone the project repository:
   ```bash
   git clone https://github.com/Lemersom/CryptoScraper.git
   cd CryptoScraper
   ```

3. **Set Up a Virtual Environment**  
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies**  
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**  
   Run the application:
   ```bash
   python ./scripts/main.py
   ```
