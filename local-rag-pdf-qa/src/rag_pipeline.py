"""Main RAG pipeline implementation."""

from .pdf_processor import PDFProcessor
from .embeddings import EmbeddingsGenerator
from .vector_store import VectorStore
from .llm_interface import OllamaInterface

class RAGPipeline:
    def __init__(self, config):
        self.config = config
        self.pdf_processor = PDFProcessor(config)
        self.embeddings_generator = EmbeddingsGenerator(config)
        self.vector_store = VectorStore(config)
        self.llm = OllamaInterface(config)
    
    def process_document(self, pdf_path):
        """Process a PDF document and add to vector store."""
        text = self.pdf_processor.extract_text(pdf_path)
        chunks = self._chunk_text(text)
        embeddings = self.embeddings_generator.generate(chunks)
        self.vector_store.add_documents(chunks, embeddings)
    
    def query(self, question):
        """Query the system with a question."""
        query_embedding = self.embeddings_generator.generate(question)
        relevant_docs = self.vector_store.search(query_embedding)
        
        context = "\n".join([doc for doc, _ in relevant_docs])
        prompt = self._construct_prompt(question, context)
        
        return self.llm.generate(prompt)
    
    def _chunk_text(self, text, chunk_size=1000):
        """Split text into chunks."""
        words = text.split()
        chunks = []
        current_chunk = []
        
        for word in words:
            current_chunk.append(word)
            if len(" ".join(current_chunk)) >= chunk_size:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
        
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        return chunks
    
    def _construct_prompt(self, question, context):
        """Construct prompt for the LLM."""
        return f"""Context: {context}

Question: {question}

Please answer the question based on the context provided above."""