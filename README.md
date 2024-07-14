Simple chat model using Open source llm model Google palm

library required are:
langchain
langchain_community
faiss-gpu
unstructured

I have used GooglePalm which is an opensource model.
to use GooglePalm you must have an API Key which you can get from aistudio.google.com
i have loaded the url using unstructured url loader then converted it into chunks, then storing it in the vector form using GooglePalmembeddings and then finally indexing it using FAISS
.
