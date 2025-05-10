from flask import Flask, request, Response
import requests

app = Flask(__name__)

# List of backend services
backends = ['http://localhost:9001', 'http://localhost:9002']
counter = 0

@app.route('/', methods=['GET', 'POST'])
def load_balance():
    global counter
    backend = backends[counter % len(backends)]
    counter += 1

    # Forward request to chosen backend
    try:
        resp = requests.request(
            method=request.method,
            url=f"{backend}{request.path}",
            headers={key: value for key, value in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False)

        response = Response(resp.content, resp.status_code)
        for key, value in resp.headers.items():
            response.headers[key] = value
        return response
    except Exception as e:
        return Response(f"Error connecting to backend: {str(e)}", status=502)

if __name__ == '__main__':
    app.run(port=9000)
