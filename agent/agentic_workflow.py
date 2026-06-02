
from utils.model_loader import ModelLoader
from prompt_lib.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START

from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_info import WeatherInfoTool
from tools.place_search import PlaceSearchTool
from tools.expense_calculator import CalculatorTool
from tools.currency_convertion import CurrencyConversionTool


class GraphBuilder():
    def __init__(self, model_provider: str = "Groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm =self.model_loader.load_llm()
        self.tools = []
        self.weather_tool = WeatherInfoTool()
        self.place_search_tool = PlaceSearchTool()
        self.calculator_tool = CalculatorTool()
        self.currency_conversion_tool = CurrencyConversionTool()
        self.tools.extend(self.weather_tool.weather_tool_list)
        self.tools.extend(self.place_search_tool.places_search_tool_list)
        self.tools.extend(self.calculator_tool.calculator_tooL_list)
        self.tools.extend(self.currency_conversion_tool.currency_convertor_tool)
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        self.graph = None
        self.system_prompt = SYSTEM_PROMPT


    def agent_function(self, state: MessagesState):
        """
        This function represents the agent's main logic. It will be called when the agent node is executed in the graph.
        """
        user_input = state["messages"]
        # Add system prompt to the user input
        input_question = [self.system_prompt] + user_input
        # Call the model with the input question
        response = self.llm_with_tools.invoke(input_question)
        # Return the response as a dictionary with the key "messages"
        return {"messages": response}

    def build_graph(self):
        # Build the graph with the necessary nodes and edges
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        self.graph = graph_builder.compile()
        return self.graph



    def __call__(self, *args, **kwds):
        return self.build_graph()
