
# Stroke Prediction Web App

This is a machine learning-powered web application built using **Streamlit** to predict the likelihood of a stroke based on various health factors. The app takes user inputs such as age, blood pressure, cholesterol levels, smoking status, and more, and provides a prediction on the likelihood of having a stroke. The goal is to help individuals assess their stroke risk and take preventative actions accordingly.

## Features:
- **Real-time Stroke Prediction**: Users input their health information, and the model predicts the likelihood of a stroke occurring.
- **Simple User Interface**: Built with Streamlit, the app features an easy-to-use interface for both technical and non-technical users.
- **Interactive Model**: Explore how changes in input parameters affect the stroke prediction.

## Technologies:
- **Web Framework**: Streamlit
- **Machine Learning**: Scikit-learn
- **ML model**: AdaBoost Classifier

## Getting Started:
1. Clone this repository.
2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app locally:  
   ```bash
   streamlit run app.py
   ```
4. The app will be available at `http://localhost:8501`.

## Dataset:
The model is trained on the publicly available [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset), which contains various health metrics to predict the risk of stroke.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
