# 🌍 AI Travel Planner

AI Travel Planner is an agentic trip planning system built with **LangGraph**, **FastAPI**, and **Streamlit**. It coordinates multiple specialized tools (Weather, Place Search, Expense Calculator, and Currency Conversion) using a ReAct-based agentic workflow to create tailored, context-aware travel plans.

---

## 📖 About the Project

Traditional travel planning involves juggling multiple websites: checking weather patterns, searching for local attractions, converting currency rates, and calculating estimated expenses across spreadsheets. 

**AI Travel Planner** solves this fragmentation by consolidating the planning process into an intelligent, conversational interface. Using an **agentic workflow powered by LangGraph**, the system acts as a digital travel concierge. When a user asks a question, the agent doesn't just generate text; it actively reasons, decides which information is missing, calls specialized real-world tools, and aggregates the results into a cohesive itinerary.

### How It Helps Users

- **All-in-One Trip Planning**: Eliminates the need to switch between weather sites, map searches, currency converter widgets, and spreadsheets.
- **Accurate Real-Time Context**: Incorporates real-time weather details and location searches so itineraries correspond with actual conditions and available destinations.
- **Automated Expense & Currency Math**: Calculates your budget and automatically converts costs to your preferred currency, removing manual financial calculations from planning.
- **Interactive Itinerary Customization**: Users can refine their trip details on the fly (e.g. asking the agent to "change to a budget-friendly option" or "find family-friendly dinner options nearby") with instant backend updates.

---

## 🏗️ Project Architecture

```
AI_Trip_Planner/
├── agent/                   # Agent workflow configuration (LangGraph StateGraph)
│   ├── __init__.py
│   └── agentic_workflow.py
├── exception/               # Custom exception handling
│   ├── __init__.py
│   └── exception_handler.py
├── logger/                  # Custom logging subsystem
│   ├── __init__.py
│   └── logging.py
├── prompt_lib/              # System prompt definitions
│   ├── __init__.py
│   └── prompt.py
├── tools/                   # Agent tool suite (Weather, Place Search, Calculator, etc.)
│   ├── __init__.py
│   ├── currency_convertion.py
│   ├── expense_calculator.py
│   ├── place_search.py
│   └── weather_info.py
├── utils/                   # Helper utilities
│   ├── __init__.py
│   └── model_loader.py
├── main.py                  # FastAPI Backend API Server
├── streamlit_app.py         # Streamlit Frontend Client
├── setup.py                 # Setuptools installer
├── requirements.txt         # Package dependencies
└── .env                     # Environment variables
```

---

## ✨ Features

- **Agentic Workflow**: Utilizes `LangGraph`'s state management, allowing the LLM to make sequential, conditional tool invocations before delivering a complete plan.
- **Rich Tool Set**:
  - **Weather Search**: Retrieves destination temperature and conditions.
  - **Places Search**: Finds restaurants, attractions, and accommodations.
  - **Expense Calculator**: Calculates and totals travel costs.
  - **Currency Conversion**: Conversions between international rates.
- **Dual-Channel Logging**: Log outputs are written simultaneously to the terminal console and to timestamped log files in a `/logs` folder.
- **Detailed Exception Tracebacks**: Custom exception system (`CustomException`) automatically captures file names, error lines, and exact traceback messages to streamline debugging.
- **FastAPI API Layer**: Decoupled, asynchronous REST API serving backend queries at `/query`.
- **Streamlit Interactive UI**: High-fidelity, user-friendly frontend client for chat and presentation.

---

## 🛠️ Prerequisites & Setup

Ensure you have Python 3.9+ installed.

### 1. Set Up Environment Variables
Create a `.env` file in the root directory and populate it with your API keys:

```bash
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_key
GPLACES_API_KEY=your_google_places_key
FOURSQUARE_API_KEY=your_foursquare_key
TAVILY_API_KEY=your_tavily_key
OPENWEATHERMAP_API_KEY=your_openweathermap_key
EXCHANGE_RATE_API_KEY=your_exchangerate_key
LANGCHAIN_API_KEY=your_langchain_key
```

### 2. Install Dependencies
Set up a Python virtual environment and install the required libraries:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install package dependencies
pip install -r requirements.txt
pip install -e .
```

---

## 🚀 How to Run

### Step 1: Start the Backend (FastAPI)
Run the backend server using `uvicorn`:

```bash
uvicorn main:app --reload
```
The backend server will run on `http://127.0.0.1:8000`.

### Step 2: Start the Frontend (Streamlit)
Run the Streamlit app to launch the chat UI:

```bash
streamlit run streamlit_app.py
```
The frontend application will open automatically in your browser at `http://localhost:8501`.

---

## 🔬 Exception Handling & Logging Usage

To integrate the custom logging and exception handling into new components:

```python
from logger import logger
from exception import CustomException
import sys

def my_function():
    logger.info("Initializing operation...")
    try:
        # Perform operation
        result = 10 / 0
    except Exception as e:
        logger.error("An error occurred during operation.")
        raise CustomException(e, sys)
```
This configuration records the traceback details, locating the exact line and file where the exception occurred.
