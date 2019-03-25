from flask import Flask, render_template, request

app = Flask(__name__)

car_model_color = {
    "BMW": "red",
    "Mercedes": "silver",
    "Lada": "Gold"
}

car_model_owner = {
    "BMW": "Jack",
    "Mercedes": "Donald",
    "Lada": "Vladimir"
}


@app.route("/")
def default():
    return render_template("default_index.html", model_color=car_model_color, model_owner=car_model_owner)


@app.route("/all")
def show_all():
    return render_template("show_all.html", model_color=car_model_color, model_owner=car_model_owner)


@app.route("/model_color")
def show_model_color():
    return render_template("show_model_color.html", model_color=car_model_color)


@app.route("/handle_model_color", methods=["POST"])
def handle():
    result_form = request.form
    return render_template("Show_new_dict.html", result=result_form)


if __name__ == "__main__":
    app.run(debug=True)
