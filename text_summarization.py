import requests
import json

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": "Bearer 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"}

# Function to send a query to the Hugging Face model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# List to store all input-output queries
all_queries = []

# Function to store input-output pairs
def store_input_output(input_query):
    # Get output from the model
    output = query({"inputs": input_query})

    if output:
        # Extract output text from the response
        generated_text = output[0].get("generated_text", "No output text found")

        # Store the input and output pair in the list
        all_queries.append({
            "input": input_query,
            "output": generated_text
        })
    else:
        print(f"Failed to get a valid response for input: {input_query}")

# Interactive loop for user input
while True:
    # Take input from the user
    input_query = input("Enter your query (or type 'exit' to stop): ")

    if input_query.lower() == "exit":
        break  # Exit the loop if the user types 'exit'

    # Store the input and output
    store_input_output(input_query)

    print("Query processed and stored.")

# Save all input-output pairs to a JSON file
output_file = "all_input_output.json"
with open(output_file, "w") as f:
    json.dump(all_queries, f, indent=4)

print(f"All input and output queries saved to {output_file}")
