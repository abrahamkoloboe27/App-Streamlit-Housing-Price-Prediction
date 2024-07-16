import streamlit as st
import requests

# Set the page configuration
st.set_page_config(
        page_title="House Price Prediction",
        page_icon=":house_with_garden:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Add a title with an emoji
st.title(":house_with_garden: House Price Prediction")
if st.sidebar.toggle("About the author"):
        with st.expander("Author", True) : 
            c1, c2 = st.columns([1,2])
            with c1 :
                st.image("img/About the author.png")
            with c2 : 
                st.header(""" **S. Abraham Z. KOLOBOE**""")
                st.markdown("""
                    
                    *:blue[Data Scientist | Ingénieur en Mathématiques et Modélisation]*

                    Bonjour,

                    Je suis Abraham KOLOBOE, un Data Scientist et Ingénieur en Mathématiques et Modélisation. 
                    Mon expertise se situe dans les domaines des sciences de données et de l'intelligence artificielle. 
                    Avec une approche technique et concise, je m'engage à fournir des solutions efficaces et précises dans mes projets.
                            
                    * Email : <abklb27@gmail.com>
                    * WhatsApp : +229 91 83 84 21
                    * Linkedin : [Abraham KOLOBOE](https://www.linkedin.com/in/abraham-zacharie-koloboe-data-science-ia-generative-llms-machine-learning)
                        
                                        """)
# Define the API endpoint
API_ENDPOINT = st.text_input("API Endpoint", value="http://0.0.0.0:8000/predict")

# Define the Streamlit app
def main():
    # Create a sidebar toggle
    with st.sidebar:
        if st.toggle("Show Project Description", True):
            st.markdown("This project is a house price prediction application that uses a machine learning model to predict the price of a house based on various features such as area, number of bedrooms, bathrooms, etc.")

        if st.toggle("Show App Description",True):
            st.markdown("This app allows users to input the details of a house and get a predicted price based on the machine learning model. Users can also modify the API endpoint to use a different model if desired.")

    # Create a form
    with st.form(key="house_form"):
        # Create two columns
        col1, col2 = st.columns(2)

        # Create input fields in the first column
        with col1:
            area = st.number_input("Area", value=2640)
            bedrooms = st.number_input("Bedrooms", value=2)
            bathrooms = st.number_input("Bathrooms", value=1)
            stories = st.number_input("Stories", value=1)
            mainroad = st.selectbox("Main Road", ["yes", "no"])
            guestroom = st.selectbox("Guest Room", ["yes", "no"])
            basement = st.selectbox("Basement", ["yes", "no"])

        # Create input fields in the second column
        with col2:
            hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
            airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
            parking = st.number_input("Parking", value=1)
            prefarea = st.selectbox("Preferred Area", ["yes", "no"])
            furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "unfurnished", "semi-furnished"])

        # Create a dictionary with the input data
        data = {
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "mainroad": mainroad,
            "guestroom": guestroom,
            "basement": basement,
            "hotwaterheating": hotwaterheating,
            "airconditioning": airconditioning,
            "parking": parking,
            "prefarea": prefarea,
            "furnishingstatus": furnishingstatus,
        }

        # Create a submit button
        submit_button = st.form_submit_button(label="Predict")

    # Send a POST request to the API and display the predicted price
    if submit_button:
        response = requests.post(API_ENDPOINT, json=data)
        prediction = response.json()["prediction"]
        st.metric(label="Predicted Price", value=f"{prediction:.3f}")

if __name__ == "__main__":
    main()
