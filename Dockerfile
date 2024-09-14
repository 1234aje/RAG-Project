FROM python:3.10-slim
WORKDIR /app
COPY requirement.txt /app/

RUN pip install --no-cache-dir -r requirement.txt

COPY . /app/

EXPOSE 8501  

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.headless=true"]
