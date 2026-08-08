import os

from flask import Flask, render_template, request, send_file

from parser.candidate_profile import create_candidate_profile
from recommender.job_loader import load_jobs
from recommender.recommendation import recommend_jobs
from reports.pdf_report_generator import generate_pdf_report


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


latest_report = None


ALLOWED_EXTENSIONS = {"pdf", "docx"}


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )



@app.route("/")
def home():

    return render_template("index.html")



@app.route("/upload", methods=["POST"])
def upload_resume():

    global latest_report


    resume = request.files["resume"]


    if resume.filename == "":
        return "No file selected!"


    if not allowed_file(resume.filename):
        return "Invalid file! Please upload a PDF or DOCX."



    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )


    # Save resume
    resume.save(file_path)



    # Extract candidate details
    profile = create_candidate_profile(
        file_path
    )



    # Load jobs
    jobs = load_jobs(
        "datasets/jobs.csv"
    )



    # Generate recommendations
    recommendations = recommend_jobs(
        profile,
        jobs
    )



    # Generate report
    latest_report = generate_pdf_report(
    profile,
    recommendations
    )



    return render_template(
        "result.html",
        profile=profile,
        recommendations=recommendations
    )




@app.route("/download_report")
def download_report():

    if latest_report:

        return send_file(
            latest_report,
            as_attachment=True
        )


    return "No report available!"




if __name__ == "__main__":

    app.run(debug=True)