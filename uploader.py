import streamlit as st

from PIL import Image

# Title 
st.title("Vanperse Image Uploader and Display")


# Uploading a New File 
uploaded_file = st.file_uploader("Choose an Image ..", type="")

# Displaying the Image 
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption = 'Uploaded Image',use_column_width=True)

name = st. text_input("Enter a name for the image :")
st.write("This Image is called as {}".format(name))


