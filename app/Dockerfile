# ─────────────────────────────────────────────────────────────────────────────
# Stage 1 — Builder
# Install dependencies in an isolated layer to keep the final image lean.
# ─────────────────────────────────────────────────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first → better Docker layer caching
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt


# ─────────────────────────────────────────────────────────────────────────────
# Stage 2 — Runtime
# Minimal final image: no build tools, no cache bloat.
# ─────────────────────────────────────────────────────────────────────────────
FROM python:3.12-slim AS runtime

# Security: run as non-root user
RUN groupadd --gid 1001 appgroup \
    && useradd  --uid 1001 --gid appgroup --shell /bin/false --create-home appuser

WORKDIR /app

# Pull installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy application source
COPY app.py .

# Runtime environment defaults (override via K8s ConfigMap / env vars)
ENV PORT=5000 \
    APP_ENV=production \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Switch to non-root
USER appuser

EXPOSE 5000

# Healthcheck — Docker itself will mark the container unhealthy if it fails
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

# Use Gunicorn for production; 4 workers, bind all interfaces
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "--timeout", "120", "--access-logfile", "-", "app:app"]
