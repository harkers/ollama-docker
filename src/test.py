from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler 
                                 
llm = Ollama(
    base_url="http://l92.168.10.60:11434",
    model="llama2-uncensored", 
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

llm("hello:")