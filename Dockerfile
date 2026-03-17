# ---- Base Image ----
FROM python:3.12-slim

# ---- Environment ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- Install system deps ----
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ---- Install uv ----
RUN pip install uv

# ---- Set workdir ----
WORKDIR /app

# ---- Copy project ----
COPY . .

# ---- Install dependencies via uv ----
RUN uv pip install --system -r pyproject.toml

# ---- Expose port ----
EXPOSE 8080

# ---- Run app ----
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]