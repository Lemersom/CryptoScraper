# CryptoScraper

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Lemersom/CryptoScraper/blob/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/Lemersom/CryptoScraper/blob/main/README.pt-br.md)

CryptoScraper é uma ferramenta desenvolvida em Python para buscar dados de criptomoedas utilizando o Yahoo Finance. Ela permite que os usuários forneçam um arquivo de entrada (CSV ou XLSX) com os símbolos das criptomoedas, obtenham dados relevantes como preços e capitalização de mercado e salvem os resultados no mesmo formato do arquivo original.

## Tecnologias

- **Python**: Linguagem de programação principal.
- **BeautifulSoup**: Web scraping.
- **OpenPyXL**: Leitura e escrita de arquivos XLSX.
- **Módulo CSV**: Leitura e escrita de arquivos CSV.
- **Requests**: Para realizar requisições HTTP.
- **PyInstaller**: Para gerar executáveis independentes.

## Para os Usuários

1. **Baixe o Executável**  
   Faça o download do executável na página de [Releases](https://github.com/Lemersom/CryptoScraper/releases/latest) ou na pasta [bin](https://github.com/Lemersom/CryptoScraper/tree/main/bin).

2. **Prepare o Arquivo de Entrada**  
   Coloque um arquivo chamado `input.csv` ou `input.xlsx` na pasta `input/`. Certifique-se de que o arquivo contém as seguintes colunas:
   - **Name**: Nome da criptomoeda.
   - **Symbol**: Símbolo da criptomoeda (por exemplo, BTC-USD, SOL-USD).
   - **Invested Amount**: Valor que você investiu.

   > Observação: A pasta `input/` deve existir no mesmo diretório que o executável `.exe`.

3. **Execute o Programa**  
   Ao executar o arquivo `.exe`, o programa irá:
   - Ler o arquivo de entrada na pasta `input/`.
   - Buscar os dados das criptomoedas no Yahoo Finance.
   - Salvar os resultados em um novo arquivo de saída na pasta `output/`.
     - Se a pasta `output/` não existir, ela será criada automaticamente.

4. **Exemplos**  
   Arquivos de exemplo (entrada e saída) estão disponíveis nas pastas [input/](https://github.com/Lemersom/CryptoScraper/tree/main/input) e [output/](https://github.com/Lemersom/CryptoScraper/tree/main/output) no repositório.

## Para os Desenvolvedores

1. **Instale o Python**  
   Certifique-se de que o Python está instalado no seu sistema.

2. **Clone o Repositório**  
   Clone o repositório do projeto:
   ```bash
   git clone https://github.com/Lemersom/CryptoScraper.git
   cd CryptoScraper
   ```

3. **Crie um Ambiente Virtual**  
   - Crie o ambiente virtual:
     ```bash
     python -m venv venv
     ```
   - Ative o ambiente virtual:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

4. **Instale as Dependências**  
   Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a Aplicação**  
   Rode a aplicação:
   ```bash
   python ./scripts/main.py
   ```
