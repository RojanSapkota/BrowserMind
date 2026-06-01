import asyncio
import os
import sys

from dotenv import load_dotenv

from browser_use import Agent
from browser_use.browser import BrowserSession
from browser_use.tools.service import Tools

load_dotenv()

SPEED_OPTIMIZATION_PROMPT = """
Speed optimization instructions:
- Be extremely concise and direct in your responses
- Get to the goal as quickly as possible
- Use multi-action sequences whenever possible to reduce steps
"""

def get_llm(provider: str):
	if provider == 'anthropic':
		from browser_use.llm import ChatAnthropic
		api_key = os.getenv('ANTHROPIC_API_KEY')
		if not api_key:
			raise ValueError('ANTHROPIC_API_KEY is not set')
		return ChatAnthropic(model='claude-3-5-sonnet-20240620', temperature=0.0)
	
	elif provider == 'openai':
		from browser_use import ChatOpenAI
		api_key = os.getenv('OPENAI_API_KEY')
		if not api_key:
			raise ValueError('OPENAI_API_KEY is not set')
		return ChatOpenAI(model='gpt-4.1', temperature=0.0)
	
	elif provider == 'groq':
		from browser_use import ChatGroq
		api_key = os.getenv('GROQ_API_KEY')
		if not api_key:
			raise ValueError('GROQ_API_KEY is not set')
		return ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct', temperature=0.0)
	
	elif provider == 'gemini':
		from browser_use import ChatGoogle
		api_key = os.getenv('GOOGLE_API_KEY')
		if not api_key:
			raise ValueError('GOOGLE_API_KEY is not set')
		return ChatGoogle(model='gemini-2.0-flash-lite', temperature=0.0)
	
	elif provider == 'ollama':
		from browser_use import ChatOllama
		return ChatOllama(model='llama3.2:latest')

	else:
		raise ValueError(f'Unsupported provider: {provider}')


def initialize_agent(query: str, provider: str):
	llm = get_llm(provider)
	
	browser_session = BrowserSession(
		headless=True,
		disable_security=False,
		window_size={'width': 1280, 'height': 720},
		minimum_wait_page_load_time=0.1,
		wait_between_actions=0.1,
		)

	return Agent(
		task=query,
		llm=llm,
		tools=Tools(),
		browser_session=browser_session,
		use_vision=False,
		max_actions_per_step=1,
		extend_system_message=SPEED_OPTIMIZATION_PROMPT
	)

async def run_agent(query: str, provider: str = 'groq'):
	if get_llm(provider) is None:
		raise ValueError(f"LLM provider '{provider}' is not properly configured.")
	agent = initialize_agent(query, provider)
	await agent.run()

if __name__ == "__main__":
	query = input("Enter your task for the agent: ")
	asyncio.run(run_agent(query, provider='groq'))
