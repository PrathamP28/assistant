import ollama

# 1. Define your prompts and model
system_prompt = "You are a helpful assistant that speaks like a pirate."
user_prompt = "Explain why the ocean is salty."
model_name = "llama3" # Ensure you have run 'ollama pull llama3' in your terminal

try:
    # 2. Call the Ollama API using the 'chat' method
    # This allows you to clearly separate instructions from user input
    response = ollama.chat(
        model=model_name,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ]
    )

    # 3. Print the final response
    print(response['message']['content'])

except Exception as e:
    print(f"An error occurred: {e}")
    print("Verification checklist:")
    print("- Is the Ollama app running?")
    print(f"- Have you downloaded the model using 'ollama pull {model_name}'?")

