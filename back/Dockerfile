# Define a imagem base do container como Python 3.10.8
FROM python:3.10.8

# Define o diretório de trabalho como o diretório raiz do projeto
WORKDIR /app

# Copia o arquivo requirements.txt para o container
COPY requirements.txt .

# Instala as dependências do Python usando o arquivo requirements.txt
RUN pip install -r requirements.txt

# Copia todo o conteúdo da pasta back para o container
COPY . .

# Exibe a porta 8080 para que outros containers possam acessá-la
EXPOSE 8080

# Define o comando a ser executado quando o container for iniciado
# Este comando ativa o ambiente virtual venv e executa o script principal (main.py)
CMD ["python", "main.py"]