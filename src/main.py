from flask import Flask, render_template, redirect, url_for, flash, request
from organizer import organize_files

app = Flask(__name__)
app.secret_key = 'dev'  # change for production

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/organize', methods=['POST'])
def organize():
    source = request.form.get('source')
    destination = request.form.get('destination')

    if not source or not destination:
        flash('Please provide both source and destination folders', 'danger')
        return redirect(url_for('index'))

    config = {
        "source_folder": source,
        "destination_folder": destination,
        "extensions": {
            "jpg": "Images",
            "jpeg": "Images",
            "png": "Images",
            "gif": "Images",
            "pdf": "Documents",
            "docx": "Documents",
            "doc": "Documents",
            "xlsx": "Spreadsheets",
            "csv": "Spreadsheets",
            "mp4": "Videos",
            "mp3": "Audio",
            "default": "Others"
        }
    }

    try:
        moved = organize_files(config)
        flash(f'✅ Organized {moved} files', 'success')
    except Exception as e:
        flash(f'Error: {e}', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
