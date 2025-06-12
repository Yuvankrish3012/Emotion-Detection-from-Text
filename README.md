# Emotion-Detection-from-Text

This project detects human emotions like **joy**, **sadness**, **anger**, and more — using NLP and machine learning techniques. The app provides a user-friendly **Streamlit interface** to analyze emotions from sentences.

---

## 📁 Dataset

- Dataset: [Emotion Dataset for NLP](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp)
- Format: `.txt` files (`train.txt`, `test.txt`, `val.txt`)
- Labels: `joy`, `sadness`, `anger`, `fear`, `surprise`, `love`

---

## ⚙️ Project Pipeline

1. **Data Preprocessing**
   - Lowercasing, punctuation removal
   - Custom `clean_text()` function

2. **TF-IDF Vectorization**
   - Max features: 5000

3. **Label Encoding**
   - With `LabelEncoder` from `sklearn`

4. **Model Training**
   - Classifier: `Logistic Regression`

5. **Evaluation Metrics**
   - Accuracy, Precision, Recall, F1-Score
   - Confusion Matrix

---

## ✅ Model Evaluation

Accuracy : 0.87
Precision: 0.87
Recall : 0.87
F1 Score : 0.86

yaml
Copy
Edit

### 📋 Classification Report

| Emotion   | Precision | Recall | F1-Score | Support |
|-----------|-----------|--------|----------|---------|
| anger     | 0.90      | 0.82   | 0.86     | 275     |
| fear      | 0.89      | 0.79   | 0.84     | 224     |
| joy       | 0.84      | 0.96   | 0.89     | 695     |
| love      | 0.82      | 0.59   | 0.69     | 159     |
| sadness   | 0.90      | 0.93   | 0.91     | 581     |
| surprise  | 0.85      | 0.52   | 0.64     | 66      |

---

## 📊 Visualizations

### 🔷 Confusion Matrix

![image](https://github.com/user-attachments/assets/da8e1ffa-955f-4aed-b939-e9e13a9314e5)


---

## 🌐 Streamlit UI

![Screenshot 2025-06-12 150136](https://github.com/user-attachments/assets/93be50e3-20a1-4cdb-97d2-264f98b80c83)

![Screenshot 2025-06-12 150216](https://github.com/user-attachments/assets/2d17d205-0d71-4ced-b1b1-6663236235c7)

Simple and interactive web app to enter your text and instantly get the predicted emotion.

---

## 🚀 How to Run Locally

### ✅ Prerequisites

- Python 3.8+
- `streamlit`, `scikit-learn`, `pandas`, `matplotlib`, `seaborn`

### 🛠️ Run the App

```bash
# Step 1: Activate environment
conda activate myenv

# Step 2: Navigate to folder
cd "D:\ML PROJECTS\Emotion Detection from Text"

# Step 3: Launch app
streamlit run emotion_app.py
🗂️ Project Structure
vbnet
Copy
Edit
Emotion Detection from Text/
├── train.txt
├── test.txt
├── val.txt
├── emotion_model.pkl
├── emotion_vectorizer.pkl
├── emotion_label_encoder.pkl
├── emotion_app.py
├── confusion_matrix_emotion.png
└── README.md
💡 Future Improvements
Use BERT or LSTM for deeper context understanding

Add word clouds for each emotion

Enable batch input or CSV uploads

Deploy online with Streamlit Cloud

🧑‍💻 Author
Yuvan Krishnan
GitHub: Yuvankrish3012
