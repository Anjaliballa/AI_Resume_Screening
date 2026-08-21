LEARNING_PATHS = {

    "python": [
        "Python fundamentals",
        "Functions and modules",
        "Object-Oriented Programming",
        "File handling and APIs"
    ],

    "machine learning": [
        "Machine Learning fundamentals",
        "Supervised and unsupervised learning",
        "Model evaluation",
        "Feature engineering"
    ],

    "scikit-learn": [
        "Scikit-learn fundamentals",
        "Data preprocessing",
        "Model training",
        "Model evaluation and pipelines"
    ],

    "deep learning": [
        "Neural network fundamentals",
        "Forward propagation and backpropagation",
        "CNNs and RNNs",
        "Deep learning model training"
    ],

    "pytorch": [
        "PyTorch fundamentals",
        "Tensors and datasets",
        "Neural network implementation",
        "Model training with PyTorch"
    ],

    "tensorflow": [
        "TensorFlow fundamentals",
        "Keras API",
        "Neural network construction",
        "Model training and evaluation"
    ],

    "nlp": [
        "NLP fundamentals",
        "Text preprocessing",
        "TF-IDF and word embeddings",
        "Transformer fundamentals"
    ],

    "nltk": [
        "NLTK fundamentals",
        "Tokenization",
        "Stemming and lemmatization",
        "Text classification"
    ],

    "spacy": [
        "spaCy fundamentals",
        "Named Entity Recognition",
        "Part-of-speech tagging",
        "NLP pipelines"
    ],

    "opencv": [
        "OpenCV fundamentals",
        "Image processing",
        "Feature detection",
        "Computer vision applications"
    ],

    "computer vision": [
        "Computer vision fundamentals",
        "Image processing",
        "Feature extraction",
        "Object detection"
    ],

    "flask": [
        "Flask fundamentals",
        "REST APIs",
        "Routing and templates",
        "Deploying Flask applications"
    ],

    "javascript": [
        "JavaScript fundamentals",
        "DOM manipulation",
        "Async programming",
        "Modern JavaScript"
    ],

    "java": [
        "Java fundamentals",
        "Object-oriented programming",
        "Collections framework",
        "Exception handling"
    ],

    "data structures": [
        "Arrays and strings",
        "Linked lists",
        "Stacks and queues",
        "Trees and graphs",
        "Sorting and searching"
    ],

    "excel": [
        "Excel fundamentals",
        "Formulas and functions",
        "Pivot tables",
        "Data analysis"
    ]
}


def generate_learning_recommendations(
    skill_priorities
):
    """
    Generate learning recommendations
    based on missing skill priorities.
    """

    recommendations = []

    for skill, information in skill_priorities.items():

        priority = information["priority"]
        score = information["score"]

        learning_path = LEARNING_PATHS.get(
            skill,
            [
                f"{skill} fundamentals",
                f"Practical {skill} exercises",
                f"Build a project using {skill}"
            ]
        )

        recommendations.append({

            "skill": skill,

            "priority": priority,

            "priority_score": score,

            "learning_path": learning_path

        })

    # Highest priority first

    recommendations.sort(
        key=lambda x: x["priority_score"],
        reverse=True
    )

    return recommendations
