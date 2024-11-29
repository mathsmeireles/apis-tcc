# Etapa base: usar uma imagem oficial do Python como base
FROM python:3.12-slim

# Configurar o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de requisitos para instalar dependências
COPY requirements.txt /app/

# Instalar as dependências do Django e outras do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do projeto para o diretório de trabalho no contêiner
COPY . /app

# Configurar as variáveis de ambiente do Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE biblioteca.settings

# Expõe a porta 8000 para o servidor Django
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
