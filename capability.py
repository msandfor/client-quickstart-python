from flask import Flask, Response
from twilio.jwt.client import ClientCapabilityToken

app = Flask(__name__)


@app.route('/token', methods=['GET'])
def get_capability_token():
    """Respond to incoming requests."""

    # Find these values at twilio.com/console
    account_sid = 'ACab62879858e561e0bee754b4beb4363f'
    auth_token = '09eddc4f6d8fc25860589d648f1f5fa8'

    capability = ClientCapabilityToken(account_sid, auth_token)

    # Twilio Application Sid
    application_sid = 'AP32bea3e2b14a2063a3bbc7fe36489eb3'
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming('joey')
    token = capability.to_jwt()

    return Response(token, mimetype='application/jwt')


if __name__ == "__main__":
    app.run(debug=True)