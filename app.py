import os
from flask import Flask, request, flash, redirect, url_for

UPLOAD_FOLDER = "upload"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "The security key..."

def allowed_file(filename):
    ALLEW_EXTENSIONS = ["pdf", "jpg", "mp4", "log"]

    if '.' in filename:
        if filename.rsplit('.')[1] in ALLEW_EXTENSIONS:
            return True
    return False

def send_upload_form():
    FORMFILE = "form.html"

    with open(FORMFILE) as f:
        return f.read()

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part...")
            return redirect(request.url)

        file = request.files['file']
        if file.filename == "":
            flash("No file selected...")
            return redirect(request.url)

        if allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for('upload_file', filename=filename))

    return send_upload_form()

def main():
    app.run()

if __name__ == "__main__":
    main()
