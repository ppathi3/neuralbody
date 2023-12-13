import streamlit as st

def home_page():
    st.title("Neural Body: Implicit Neural Representations with Structured Latent Codes")
    st.header("Introduction to Neural Body")
    intro_text = """
    Our application addresses a critical challenge in synthesizing novel views of human performers from sparse camera views. 
    While recent approaches excel with dense input views, sparse views pose an ill-posed problem for neural representation learning.

    To overcome this challenge, our innovation lies in integrating observations across video frames. We introduce NeuralBody, 
    a novel representation for the human body. It assumes that learned neural representations across frames share a set of latent codes 
    tied to a deformable mesh, allowing natural integration of observations.

    This deformable mesh not only guides geometric understanding but also enables more efficient learning of 3D representations. 
    Our approach has been evaluated on the ZJU-MoCap dataset, capturing performers with complex motions. Results demonstrate substantial 
    improvements in novel view synthesis quality compared to prior works.

    Additionally, our approach showcases its capability to reconstruct a moving person from monocular video data on the People-Snapshot dataset.

    Explore our app to delve deeper into NeuralBody's innovative techniques and its exceptional performance in view synthesis!
    """

    st.write(intro_text)
def results_page():
    st.title("Results Page")
    st.header("Input and Output")

    # Input video selection
    input_video = "data/people_snapshot/female-3-casual/female-3-casual.mp4"
    st.video(input_video)

    if st.button("Process"):

        # Process input_video and generate output_image

        # Placeholder for output paths (replace with actual paths)
        output_image_path = "data/render/female3c/frame_0000/0000.png"

        # Display output image
        st.image(output_image_path, caption="Output Image", use_column_width=True)

def main():
    st.sidebar.title("Navigation")
    selected_tab = st.sidebar.radio("Go to", ("Home Page", "Results Page"))

    if selected_tab == "Home Page":
        home_page()
    elif selected_tab == "Results Page":
        results_page()

if __name__ == "__main__":
    main()

