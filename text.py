import boto3
import os
from dotenv import load_dotenv
load_dotenv()

access_key = os.getenv("access_key")    
secret = os.getenv("secret")

def extract_text_from_image(file_path: str) -> str:
    # Create Textract client
    client = boto3.client("textract",region_name= "us-east-1", 
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret)

    # Read file as bytes
    with open(file_path, "rb") as file:
        image_bytes = file.read()

    # Call Textract
    response = client.detect_document_text(
        Document={"Bytes": image_bytes}
    )

    # Extract detected text
    extracted_text = []
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            extracted_text.append(item["Text"])

    return "\n".join(extracted_text)



