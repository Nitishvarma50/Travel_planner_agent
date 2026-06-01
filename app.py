from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
import os


app = FastAPI()


class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_travel_planner(query: QueryRequest):
    try:
        print("Received query:", query)
        graph = GraphBuilder(model_name="groq")
        react_app = graph()
        
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("graph.png", "wb") as f:
            f.write(png_graph)

        print("Graph generated and saved as graph.png")
        messages ={"messages": {query.Question}}

        output = react_app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})