from flask import Flask, request, jsonify, redirect

from datetime import datetime, timedelta

from database import db

from extensions import ma

app = Flask(__name__)

app.config.from_object("config.Config")

db.init_app(app)
ma.init_app(app)

from models import Link

from schemas import LinkSchema
from utils import generateShortId

@app.before_request
def setup():
    app.before_request_funcs[None].remove(setup)

    db.create_all()

linkSchema = LinkSchema()

@app.route("/links", methods=["POST"])
def createLink():
    data = request.get_json()
    # errors = linkSchema.validate(data)

    # if errors:
    #     return jsonify(errors), 400 

    url = data["url"]

    expiresAt = datetime.utcnow() + timedelta(days=7) # 7 days 

    shortUrl = generateShortId()

    newUrl = Link(original_url=url, short_url=shortUrl, expires_at=expiresAt)

    db.session.add(newUrl)
    db.session.commit()

    return jsonify({
        "url": f"http://localhost:5000/r/{shortUrl}"
    }), 201

@app.route("/r/<shortenedUrl>", methods=["GET"])
def getLink(shortenedUrl):
    url = Link.query.filter_by(short_url=shortenedUrl).first()

    if not url:
        return jsonify({
            "error": "URL not found"
        }), 400

    if datetime.utcnow() > url.expires_at:
        return jsonify({
            "error": "Link is expired"
        }), 400

    return redirect(url.original_url)

if __name__ == "__main__":
    app.run(debug=True)