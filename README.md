# resume-screening
NLP Resume Screening Web App
Overview
This project is a web application designed for automated resume screening using Natural Language Processing (NLP) techniques. The application leverages advanced NLP methods to analyze and classify resumes into predefined categories, providing a seamless experience for resume evaluation.

Features
Resume Upload: Users can upload resumes in .txt or .pdf formats.
Resume Cleaning: The uploaded resumes are cleaned by removing unnecessary elements such as URLs, hashtags, mentions, special characters, and non-ASCII characters.
NLP Processing: Utilizes the TF-IDF vectorizer to transform text data into numerical features for classification.
Resume Classification: Employs a pre-trained machine learning model to predict the category of the uploaded resume.
Category Mapping: Maps the predicted category ID to meaningful job titles, such as "Java Developer," "Python Developer," "Data Science," etc.
Interactive Web Interface: Built with Streamlit, offering a user-friendly interface with animations and a blue color palette.
Technologies Used
Python Libraries:
Streamlit: For creating the web application and interactive user interface.
Scikit-learn: For machine learning models and TF-IDF vectorization.
NLTK: For text preprocessing, including tokenization and stopwords removal.
Pickle: For saving and loading machine learning models and vectorizers.
Regex: For text cleaning and preprocessing.
Usage
Navigate to the web app in your browser.
Upload a resume file (txt or pdf).
The app processes and cleans the resume, then predicts and displays the job category.
Customization
Models and Vectorizers: Update the clf.pkl and tfidf.pkl files with your own pre-trained models and vectorizers for different classification tasks.
CSS Styling: Customize the app.py file to adjust the color palette, animations, and layout to match your preferences.
Contributing
Feel free to open issues or submit pull requests to contribute to the development of this project. Please follow the project's code of conduct and contribution guidelines.
