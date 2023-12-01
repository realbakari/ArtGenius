#@title ArtGenius
prompt = 'Full-body shot of the coolest car in the world' #@param {type:"string"}
openai_key = '' #@param {type:"string"}
steps = 5 #@param {type:"slider", min:1, max:10, step:1}

!pip install --upgrade openai > /dev/null

from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

# Initialize OpenAI client
client = OpenAI(api_key=openai_key)

def decide_style(prompt):
    """
    Decide whether the image style should be 'natural' or 'artistic'.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Given a prompt to generate an image, decide which type of image it should be: `natural` or `art`. `art` is more artistic, `natural` is more realistic."},
            {"role": "user", "content": f"Prompt: `{prompt}`"},
        ],
        logit_bias={'53980': 100, '472': 100},
        max_tokens=1,
        temperature=0,
    )

    style = 'vivid' if 'art' in response.choices[0].message.content else 'natural'
    print('Style Chosen:', style)
    return style

def generate_image(prompt, style):
    """
    Generate an image using DALL-E based on the provided prompt and style.
    """
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="hd",
        style=style,
        n=1,
    )

    image_url = response.data[0].url
    revised_prompt = response.data[0].revised_prompt
    return image_url, revised_prompt

def get_artistic_suggestion(image_url, prompt):
    """
    Get artistic suggestions for improving the generated image.
    """
    suggestion_request = [
        {"type": "text", "text": f"In two sentences or less, how can this image be improved to better fit this prompt: `{prompt.strip()}`?"},
        {"type": "image_url", "image_url": {"url": image_url}},
    ]

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[{"role": "user", "content": suggestion_request}],
        max_tokens=250,
    )

    suggestion = response.choices[0].message.content
    print('Suggestion:', suggestion)

    improved_prompt_request = [
        {"type": "text", "text": f"Here is the current prompt that was used to generate this image: `{prompt}`.\n\nHere is a suggestion for improvement: `{suggestion}`.\n\nWrite a new prompt that incorporates the suggestion to generate a better image. Make it clear, and three sentences or less. Don't mention that there have been other prompts, just describe what you want the new image to look like."},
        {"type": "image_url", "image_url": {"url": image_url}},
    ]

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[{"role": "user", "content": improved_prompt_request}],
        max_tokens=250,
    )

    improved_prompt = response.choices[0].message.content
    print('Improved Prompt:', improved_prompt)
    return improved_prompt

def gpt_artist(prompt, steps):
    """
    Main function for ArtGenius that orchestrates the image generation and improvement process.
    """
    style = decide_style(prompt)

    for _ in range(steps):
        try:
            # Generate an image
            image_url, prompt = generate_image(prompt, style)

            # Display the image
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            display(img)

            # Get artistic suggestion
            prompt = get_artistic_suggestion(image_url, prompt)
        except Exception as e:
            print(f"An error occurred: {str(e)}. Retrying...")

    return prompt

# Test the 'gpt-artist'
final_prompt = gpt_artist(prompt, steps)
print("Final prompt:", final_prompt)
