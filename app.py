import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "your-api-key"

def generate_marketing_content(product_name, category):
    """
    Function to generate marketing content using GPT-3.
    Args:
        product_name (str): Name of the product
        category (str): Category of the product
    Returns:
        str: Generated marketing content
    """
    prompt = f"Generate a creative and engaging marketing slogan and description for a product named '{product_name}' in the '{category}' category."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Generative AI for Marketing")
st.markdown("### Enter product details to generate marketing content")

product_name = st.text_input("Product Name")
category = st.text_input("Category")

if st.button("Generate"):
    if product_name and category:
        content = generate_marketing_content(product_name, category)
        st.subheader("Generated Marketing Content")
        st.write(content)
    else:
        st.warning("Please enter both product name and category.")
