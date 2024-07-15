import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/trigger', methods=['POST'])
def trigger_script():
    api_url = 'https://YOUR_API_GATEWAY_URL'  # Replace with your API Gateway URL
    try:
        response = requests.post(api_url)
        response.raise_for_status()
        return jsonify({'message': 'Script triggered successfully', 'data': response.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Failed to trigger script', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
