**Objective**:  
This assignment is designed to deepen your understanding of the parameters used with the OpenAI Chat Completion API. You will explain the purpose and functionality of the following terms or parameters in your own words.

**Terms/Parameters to Explain**:

- Messages:
  - ` `Contains the conversation history b/w the user and the AI.
  - Takes two args: role, content in form of dict.
- Model  
  - Choose the model later to be used for the content generation. i.e. prompts.
  - Takes the model’s name and its version as str.
- Max Completion Tokens
  - As the tokens help control the length of the response (prompt),
  - Helps set the limit for the tokens
- n
  - The no. of responses we need AI to generate.
- Stream
  - Used to generate real-time output in form of chunks instead of a single output.
- Temperature
  - Control the creativity/randomness of the model (LLM).
  - Generally, its value lies 0-1.
- Top\_p
  - Control the diversity of response. 
- Tools
  - Pass in the tools required to complete the job. i.e. “tools”: [tool1, tool2, tool3]
  - Takes a dict as input.

