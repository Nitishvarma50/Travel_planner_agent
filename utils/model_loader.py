import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional
from utils.config_loader import load_config
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq


class Config_Loader():
    def __init__(self):
        print(f"Loading configuration ")
        load_dotenv()
        self.config =load_config()

    def __getitem__(self, key):
        return self.config[key]
    

class ModelLoader(BaseModel):
    model_provider: Literal["openai", "Groq", "groq"] = "openai"
    config: Optional[Config_Loader] = Field(default=None, exclude=True)

    def model_post_init(self, __context):
        # Load the model based on the provider and configuration
        if self.model_provider == "groq":
            self.model_provider = "Groq"
        self.config = Config_Loader()

    class Config():
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load the language model based on the provider and configuration
        """
        print("LLM Loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "openai":
            # Load OpenAI model using the configuration
            print("Loading OpenAI model...")
            OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model=model_name, temperature=0.7, openai_api_key=OPENAI_API_KEY)
        elif self.model_provider == "Groq":
            # Load Groq model using the configuration
            print("Loading Groq model...")
            # Implement the logic to load the Groq model here
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["Groq"]["model_name"]
            llm = ChatGroq(model=model_name, temperature=0.7, groq_api_key=groq_api_key)

        return llm
