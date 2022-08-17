FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN adduser -u 5000 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD ["python", "app.py"]
