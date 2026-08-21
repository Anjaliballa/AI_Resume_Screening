# recommender/career_roadmap.py


CAREER_ROADMAPS = {

    "machine learning": {
        "career": "Machine Learning Engineer",

        "phases": [
            {
                "phase": 1,
                "title": "Strengthen Python & Data Skills",
                "skills": [
                    "python",
                    "numpy",
                    "pandas",
                    "sql"
                ],
                "projects": [
                    "Build a data analysis project",
                    "Build a Python data preprocessing pipeline"
                ]
            },

            {
                "phase": 2,
                "title": "Master Machine Learning",
                "skills": [
                    "machine learning",
                    "scikit-learn",
                    "feature engineering",
                    "model evaluation"
                ],
                "projects": [
                    "Build a customer churn prediction system",
                    "Build a house price prediction system"
                ]
            },

            {
                "phase": 3,
                "title": "Learn Deep Learning",
                "skills": [
                    "deep learning",
                    "neural networks",
                    "pytorch",
                    "tensorflow"
                ],
                "projects": [
                    "Build an image classification system",
                    "Build a neural network from scratch"
                ]
            },

            {
                "phase": 4,
                "title": "Build Real-World ML Projects",
                "skills": [
                    "model deployment",
                    "flask",
                    "REST APIs",
                    "git",
                    "github"
                ],
                "projects": [
                    "Deploy an ML model using Flask",
                    "Build an end-to-end ML application"
                ]
            }
        ]
    },


    "data science": {
        "career": "Data Scientist",

        "phases": [
            {
                "phase": 1,
                "title": "Data Analysis Foundations",
                "skills": [
                    "python",
                    "numpy",
                    "pandas",
                    "sql"
                ],
                "projects": [
                    "Build an exploratory data analysis project",
                    "Analyze a real-world dataset"
                ]
            },

            {
                "phase": 2,
                "title": "Statistics & Machine Learning",
                "skills": [
                    "statistics",
                    "machine learning",
                    "scikit-learn",
                    "model evaluation"
                ],
                "projects": [
                    "Build a classification model",
                    "Build a regression model"
                ]
            },

            {
                "phase": 3,
                "title": "Advanced Data Science",
                "skills": [
                    "feature engineering",
                    "data visualization",
                    "ensemble learning",
                    "model optimization"
                ],
                "projects": [
                    "Build a predictive analytics system",
                    "Build a complete data science pipeline"
                ]
            },

            {
                "phase": 4,
                "title": "Portfolio & Deployment",
                "skills": [
                    "flask",
                    "REST APIs",
                    "git",
                    "github"
                ],
                "projects": [
                    "Deploy a machine learning project",
                    "Create a professional GitHub portfolio"
                ]
            }
        ]
    },


    "python developer": {
        "career": "Python Developer",

        "phases": [
            {
                "phase": 1,
                "title": "Python Fundamentals",
                "skills": [
                    "python",
                    "object-oriented programming",
                    "data structures"
                ],
                "projects": [
                    "Build a command-line application",
                    "Build a Python automation project"
                ]
            },

            {
                "phase": 2,
                "title": "Backend Development",
                "skills": [
                    "flask",
                    "REST APIs",
                    "sql",
                    "databases"
                ],
                "projects": [
                    "Build a Flask REST API",
                    "Build a database-backed web application"
                ]
            },

            {
                "phase": 3,
                "title": "Production Skills",
                "skills": [
                    "git",
                    "github",
                    "testing",
                    "api development"
                ],
                "projects": [
                    "Build and test a production-style API",
                    "Deploy a Flask application"
                ]
            }
        ]
    },


    "ai": {
        "career": "AI Engineer",

        "phases": [
            {
                "phase": 1,
                "title": "AI Foundations",
                "skills": [
                    "python",
                    "machine learning",
                    "statistics"
                ],
                "projects": [
                    "Build a machine learning prediction system",
                    "Build an intelligent classification system"
                ]
            },

            {
                "phase": 2,
                "title": "Computer Vision & Deep Learning",
                "skills": [
                    "computer vision",
                    "opencv",
                    "deep learning",
                    "pytorch"
                ],
                "projects": [
                    "Build an image classification system",
                    "Build an object detection project"
                ]
            },

            {
                "phase": 3,
                "title": "Advanced AI Applications",
                "skills": [
                    "neural networks",
                    "transformers",
                    "model deployment"
                ],
                "projects": [
                    "Build an AI-powered application",
                    "Deploy an AI model as an API"
                ]
            }
        ]
    },


    "computer vision": {
        "career": "Computer Vision Engineer",

        "phases": [
            {
                "phase": 1,
                "title": "Image Processing",
                "skills": [
                    "python",
                    "opencv",
                    "image processing"
                ],
                "projects": [
                    "Build an image processing application",
                    "Build a color detection system"
                ]
            },

            {
                "phase": 2,
                "title": "Deep Learning for Vision",
                "skills": [
                    "machine learning",
                    "deep learning",
                    "cnns",
                    "pytorch"
                ],
                "projects": [
                    "Build an image classifier",
                    "Build an object detection system"
                ]
            },

            {
                "phase": 3,
                "title": "Advanced Computer Vision",
                "skills": [
                    "object detection",
                    "image segmentation",
                    "computer vision"
                ],
                "projects": [
                    "Build a real-time object detection system",
                    "Build an image segmentation project"
                ]
            }
        ]
    },


    "nlp": {
        "career": "NLP Engineer",

        "phases": [
            {
                "phase": 1,
                "title": "NLP Fundamentals",
                "skills": [
                    "python",
                    "nlp",
                    "nltk",
                    "text preprocessing"
                ],
                "projects": [
                    "Build a sentiment analysis system",
                    "Build a text classification system"
                ]
            },

            {
                "phase": 2,
                "title": "Advanced NLP",
                "skills": [
                    "spacy",
                    "word embeddings",
                    "tf-idf",
                    "machine learning"
                ],
                "projects": [
                    "Build a named entity recognition system",
                    "Build a document classification system"
                ]
            },

            {
                "phase": 3,
                "title": "Modern NLP",
                "skills": [
                    "transformers",
                    "bert",
                    "deep learning",
                    "pytorch"
                ],
                "projects": [
                    "Build a transformer-based NLP application",
                    "Build a question-answering system"
                ]
            }
        ]
    }
}


def find_career_roadmap(job_title):
    """
    Find the correct roadmap for a job title.
    """

    title = job_title.lower().strip()

    # Machine Learning / ML Engineer
    if (
        "machine learning" in title
        or "ml engineer" in title
        or title.startswith("ml ")
        or "ml intern" in title
    ):
        return CAREER_ROADMAPS["machine learning"]

    # Data Science
    if (
        "data science" in title
        or "data scientist" in title
    ):
        return CAREER_ROADMAPS["data science"]

    # Python Developer
    if "python developer" in title:
        return CAREER_ROADMAPS["python developer"]

    # Computer Vision
    if "computer vision" in title:
        return CAREER_ROADMAPS["computer vision"]

    # NLP
    if (
        "nlp" in title
        or "natural language" in title
    ):
        return CAREER_ROADMAPS["nlp"]

    # AI
    if (
        title.startswith("ai ")
        or " ai " in f" {title} "
        or "artificial intelligence" in title
    ):
        return CAREER_ROADMAPS["ai"]

    return None


def generate_career_roadmap(
    job_title,
    candidate_skills,
    missing_skills,
    skill_priorities
):
    """
    Generate a personalized career roadmap.
    """

    roadmap = find_career_roadmap(job_title)

    # Fallback roadmap
    if roadmap is None:

        roadmap = {
            "career": job_title,

            "phases": [
                {
                    "phase": 1,
                    "title": "Learn Required Skills",
                    "skills": missing_skills,
                    "projects": [
                        f"Build a project using {job_title}"
                    ]
                }
            ]
        }

    candidate_skills = set(
        skill.lower().strip()
        for skill in candidate_skills
    )

    personalized_phases = []

    for phase in roadmap["phases"]:

        required_phase_skills = [
            skill.lower().strip()
            for skill in phase["skills"]
        ]

        completed_skills = [
            skill
            for skill in required_phase_skills
            if skill in candidate_skills
        ]

        remaining_skills = [
            skill
            for skill in required_phase_skills
            if skill not in candidate_skills
        ]

        if required_phase_skills:

            completion = (
                len(completed_skills)
                / len(required_phase_skills)
            ) * 100

        else:

            completion = 100

        personalized_phases.append({

            "phase": phase["phase"],

            "title": phase["title"],

            "completion": round(
                completion,
                2
            ),

            "completed_skills":
                completed_skills,

            "remaining_skills":
                remaining_skills,

            "projects":
                phase["projects"]

        })

    all_required_skills = set()

    for phase in roadmap["phases"]:

        for skill in phase["skills"]:

            all_required_skills.add(
                skill.lower().strip()
            )

    matched_roadmap_skills = (
        candidate_skills
        .intersection(all_required_skills)
    )

    if all_required_skills:

        overall_coverage = (
            len(matched_roadmap_skills)
            / len(all_required_skills)
        ) * 100

    else:

        overall_coverage = 0

    return {

        "career": roadmap["career"],

        "job_title": job_title,

        "overall_skill_coverage":
            round(
                overall_coverage,
                2
            ),

        "priority_skills":
            skill_priorities,

        "phases":
            personalized_phases

    }
