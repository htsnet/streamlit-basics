import streamlit as st
from PIL import Image

st.set_page_config(page_title='Basic commands from Streamlit', page_icon=':smiley', layout='centered', )

def main():
    st.title("Streamlit Basics")

    st.header('Some basic commands from **Streamlit**')
    st.subheader('Just some commands...')

    st.subheader('Messages')

    st.info("Info")
    st.success("Success")
    st.warning("Warning")
    st.error("Error")

    st.subheader('Image')
    # Images
    from PIL import Image
    img = Image.open('logoStreamlit.png')
    st.image(img, width=400, caption="Logo Streamlit")

    st.subheader('Other widgets')
    st.checkbox('Checkbox')
    st.radio('Radiobutton', ['Option 1', 'Option 2', 'Option 3'])

    st.sidebar.write("A sidebar to show any information...")


if __name__ == '__main__':
	main() 