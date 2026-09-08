"""
Alem Trans.KZ — телефон/заявка формасынан Telegram-ге хабарлама жіберетін кіші backend.

Жергілікті іске қосу:
    pip install -r requirements.txt
    BOT_TOKEN=... CHAT_ID=... python telegram-bot.py

Railway/сервер жағдайында BOT_TOKEN мен CHAT_ID мәндерін коды ЕМЕС, платформаның
Environment Variables бөлімінде сақтаңыз (репозиторий public болғандықтан токен
кодта тұрмауы керек). Алу қадамдары — INSTALLATION.md.
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")

TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/sendMessage"

app = Flask(__name__)
CORS(app)


def build_message(data):
    return (
        "📦 Новая заявка — Alem Trans.KZ\n\n"
        f"Имя: {data.get('name', '-')}\n"
        f"Телефон: {data.get('phone', '-')}\n"
        f"Откуда: {data.get('from', '-')}\n"
        f"Куда: {data.get('to', '-')}\n"
        f"Груз: {data.get('cargo', '-')}\n"
        f"Комментарий: {data.get('comment', '-')}"
    )


@app.route("/api/order", methods=["POST"])
def order():
    if not BOT_TOKEN or not CHAT_ID:
        return jsonify({"ok": False, "error": "BOT_TOKEN/CHAT_ID not configured on server"}), 500

    data = request.get_json(silent=True) or {}

    name = (data.get("name") or "").strip()
    phone = (data.get("phone") or "").strip()

    if not name or not phone:
        return jsonify({"ok": False, "error": "name and phone are required"}), 400

    message = build_message(data)
    url = TELEGRAM_API_URL.format(token=BOT_TOKEN)

    try:
        response = requests.post(
            url,
            json={"chat_id": CHAT_ID, "text": message},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        return jsonify({"ok": False, "error": f"telegram request failed: {exc}"}), 502

    return jsonify({"ok": True})


@app.route("/api/order", methods=["GET"])
def order_health():
    return jsonify({"ok": True, "message": "Order endpoint is running. Use POST to submit."})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
