# Define a imagem base do container como Node.js 20.10.0
FROM node:20.10.0

# Define o diretório de trabalho como o diretório raiz do projeto
WORKDIR /app

# Copia o arquivo package.json para o container
COPY package.json .

# Instala as dependências do Node.js usando o arquivo package.json
RUN npm install

# Copia todo o conteúdo da pasta front para o container
COPY . .

# Exibe a porta 5173 para que outros containers possam acessá-la
EXPOSE 5173

# Define o comando a ser executado quando o container for iniciado
# Este comando executa o script `start` do pacote npm
CMD ["npm", "start"]