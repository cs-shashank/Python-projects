from google import genai # Import the Gemini AI client library

def main():
    print("\n==============================")
    print("   Gemini AI Prompt Tool")
    print("==============================\n")

    try:
        # Create Gemini client
        client = genai.Client(api_key="YOUR_API_KEY")

        # Take user input
        prompt = input("Enter your prompt: ")

        print("\nGenerating response...\n")

        # Send request to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        # Print result
        print("AI Response:\n")
        print(response.text)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()