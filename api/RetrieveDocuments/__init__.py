import json
from models.sentence_transformers_model import generate_embedding
from models.search_service import search_documents
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Extract query from the request
        body = req.get_json()
        query = body.get("query")

        # Generate embeddings for the query
        query_embedding = generate_embedding(query)

        # Search for relevant documents based on the embedding
        results = search_documents(query_embedding)

        # Return results as JSON
        return func.HttpResponse(
            json.dumps({"documents": results}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500
        )
