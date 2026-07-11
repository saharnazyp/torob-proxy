from flask import Flask, request, jsonify
import httpx

app = Flask(__name__)

@app.route("/")
def search():
    query = request.args.get("query", "")
    page = request.args.get("page", "0")
    url = f"https://api.torob.com/v4/base-product/search/?query={query}&page={page}"
    H = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "fa-IR,fa;q=0.9",
        "Referer": "https://torob.com/",
    }
    try:
        r = httpx.get(url, headers=H, timeout=20)
        if "json" in r.headers.get("content-type", ""):
            return jsonify(r.json())
        else:
            return jsonify({"error": "not_json", "status": r.status_code, "body": r.text[:200]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
