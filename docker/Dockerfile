# Usamos uma imagem oficial do Python como base
FROM python:3.10-slim

# Diretório padrão dentro do container onde o código será colocado
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Atualiza o pip e instala as dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Comando padrão ao iniciar o container (pode ser alterado para scripts)
CMD ["python"]
