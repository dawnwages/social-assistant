from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Azure Cognitive Search setup
search_client = SearchClient(
    endpoint="https://<search service>.search.windows.net/",
    index_name="<index name>",
    credential=AzureKeyCredential("<search API key>")
)

def search_documents(query_embedding):
    # Perform search using the generated embeddings
    search_results = search_client.search(
        search_text="*",  # Empty query since we are using embeddings
        vectors=[
            {"value": query_embedding, "fields": "embedding_field", "k": 5}
        ]
    )

    documents = []
    for result in search_results:
        documents.append(result["document_field"])  # Customize based on your schema
    return documents
