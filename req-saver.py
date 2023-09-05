from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the log file where requests will be saved.
log_file = "request_log.txt"

# Create a custom request handler by inheriting from BaseHTTPRequestHandler.
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log the incoming GET request.
        request_info = f"{self.address_string()} - {self.date_time_string()}: {self.path}\n"
        with open(log_file, "a") as log:
            log.write(request_info)

        # Send a response back to the client.
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Request logged successfully")

# Define the server's host and port.
host = "https://sts-tt-cc.netlify.app"  # Change to your server's address if needed
port = 80 or 433

# Create an HTTP server with the custom request handler.
server = HTTPServer((host, port), RequestHandler)
print(f"Server started on http://{host}:{port}")

# Serve requests indefinitely.
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

# Close the server gracefully.
server.server_close()
print("Server Error")
