from .app import app
import os

if __name__ == '__main__':
    port = os.environ.get("PORT", 5050)
    app.run(host="0.0.0.0", port=port)

def main():
    port = os.environ.get("PORT", 5050)
    app.run(host="0.0.0.0", port=port)
    #app.run(debug=True, host = '0.0.0.0', port=5050)