from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

def create_model(api_key, model_name="gpt-4o"):
    """
    Try to create a ChatOpenAI model with a given model_name.
    """
    return ChatOpenAI(
        temperature=0,
        api_key=api_key,
        model=model_name
    )

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY not found. Add it to your .env file.")
        return

    # Try GPT-4o first
    try:
        model = create_model(api_key, "gpt-4o")
        print("✅ Using GPT-4o")
    except Exception as e:
        print("⚠️ Could not init GPT-4o. Fallback to GPT-3.5-Turbo...")
        model = create_model(api_key, "gpt-3.5-turbo")

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome!")
    print("Ask me anything (type 'quit' to exit):")

    while True:
        user_input = input("\nYou : ").strip()

        if user_input.lower() == "quit":
            break

        print("\nAssistant : ", end="")

        try:
            for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}
            ):
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="")
            print()

        except openai.RateLimitError:
            # Automatic fallback when quota/rate limit reached
            print("\n⚠️ Rate limit/quota exceeded on GPT-4. Switching to GPT-3.5-Turbo...")
            model = create_model(api_key, "gpt-3.5-turbo")
            agent_executor = create_react_agent(model, tools)

        except Exception as e:
            print(f"\n❌ Error: {e}")
            break

if __name__ == "__main__":
    main()
