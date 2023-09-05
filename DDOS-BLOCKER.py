from flask import Flask, request, jsonify, abort
from collections import defaultdict

app = Flask(__name__)

# Create a dictionary to store request counts for each IP address.
ip_request_count = defaultdict(int)

# Define the maximum allowed requests per IP.
MAX_REQUESTS = 1500

@app.route('/')
def hello_world():
    # Get the user's IP address from the request.
    user_ip = request.remote_addr

    # Check if the IP has exceeded the maximum allowed requests.
    if ip_request_count[user_ip] >= MAX_REQUESTS:
        # Block the IP address.
        block_ip(user_ip)
        return "Your IP address has been blocked due to excessive requests."

    # Process the request.
    ip_request_count[user_ip] += 1
    return "Hello, World!"

def block_ip(ip_address):
    # In a real implementation, you might add the blocked IP to a database or firewall rule.
    # For this simplified example, we'll just print a message.
    print(f"Blocking IP: {ip_address}")

if __name__ == '__main__':
    app.run(debug=True)
