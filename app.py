from flask import Flask, render_template, request
import os

from extractor import extract_metadata
from hash_generator import generate_hash


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )



@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(path)


    metadata = extract_metadata(path)

    metadata.update(
        generate_hash(path)
    )


    return render_template(
        "index.html",
        metadata=metadata
    )


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)