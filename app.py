import os
from werkzeug.utils import secure_filename
from flask import Flask, request, flash, redirect, url_for

UPLOAD_FOLDER = "upload"
ALLEW_EXTENSIONS = ["pdf", "jpg", "mp4", "log"]
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "The security key..."

def allowed_file(filename):

    if '.' in filename:
        if filename.rsplit('.')[1] in ALLEW_EXTENSIONS:
            return True
    return False

def send_upload_form():
    FORMFILE = "form.html"
    with open(FORMFILE) as f:
        return f.read()

def show_allowed_file_extensions():
    str = "Allowed file extensions: "
    for ext in ALLEW_EXTENSIONS:
        str = str + "." + ext + "; "
    return str

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
            filename = secure_filename(file.filename)
            print filename
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for('upload_file', filename=filename))
        else:
            return show_allowed_file_extensions()

    return send_upload_form()

def main():
    app.run()

if __name__ == "__main__":
    main()
