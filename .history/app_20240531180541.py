from flask import Flask, request
import openai


# Initialize Flask app
app = Flask(__name__)

# Set GPT-4o API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define API endpoint for data analysis
@app.route("/analyze", methods=["POST"])
def analyze_data():
    # Get data from request
    data = request.json

    # Preprocess data (if necessary)

    # Use GPT-4o to generate insights
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following data: {data}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return insights as JSON response
    return jsonify({"insights": response.choices[0].text})

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
