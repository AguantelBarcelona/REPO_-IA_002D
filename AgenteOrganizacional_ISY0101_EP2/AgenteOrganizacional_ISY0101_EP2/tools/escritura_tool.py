from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama

def generar_informe(tema):
    llm = Ollama(model="gwen2.5:3b-instruct")
    template = PromptTemplate(
        input_variables=["tema"],
        template="Redacta un informe breve y profesional sobre {tema}."
    )
    chain = LLMChain(llm=llm, prompt=template)
    return chain.run(tema)
