from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

default_medications = {
    1: {"name": "Cefixime", "dose_per_kg": 8, "concentration": 100, "volume_unit": 5, "interval": "Every 12 hours"},
    2: {"name": "Azithromycin", "dose_per_kg": 10, "concentration": 200, "volume_unit": 5, "interval": "Once daily"},
    3: {"name": "Prednisolone", "dose_per_kg": 15, "concentration": 15, "volume_unit": 5, "interval": "Once daily"},
    # أضف المزيد من الأدوية هنا
}

@app.route('/')
def index():
    return render_template('index.html', medications=default_medications)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        dose_per_kg = float(request.form['dose_per_kg'])
        concentration = float(request.form['concentration'])

        total_dose = weight * dose_per_kg
        volume_required = total_dose / concentration

        result = {
            'total_dose': f"{total_dose:.2f}",
            'volume_required': f"{volume_required:.2f}"
        }

        return jsonify(result)

    except ValueError:
        return jsonify({"error": "Please enter valid numeric values."})

if __name__ == "__main__":
    app.run(debug=True)

