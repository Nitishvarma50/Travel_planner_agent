
from utils.model_loader import ModelLoader
from prompt_lib.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessageState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_info import WeatherInfoTool
from tools.place_search import PlaceSearchTool
from tools.calculator import CalculatorTool
from tools.currency_convertion import CurrencyConversionTool


class GraphBuilder():
    def __init__(self):
        pass

    def agent_function(self, state: MessageState):
        """
        This function represents the agent's main logic. It will be called when the agent node is executed in the graph.
        """
        user_input = state["messages"]
        # Add system prompt to the user input
        input_question = [self.system_prompt] + user_input
        # Call the model with the input question
        response = self.llm_with_tools(input_question)
        # Return the response as a dictionary with the key "messages"
        return {"messages": response}

    def build_graph(self):
        # Build the graph with the necessary nodes and edges
        graph_builder = StateGraph(MessageState)
        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edge("agent", tools_condition)
        
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        self.graph = graph_builder.compile()
        return self.graph



    def __call__(self, *args, **kwds):
        pass