import os
import sentry_sdk

from bottle import Bottle, run, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration


## Введите вашу ссылку dsn
sentry_sdk.init(
    dsn="ENTER_YOUR_DSN",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/success')
def index():
    return HTTPResponse(status=200, body="Успешный запрос")

@app.route('/')
def index():
    return HTTPResponse(status=200, body="Вы на главной странице.")

@app.route('/fail')
def index():
    raise RuntimeError("Oppps,Server error!")
    return HTTPResponse(status=500, body="Fail request")


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8081, debug=True)
