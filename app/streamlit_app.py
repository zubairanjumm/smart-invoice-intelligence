import json

import streamlit as st

from app.main import process_invoice


st.set_page_config(
    page_title="Smart Invoice Intelligence",
    page_icon="📄",
    layout="centered",
)


st.title("Smart Invoice Intelligence")
st.write("Upload an invoice and extract structured data using AI.")


uploaded_file = st.file_uploader(
    "Upload an invoice",
    type=["pdf", "png", "jpg", "jpeg"],
)


if uploaded_file is not None:
    st.write(f"**File:** {uploaded_file.name}")

    if st.button("Extract Invoice"):
        try:
            with st.spinner("Processing invoice..."):
                file_path = f"temp_{uploaded_file.name}"

                with open(file_path, "wb") as file:
                    file.write(uploaded_file.getbuffer())

                invoice = process_invoice(file_path)

            st.success("Invoice processed successfully.")

            st.subheader("Invoice Data")

            st.json(
                json.loads(
                    invoice.model_dump_json()
                )
            )

        except Exception as error:
            st.error(f"Error: {error}")