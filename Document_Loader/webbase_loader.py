from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.vegnonveg.com/products/nike-dunk-low-retro-whitemidnight-navy'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)