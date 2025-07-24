import streamlit as st
import boto3
import os

# AWS S3 Setup
BUCKET_NAME = "ppe-detection-input"
UPLOAD_PREFIX = "uploads/"

# Streamlit Page Config
st.set_page_config(page_title="AI-powered PPE Detection", page_icon="🦺", layout="centered")

st.title("🦺 AI-powered PPE Detection")
st.markdown("Upload a photo to detect PPE using AWS Rekognition.")

# Upload Section
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Upload to S3"):
        # Save file temporarily
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Upload to S3 using boto3
        s3 = boto3.client("s3")
        s3.upload_file(
            Filename=uploaded_file.name,
            Bucket=BUCKET_NAME,
            Key=UPLOAD_PREFIX + uploaded_file.name
        )

        st.success(f"✅ Uploaded to S3 bucket ⁠ {BUCKET_NAME} ⁠ successfully!")

        # Remove temp file
        os.remove(uploaded_file.name)