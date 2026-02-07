# Document Loader

Document Loaders are a crucial component of **Retrieval-Augmented Generation (RAG)** pipelines, responsible for extracting and loading data from various sources into a format that can be processed by LangChain applications.

## RAG Pipeline Components

1. **Document Loader** - Load data from various sources
2. **Text Splitters** - Split documents into manageable chunks
3. **Vector Databases** - Store and index document embeddings
4. **Retrievers** - Retrieve relevant documents based on queries

---

## Types of Document Loaders

### 1. TextLoader
Loads plain text files (`.txt`) for processing. Ideal for simple text-based documents where you need to generate summaries or perform analysis.

**Use Case:** Loading and summarizing text files

### 2. PyPDFLoader
Loads PDF documents and converts them into processable text format. Each page of the PDF is treated as a separate document.

**Example:** A 25-page PDF will generate 25 separate document objects, one per page.

### 3. WebBaseLoader
Extracts content from web pages using two methods:
- HTTP requests
- BeautifulSoup for HTML parsing

**Use Case:** Scraping and loading content from websites

### 4. CSVLoader
Loads data from CSV files, converting structured tabular data into document format.

**Use Case:** Processing datasets and tabular information

---

## DirectoryLoader

The **DirectoryLoader** enables loading multiple documents from a directory in a single operation, making it efficient for bulk document processing.

---

## Loading Strategies: Load vs Lazy Load

### Load (Eager Loading)
- Loads all documents at once
- Faster for small datasets
- Higher memory consumption
- All files loaded into memory immediately

### Lazy Load
- Returns a generator that loads documents one by one
- Memory efficient for large datasets
- Processes files sequentially
- Better for directories with many large files

### When to Use Which?

- **Use Lazy Load:** When working with large directories or multiple large files to avoid memory issues and improve performance
- **Use Load:** When working with smaller datasets where loading everything at once is manageable

---

