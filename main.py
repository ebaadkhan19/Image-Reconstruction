import streamlit as st

from PIL import Image
import numpy as np

import tensorflow as tf


def create_model():
    model = tf.saved_model.load("model/mnist_reconstructor")
    return model


model = create_model()


def predict(image):
    f = model.signatures["serving_default"]
    resized_image = image.resize((28, 28))
    grayscale_image = resized_image.convert("L")
    normalized_image = (np.asarray(grayscale_image) / 255.0).reshape((1, 28, 28))
    tensor = tf.convert_to_tensor(normalized_image, dtype=tf.float32)
    predictions = (f(tensor)["output_1"].numpy() * 255).reshape((28, 28))
    reconstructed_image = Image.fromarray(predictions)
    reconstructed_image = reconstructed_image.convert("RGB")
    return reconstructed_image


def main():
    st.title("Image Reconstructor")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=False)

        if st.button("Test"):
            reconstructed = predict(image)
            st.image(reconstructed, caption="Reconstructed", use_column_width=False)


if __name__ == "__main__":
    main()
