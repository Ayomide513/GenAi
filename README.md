GenAi
A Streamlit-based generative AI testing application.  
This is a proof-of-concept setup to experiment with AI / LLM-based prompts in a web app.  

Table of Contents

  [Features](#features)  
  [Tech Stack](#tech-stack)  
  [Getting Started](#getting-started)  
  [Prerequisites](#prerequisites)  
  [Installation](#installation)  
  [Running](#running)  
  [Usage](#usage)  
  [Project Structure](#project-structure)  
  [Contributing](#contributing)   

 Features
 Web interface (via Streamlit) to enter prompts and get AI-generated responses  
 Utilities and helper modules to manage prompt logic  
 Easy to extend / swap in different models or APIs  

 Tech Stack
 Python  
 Streamlit  
 Custom modules (`prompt.py`, `utils.py`, `support_app.py`)  
 Configuration file (`config.py`)  

Getting Started

Prerequisites
Python 3.7+  
`pip`  
Internet access (for calling remote AI APIs)  
Virtual environment tool (venv, conda, etc.)

**Installation**

Clone this repository  
   ```bash
   git clone https://github.com/Ayomide513/GenAi.git
   cd GenAi

**Create and activate a virtual environment**
python3 -m venv venv
source venv/bin/activate   # on Linux / macOS
# on Windows: venv\Scripts\activate

**Install the dependencies**
pip install -r requirement.txt

**To launch the Streamlit interface:**
streamlit run support_app.py


**Contributing**
Contributions, suggestions, and pull requests are welcome! Here are a few guidelines:
Fork the repository
Create a feature branch (git checkout -b feature/YourFeature)
Make your changes, commit with clear messages
Open a pull request, explaining the change
