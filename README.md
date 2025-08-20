# Exemplo de README para deploy com Docker/Easypanel

## Como usar

1. Faça o build da imagem Docker:
   ```bash
   docker build -t docling-api .
   ```
2. Rode o container:
   ```bash
   docker run -d -p 8000:8000 docling-api
   ```
3. Acesse a API em `http://<IP-da-VPS>:8000/docs`

## Deploy no Easypanel

- Basta conectar o repositório Git.
- Configure o build para usar o Dockerfile.
- A porta de exposição é 8000.

## Endpoints

- POST `/convert` : Envie um PDF e receba o Markdown.

## Requisitos

- Python 3.12
- Docker
- Easypanel

---
