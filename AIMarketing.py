import openai
import pandas as pd

# Load the sample dataset
data = pd.read_csv("products.csv")

# Set up OpenAI API key (replace 'your-api-key' with actual key)
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
    
    # Call the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    # Extract and return the generated text
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    for _, row in data.iterrows():
        product_name = row["Product Name"]
        category = row["Category"]
        content = generate_marketing_content(product_name, category)
        print(f"Product: {product_name}\nCategory: {category}\nMarketing Content: {content}\n")
