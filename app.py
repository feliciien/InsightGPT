from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Gemini API key and endpoint
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_ENDPOINT = "https://api.gemini.com/v1/analyze"  # Replace with actual Gemini API endpoint

@app.route("/analyze", methods=["POST"])
def analyze_data():
    data = request.json.get("query")
    
    # Call the Gemini API
    response = requests.post(
        GEMINI_API_ENDPOINT,
        headers={"Authorization": "Bearer AIzaSyAGWOcLqVk7-Rbhql6We6Qp2Kc_GnslKm4"},
        json={"query": data}
    )
    
    if response.status_code == 200:
        insights = response.json().get("insights")
        return jsonify({"insights": insights})
    else:
        return jsonify({"error": "Failed to fetch insights"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
