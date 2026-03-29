FROM python:3.12-slim
RUN pip install fastmcp httpx python-dotenv --no-cache-dir
WORKDIR /app
COPY server.py .
CMD ["python", "server.py"]