from flask import Flask, render_template, request, send_file
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        barcode_class = barcode.get_barcode_class('code128')
        my_code = barcode_class(data, writer=ImageWriter())

        buffer = BytesIO()
        my_code.write(buffer)
        buffer.seek(0)

        return send_file(buffer, mimetype='image/png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
