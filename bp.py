from browserpilot.agents.gpt_selenium_agent import GPTSeleniumAgent
import selenium_extract
instructions = """Go to google.com
Fill Search Box with "Hello World"
Click Search Button
"""

agent = GPTSeleniumAgent(instructions)
agent.run()
