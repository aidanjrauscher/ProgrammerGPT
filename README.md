# ProgrammerGPT

Goal: Create an agent capable of generating and executing code. Also, store generations in a vector db and retrieve when appropraite. 

Stretch: Have agent generate code to achieve desired tasks 

Inspiration: [Voyager](https://github.com/MineDojo/Voyager)

### TODO: 
- [ ] Expand support to non built-in libraries 
- [ ] Store results in vectordb - probably chroma
- [ ] Fetch results from vectordb 
- [ ] Fix script interaction - maybe an indefinite while loop?


### Setup:
1. Install requirements by running ```pip install requirements.txt```
2. Create a .env file with and provide the OPENAI_API_KEY
3. Setup Chroma with ```git clone git@github.com:chroma-core/chroma.git```
4. Build and start Chroma directory with ```docker compose --project-directory chroma/ up -d --build ```
