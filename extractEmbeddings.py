from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings(model='mistral')
text = "This is a test document."
text2='This is new text2'
query_result = embeddings.embed_query(text)
query_result2=embeddings.embed_query(text2)
print(query_result)
print(query_result2)