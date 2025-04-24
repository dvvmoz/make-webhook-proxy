from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MAKE_WEBHOOK_URL = "https://hook.eu2.make.com/5uptioo1i4fu7vrsple9rn35f322ld6y"

@app.route('/send', methods=['POST'])
def send_to_make():
    data = request.get_json()
    print(f"Received from Replit: {data}")

    try:
        r = requests.post(MAKE_WEBHOOK_URL, json=data)
        return jsonify({
            "status": "forwarded",
            "make_status": r.status_code,
            "make_response": r.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
