import streamlit as st
import cv2
from PIL import Image
import os

# Title and description
st.title("Neural Body: Implicit Neural Representations with Structured Latent Codes")
st.header("Novel View Synthesis of Dynamic Humans")

# Input image path
input_image_path = "drive/MyDrive/neuralbody/data/zju_mocap/CoreView_313/Camera (3)/CoreView_313_Camera_(3)_0544_2019-08-23_16-09-08.234.jpg"


# Output image and video paths
output_image_path = "drive/MyDrive/neuralbody/data/zju_mocap/CoreView_313/Camera (3)/CoreView_313_Camera_(3)_0544_2019-08-23_16-09-08.234.jpg"
output_video_path = "output.mp4"

# Display input image
st.subheader("Input Image")
st.image(input_image_path, caption="Input Image", use_column_width=True)

if st.button("Process Image"):
  st.write("3D Reconstructed Image")
  st.image(output_image_path, caption="Output Image", use_column_width=True)
  st.write("3D Reconstructed Video")
  st.video(output_video_path)
