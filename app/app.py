"""
Retail API - Cloud-Native Demo Application
A production-style Flask REST API for a retail store.
"""

import os
import time
import logging
from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

# ─── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
)
logger = logging.getLogger("retail-api")

# ─── App Bootstrap ────────────────────────────────────────────────────────────
app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Static info metric exposed on /metrics
metrics.info("retail_app_info", "Retail API metadata", version="1.0.0")

# ─── Data Store (in-memory) ───────────────────────────────────────────────────
PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones",  "category": "Electronics", "price": 79.99,  "stock": 142},
    {"id": 2, "name": "Running Shoes",          "category": "Footwear",    "price": 119.99, "stock": 85},
    {"id": 3, "name": "Coffee Maker",           "category": "Appliances",  "price": 49.99,  "stock": 63},
    {"id": 4, "name": "Yoga Mat",               "category": "Sports",      "price": 29.99,  "stock": 210},
    {"id": 5, "name": "Backpack",               "category": "Bags",        "price": 59.99,  "stock": 97},
    {"id": 6, "name": "Sunglasses",             "category": "Accessories", "price": 39.99,  "stock": 180},
    {"id": 7, "name": "Bluetooth Speaker",      "category": "Electronics", "price": 89.99,  "stock": 54},
    {"id": 8, "name": "Smartwatch",             "category": "Electronics", "price": 199.99, "stock": 38},
]

START_TIME = time.time()

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    return jsonify({
        "service": "Retail API",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "production"),
        "endpoints": ["/", "/products", "/products/<id>", "/health", "/metrics"],
    })


@app.route("/products")
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [p for p in PRODUCTS if p["category"].lower() == category.lower()]
        return jsonify({"count": len(filtered), "products": filtered})
    return jsonify({"count": len(PRODUCTS), "products": PRODUCTS})


@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found", "id": product_id}), 404
    return jsonify(product)


@app.route("/health")
def health():
    uptime = round(time.time() - START_TIME, 2)
    return jsonify({
        "status": "healthy",
        "uptime_seconds": uptime,
        "pod": os.getenv("HOSTNAME", "local"),
        "environment": os.getenv("APP_ENV", "production"),
    })


@app.route("/ready")
def ready():
    """Kubernetes readiness probe endpoint."""
    return jsonify({"status": "API-ready"}), 200


# ─── Error Handlers ───────────────────────────────────────────────────────────

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def server_error(e):
    logger.error("Internal server error: %s", str(e))
    return jsonify({"error": "Internal server error"}), 500


# ─── Entrypoint ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    logger.info("Starting Retail API on port %d (debug=%s)", port, debug)
    app.run(host="0.0.0.0", port=port, debug=debug)
