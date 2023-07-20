import pdfkit
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
import os
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(layout="centered", page_icon="", page_title="PDF Report Generator for News HW01")
st.title("PDF Report Generator for News HW01")

# Load HTML template
env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# template = env.from_string("""  #here the template is directly in the main .py file which is not ideal
# <html>
#
# <head>
# <title>Title</title>
# </head>
#
# <body>
# <span style="font-size:30px"><b>{{ student }}</b></span><br/><br/>
# <span style="font-size:25px"><i>has completed the course</i></span> <br/><br/>
# <span style="font-size:30px">{{ course }}</span> <br/><br/>
# <span style="font-size:20px">with a score of <b>{{ grade }}</b></span> <br/><br/><br/><br/>
# <span style="font-size:25px"><i>dated</i></span><br>
# {{ date }} <br> <br>
# <img src="data:image/png;base64,{{ image_base64 }}" />
# </body>
# </html>
# """)
template = env.get_template("template.html")  # here the template is in a separate .html file
#left, right = st.columns(2)

# st.write("Here's the template we'll be using:")
# st.image("template.png", width=300)

st.write("Answer the following questions based on the assignment post on Blackboard:")
form = st.form("template_form")
#student_name = form.text_input("Full NAME", "John Doe")
student_name = form.text_input("Full NAME")
# course = form.selectbox(
#     "Choose course",
#     ["Report Generation in Streamlit", "Advanced Cryptography"],
#     index=0,
# )
#grade = form.slider("Grade", 0, 100, 97)
#st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
q01= form.text_area(label="questions 1 answered here:", height=200, max_chars=500)

form.write("Question 2 answered here:")
uploaded_file1 = form.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="q2")
if uploaded_file1 is not None:
    # Read the image
    image1 = Image.open(uploaded_file1)
    # Convert image to base64 string
    buffered1 = BytesIO()
    image1.save(buffered1, format="PNG")
    image_base64a= base64.b64encode(buffered1.getvalue()).decode("utf-8")

form.write("Question 3 answered here:")
uploaded_file2 = form.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="q3")
if uploaded_file2 is not None:
    # Read the image
    image2 = Image.open(uploaded_file2)
    # Convert image to base64 string
    buffered2 = BytesIO()
    image2.save(buffered2, format="PNG")
    image_base64b= base64.b64encode(buffered2.getvalue()).decode("utf-8")

submit = form.form_submit_button("Generate PDF")

if submit:
    # Render the HTML template
    html = template.render(
        student_name=student_name,
        #course=course,
        #grade=f"{grade}/100",
        #date=date.today().strftime("%B %d, %Y"),
        q01=q01,
        image_base64a=image_base64a,
        image_base64b=image_base64b ,
    )
    # pdf = pdfkit.from_string(html, False)
    #pdf = pdfkit.from_string(html, "out.pdf", configuration=config)
    pdf = pdfkit.from_string(html,  configuration=config)
    st.balloons()

    # right.success("Your template successfully generated!")
    st.success("Your template successfully generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    # right.download_button(

    # Generate HTML file
    # with open("diploma.html", "w") as f:
    #     f.write(html)

    st.success("🎉 Your PDF file generated! you can  download it by clicking the below button to save it and submit it in gradescope assignment!")
    st.download_button(
        #"⬇️ Download HTML",
        "⬇️ Download pdf",
        #data=html,
        data=pdf,
        #file_name="diploma.html",
        file_name="AssignX.pdf",
        #mime="text/html",
        mime="application/octet-stream",
    )

#This file uses the virt env at
# conda deactivate
# ..\venv4pdfgen\Scripts\activate.ps1
# streamlit run ./nhw01.py
