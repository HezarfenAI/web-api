# Base image
FROM python:3.10-slim

# Ortam değişkenleri
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Sistem paketlerini yükle
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Poetry yükle
RUN curl -sSL https://install.python-poetry.org | python3 -

# PATH'e ekle
ENV PATH="/root/.local/bin:$PATH"

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılık dosyalarını kopyala
COPY pyproject.toml poetry.lock* /app/

# Bağımlılıkları kur
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Uygulama dosyalarını kopyala
COPY . /app

# Uvicorn ile başlat
CMD ["poetry", "run", "python", "src/main.py"]
