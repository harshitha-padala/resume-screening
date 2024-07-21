import streamlit as st
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf.pkl', 'rb'))

def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

# Web app
def main():
    st.set_page_config(page_title="Resume Screening App", layout="wide")
    
    # Custom CSS with blue palette and animations
    st.markdown("""
        <style>
        body {
            background-color: #f0f4f8;
            color: #333;
            text-align: center;
        }
        .title {
            color: #0056b3; /* Dark Blue */
            animation: fadeIn 2s ease-in;
            margin-top: 20px;
        }
        .upload-container {
            margin-top: 20px;
        }
        .category {
            font-weight: bold;
            color: #003d79; /* Medium Blue */
            animation: slideIn 1s ease-in-out;
            margin: 20px 0;
        }
        .prediction {
            color: #004a99; /* Light Blue */
            font-size: 18px;
            margin-bottom: 20px;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideIn {
            from { transform: translateX(-100%); }
            to { transform: translateX(0); }
        }
        .animated-button {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px 0;
            font-size: 16px;
            color: #fff;
            background-color: #007bff; /* Primary Blue */
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .animated-button:hover {
            background-color: #0056b3; /* Darker Blue */
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Resume Screening App", anchor="top")
    
    uploaded_file = st.file_uploader('Upload Resume', type=['txt', 'pdf'], label_visibility="collapsed")

    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, try decoding with 'latin-1'
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = clean_resume(resume_text)
        input_features = tfidfd.transform([cleaned_resume])
        prediction_id = clf.predict(input_features)[0]

        # Map category ID to category name
        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

        category_name = category_mapping.get(prediction_id, "Unknown")

        st.markdown(f"""
            <div class="upload-container">
                <h2 class="title">Resume Uploaded Successfully</h2>
                <p class="prediction">Predicted Category:</p>
                <p class="category">{category_name}</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


