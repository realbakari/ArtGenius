# ArtGenius

ArtGenius is an open-source project that combines the creative power of GPT-4 and DALL-E to generate stunning and unique artistic images based on user prompts. Whether you're looking for natural and realistic scenes or vibrant and abstract compositions, ArtGenius has you covered.

## Overview

ArtGenius uses a two-step process:

1. **Style Selection with GPT-4:** The system analyzes your prompt to determine the desired style - 'natural' for realistic images or 'vivid' for more artistic and abstract creations.

2. **Image Generation with DALL-E:** Once the style is chosen, ArtGenius employs DALL-E, a powerful image generation model, to bring your prompt to life in the form of a high-quality, visually appealing image.

## Getting Started

Follow these steps to get ArtGenius up and running on your machine:

### Prerequisites

- Python 3.x
- [OpenAI API key](https://beta.openai.com/account/api-keys)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/realbakari/ArtGenius.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ArtGenius
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API key:

    Replace `YOUR_OPENAI_API_KEY` in the code with your actual API key.

### Usage

1. Run the ArtGenius script:

    ```bash
    python art_genius.py
    ```

2. Follow the on-screen prompts to provide your creative input and witness the magic of ArtGenius in action!

## Features

- Dynamic image style selection using GPT-4.
- High-quality image generation with DALL-E.
- Artistic suggestions for image improvement using GPT-4 Vision API.
