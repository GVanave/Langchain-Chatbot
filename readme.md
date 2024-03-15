# 🔗🔗 🤖 Langchain Project 🔗🔗🤖

## Introduction

This project showcases two different Python scripts for developing chatbots using Langchain and Streamlit. The first script implements a simple CSV chatbot using Langchain and Streamlit, while the second script utilizes the Llama pretrained model  for chatting, without integrating with Streamlit.

## Download pretrained llama model 

```bash
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main/llama-2-7b-chat.ggmlv3.q4_0.bin
```
You can download it locally first add as path.
## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.9
- Pip 

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/GVanave/langchain-chatbot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd langchain-chatbot
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Streamlit Web Application

This project includes a Streamlit web application with two pages: one for the chatbot and another for data statistics.

To run the Streamlit web application, execute the following command:

```bash
streamlit run csv_chatbot.py 
```

## File Descriptions

- `csv_chatbot.py`: Python script implementing a simple CSV chatbot using Langchain and Streamlit.
- `llama_chatbot.ipynb`: Python script demonstrating the usage of the Llama pretrained model for chatting.
- `requirements.txt`: List of Python packages required for the project.

## Future Work

In future iterations of this project, the following enhancements are planned:

- **PDF Chatbot**: Implementing a chatbot capable of processing PDF documents for more versatile interactions.
- **Fine-tuning LLMs**: Fine-tuning Large Language Models (LLMs) like GPT-3 or BERT for specific tasks to improve conversational abilities and accuracy.

💡 Stay tuned for updates as we continue to improve and expand the capabilities of LLMs! 🚀


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.


