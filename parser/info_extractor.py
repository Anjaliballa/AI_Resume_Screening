import re


def extract_email(text):
    """
    Extract email address.
    """

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None



def extract_phone(text):
    """
    Extract Indian phone number.
    """

    pattern = r"(\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None



def extract_name(text):
    """
    Extract candidate name.
    """

    lines = text.splitlines()


    ignored = [
        "resume",
        "curriculum vitae",
        "career objective",
        "objective",
        "email",
        "phone",
        "contact",
        "address",
        "skills",
        "education",
        "projects",
        "andhra",
        "india"
    ]


    for line in lines:

        line = line.strip()


        if not line:
            continue


        lower = line.lower()


        # Ignore unwanted lines
        if any(word in lower for word in ignored):
            continue


        # Ignore email
        if "@" in line:
            continue


        # Ignore numbers
        if re.search(r"\d", line):
            continue


        # Name should be short
        if len(line.split()) <= 4:

            return line.title()


    return None




def extract_education(text):

    """
    Extract only education section.
    """

    education = []

    keywords = [
        "b.tech",
        "btech",
        "bachelor",
        "m.tech",
        "master",
        "degree",
        "cgpa",
        "university",
        "college",
        "school",
        "pre-university"
    ]


    lines = text.splitlines()


    for line in lines:

        line=line.strip()


        if not line:
            continue


        lower=line.lower()


        if any(k in lower for k in keywords):

            if line not in education:
                education.append(line)



    return education




def extract_experience(text):

    """
    Extract experience/internship.
    """

    experience=[]


    keywords=[
        "experience",
        "internship",
        "intern",
        "worked",
        "employment"
    ]


    for line in text.splitlines():

        line=line.strip()

        lower=line.lower()


        if any(k in lower for k in keywords):

            if line not in experience:
                experience.append(line)


    return experience




def extract_projects(text):

    """
    Extract project details.
    """

    projects=[]


    keywords=[
        "project",
        "developed",
        "built",
        "implemented",
        "prediction",
        "solver"
    ]


    for line in text.splitlines():

        line=line.strip()

        lower=line.lower()


        if any(k in lower for k in keywords):

            if line not in projects:
                projects.append(line)


    return projects