from flask import Flask, render_template, request
from agent import adaptive_learning_agent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_profile = {
            "learning_style": request.form.get("learning_style"),
            "progress": request.form.get("progress"),
            "hobby": request.form.get("hobby"),
            "domain": request.form.get("domain"),
            "google_api_key": request.form.get("google_api_key"),
            "tavily_api_key": request.form.get("tavily_api_key")
        }
        result = adaptive_learning_agent.invoke(student_profile)
        return render_template("result.html", result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
