import os
from datetime import datetime


def generate_report(profile, recommendations):

    report_folder = "reports/generated"

    # Create folder if it does not exist
    os.makedirs(
        report_folder,
        exist_ok=True
    )

    filename = (
        "resume_analysis_report_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".txt"
    )

    file_path = os.path.join(
        report_folder,
        filename
    )


    with open(file_path, "w", encoding="utf-8") as file:


        file.write(
            "=================================\n"
        )

        file.write(
            " AI Resume Screening Report\n"
        )

        file.write(
            "=================================\n\n"
        )


        file.write("Candidate Information\n")
        file.write("---------------------\n")

        file.write(
            f"Name: {profile['name']}\n"
        )

        file.write(
            f"Email: {profile['email']}\n"
        )

        file.write(
            f"Phone: {profile['phone']}\n\n"
        )


        file.write("Skills\n")
        file.write("------\n")

        for skill in profile["skills"]:

            file.write(
                f"- {skill}\n"
            )


        file.write("\nEducation\n")
        file.write("---------\n")

        for edu in profile["education"]:

            file.write(
                f"- {edu}\n"
            )


        file.write("\nProjects\n")
        file.write("--------\n")

        for project in profile["projects"]:

            file.write(
                f"- {project}\n"
            )


        file.write("\n\nRecommended Jobs\n")
        file.write("----------------\n")


        for index, job in enumerate(
            recommendations[:5],
            start=1
        ):

            file.write(
                f"\n{index}. {job['job_title']}\n"
            )

            file.write(
                f"Company: {job['company']}\n"
            )

            file.write(
                f"Match Score: {job['score']}%\n"
            )


    return file_path
    