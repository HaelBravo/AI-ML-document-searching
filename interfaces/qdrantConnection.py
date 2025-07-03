from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

def connect_qdrant():
    """
    Connects to Qdrant and returns the client instance.
    Adjust host/port as needed depending on your setup.
    """
    # If Qdrant is in a container and you're connecting from another container (Docker Compose)
    client = QdrantClient(host="localhost", port=6333)

    # If Qdrant is in a container, but you're connecting from your host machine
    # client = QdrantClient(host="localhost", port=6333)

    return client

def create_collection(client, collection_name, vector_size=128):
    """
    Create or recreate a collection in Qdrant.
    """
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )
    print(f"Collection '{collection_name}' is ready.")

def insert_point(client, collection_name, point_id, vector, payload):
    """
    Insert or update a point into the specified collection.
    """
    client.upsert(
        collection_name=collection_name,
        points=[
            {
                "id": point_id,
                "vector": vector,
                "payload": payload
            }
        ]
    )
    print(f"Inserted point {point_id} into '{collection_name}'.")

if __name__ == "__main__":
    # Connect to Qdrant
    client = connect_qdrant()

    # Create or ensure collection exists
    create_collection(client, "my_collection", vector_size=128)

    # Example point
    vector = [0.1] * 128  # Example dummy vector
    payload = {"label": "example"}
    insert_point(client, "my_collection", point_id=1, vector=vector, payload=payload)
