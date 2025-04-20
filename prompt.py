def create_prompt(text: str) -> str:
    prompt = (
        "You are an expert Transcripter. Your task is to read the following text and provide a "
        "clear, and engaging summary that captures the main points: and its details\n\n"
        f"{text}\n\n"
        "Please provide the summary below:"
    )
    return prompt