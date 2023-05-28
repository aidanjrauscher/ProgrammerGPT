# ProgrammerGPT

Goal: Create an agent capable of generating and executing code. Also, store generations in a vector db and retrieve when appropraite. 

Stretch: Have agent generate code to web scrape

Inspiration: [Voyager](https://github.com/MineDojo/Voyager)

### TODO: 
- [ ] Expand support to non built-in libraries 
- [x] Store results in vectordb - probably chroma
- [x] Fetch results from vectordb 
- [ ] Improve script interaction - maybe an indefinite while loop?
- [ ] Determine best embedding method
- [ ] Determine best code generation model
- [ ] Determine best vector distance and optimal max distance for retrieved code


### Setup:
1. Install requirements by running ```pip install requirements.txt```
2. Create a .env file with and provide the OPENAI_API_KEY
3. Setup Chroma with ```git clone git@github.com:chroma-core/chroma.git```
4. Build and start Chroma directory with ```docker compose --project-directory chroma/ up -d --build```
5. Describe the code you want to generate using the `task` variable 
6. Run main.py
