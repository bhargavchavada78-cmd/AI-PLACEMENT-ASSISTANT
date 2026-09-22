import re
import PyPDF2


def extract_text(uploaded_file):

    reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def clean_text(text):

    text = text.lower()

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(
        r'[^a-z0-9+#.\s]',
        ' ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()


def extract_skills(text):

    skills_database = [
        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "html",
        "css",
        "sql",
        "mysql",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "nlp",
        "tensorflow",
        "keras",
        "pytorch",
        "ann",
        "cnn",
        "rnn",
        "lstm",
        "flask",
        "streamlit",
        "git",
        "github",
        "docker",
        "aws",
        "statistics"
    ]

    found_skills = []

    for skill in skills_database:

        if skill in text:
            found_skills.append(skill)

    return found_skills


def detect_sections(text):

    sections = {

        "summary": [
            "summary",
            "profile",
            "objective"
        ],

        "education": [
            "education",
            "academic",
            "qualification",
            "degree"
        ],

        "skills": [
            "skills",
            "technical skills"
        ],

        "projects": [
            "projects",
            "academic projects",
            "personal projects"
        ],

        "experience": [
            "experience",
            "work experience",
            "internship"
        ],

        "certifications": [
            "certification",
            "certifications"
        ]
    }

    found_sections = {}

    for section, keywords in sections.items():

        found_sections[section] = False

        for keyword in keywords:

            if keyword in text:

                found_sections[section] = True

                break

    return found_sections


def match_job_description(
    resume_text,
    job_description
):

    skills_database = [
        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "html",
        "css",
        "sql",
        "mysql",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "nlp",
        "tensorflow",
        "keras",
        "pytorch",
        "ann",
        "cnn",
        "rnn",
        "lstm",
        "flask",
        "streamlit",
        "git",
        "github",
        "docker",
        "aws",
        "statistics"
    ]

    matched_skills = []

    missing_skills = []

    for skill in skills_database:

        if skill in job_description:

            if skill in resume_text:

                matched_skills.append(skill)

            else:

                missing_skills.append(skill)

    return matched_skills, missing_skills


def calculate_ats_score(
    matched_skills,
    missing_skills
):

    total_skills = (
        len(matched_skills)
        + len(missing_skills)
    )

    if total_skills == 0:
        return 0

    score = (
        len(matched_skills)
        / total_skills
    ) * 100

    return round(score, 2)