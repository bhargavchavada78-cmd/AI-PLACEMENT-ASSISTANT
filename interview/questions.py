# interview/questions.py


QUESTIONS = {

    "Machine Learning": [

        {
            "question": "What is overfitting in machine learning?",

            "keywords": [
                "training data",
                "test data",
                "generalization",
                "poor performance",
                "regularization"
            ],

            "answer": """
            Overfitting occurs when a machine learning model learns the
            training data too closely, including noise. It performs very well
            on training data but poorly on unseen test data. It can be reduced
            using regularization, cross validation, dropout, pruning or
            collecting more data.
            """
        },

        {
            "question":
            "What is the difference between supervised and unsupervised learning?",

            "keywords": [
                "labeled data",
                "unlabeled data",
                "classification",
                "regression",
                "clustering"
            ],

            "answer": """
            Supervised learning uses labeled data and is commonly used for
            classification and regression. Unsupervised learning works with
            unlabeled data and is commonly used for clustering and finding
            hidden patterns.
            """
        },

        {
            "question": "What is gradient descent?",

            "keywords": [
                "optimization",
                "loss function",
                "gradient",
                "learning rate",
                "minimum"
            ],

            "answer": """
            Gradient descent is an optimization algorithm used to minimize
            a loss function. It calculates the gradient of the loss and
            updates model parameters in the opposite direction. The learning
            rate controls the size of each update.
            """
        },

        {
            "question":
            "What is the difference between classification and regression?",

            "keywords": [
                "classification",
                "regression",
                "categorical",
                "continuous",
                "prediction"
            ],

            "answer": """
            Classification predicts categorical values such as spam or
            not spam. Regression predicts continuous numerical values such
            as house prices or temperature.
            """
        },

        {
            "question": "What is cross validation?",

            "keywords": [
                "training",
                "validation",
                "fold",
                "model evaluation",
                "data"
            ],

            "answer": """
            Cross validation is a model evaluation technique in which the
            dataset is divided into multiple parts called folds. The model
            is trained and validated multiple times using different folds.
            It helps estimate how well the model generalizes to unseen data.
            """
        }

    ],


    "Python": [

        {
            "question":
            "What is the difference between a list and a tuple in Python?",

            "keywords": [
                "list",
                "tuple",
                "mutable",
                "immutable"
            ],

            "answer": """
            A list is mutable, meaning its elements can be changed after
            creation. A tuple is immutable. Lists use square brackets while
            tuples commonly use parentheses.
            """
        },

        {
            "question": "What is a dictionary in Python?",

            "keywords": [
                "key",
                "value",
                "key value pair",
                "mapping"
            ],

            "answer": """
            A dictionary is a mutable mapping data structure that stores
            information using key-value pairs. Keys are used to access
            corresponding values.
            """
        },

        {
            "question": "What is a function in Python?",

            "keywords": [
                "function",
                "def",
                "code",
                "reuse",
                "parameters"
            ],

            "answer": """
            A function is a reusable block of code that performs a specific
            task. In Python, functions are commonly created using the def
            keyword. Functions can accept parameters and return values.
            """
        },

        {
            "question": "What is the difference between == and is in Python?",

            "keywords": [
                "equality",
                "identity",
                "value",
                "object"
            ],

            "answer": """
            The == operator checks whether two objects have equal values,
            while the is operator checks whether two variables refer to the
            same object in memory.
            """
        }

    ],


    "NLP": [

        {
            "question": "What is TF-IDF?",

            "keywords": [
                "term frequency",
                "inverse document frequency",
                "word importance",
                "document",
                "corpus"
            ],

            "answer": """
            TF-IDF stands for Term Frequency-Inverse Document Frequency.
            It measures how important a word is in a document relative to
            a collection of documents.
            """
        },

        {
            "question": "What is tokenization in NLP?",

            "keywords": [
                "token",
                "text",
                "words",
                "sentences",
                "split"
            ],

            "answer": """
            Tokenization is the process of breaking text into smaller units
            called tokens. Tokens can be words, sentences or subwords.
            """
        },

        {
            "question": "What is stemming in NLP?",

            "keywords": [
                "stemming",
                "word",
                "root",
                "suffix",
                "text"
            ],

            "answer": """
            Stemming is an NLP technique that reduces words to a basic root
            form by removing prefixes or suffixes. The resulting form may
            not always be a valid dictionary word.
            """
        },

        {
            "question": "What is the difference between stemming and lemmatization?",

            "keywords": [
                "stemming",
                "lemmatization",
                "root",
                "dictionary",
                "word"
            ],

            "answer": """
            Stemming removes word endings using simple rules, while
            lemmatization uses vocabulary and linguistic information to
            return a meaningful base form of a word.
            """
        }

    ]
}


# =========================================================
# GET QUESTIONS
# =========================================================

def get_questions(role):

    return QUESTIONS.get(role, [])