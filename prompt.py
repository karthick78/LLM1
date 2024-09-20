import os
from constants import openapi_key

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI


os.environ['OPENAI_API_KEY']=openapi_key


demo_template='''I want you to act as a acting financial advisor for people. In an easy way, explain the basics of {financial_concept}.'''

prompt=PromptTemplate(
	input_variables=['financial_concept'],
	template=demo_template
)

prompt.format(financial_concept='income tax')

llm=OpenAI(temperature=0.8)

chain1=LLMChain(llm=llm,prompt=prompt)

chain1.run('imcome tax')
