try:
    from flask import Flask
except ImportError:
    # Fallback minimal Flask-like implementation so the app can run
    # even if the 'flask' package is not installed (useful for editors/linters).
    from wsgiref.simple_server import make_server

    class Flask:
        def __init__(self, name):
            self._routes = {}

        def route(self, path):
            def decorator(f):
                self._routes[path] = f
                return f
            return decorator

        def run(self, host="0.0.0.0", port=5000):
            def app(environ, start_response):
                path = environ.get("PATH_INFO", "/")
                handler = self._routes.get(path)
                if handler:
                    body = handler()
                    if isinstance(body, str):
                        body = body.encode("utf-8")
                    start_response("200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(body)))])
                    return [body]
                start_response("404 Not Found", [("Content-Type", "text/plain")])
                return [b"Not Found"]

            print("Flask not installed. Running with wsgiref.simple_server fallback.")
            make_server(host, port, app).serve_forever()

app = Flask(__name__)

@app.route("/")
def home():
    return "Employee Management Application"

@app.route("/health")
def health():
    return "Application Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
