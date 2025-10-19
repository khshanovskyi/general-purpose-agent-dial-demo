# General-purpose Agent on DIAL platform

> Demo project with General-purpose agent on DIAL platform
> 
> GPA equipped with:
> - WEB Search (DuckDuckGo MCP Server. Performs WEB search and content fetching)
> - Python Code Interpreter (MCP Server. A stateful Python code execution environment with Jupyter kernel support)
> - Image Generation (ImageGen model within DIAL Core)
> - File Content Extractor (Extract content from file (PDF, TXT, CSV). Supports basic pagination)
> - RAG Search (Makes RAG search. Indexed files preserve during conversation in Cache)
> - Long-term memory (Stores in DIAL bucket general info about user)

## Set up and run:
1. Provide `OPENAI_API_KEY` to [core/config.json](core/config.json). `OPENAI_API_KEY` is **required** for `gpt-4o`, `gpt-4.1-nano` and `dall-e-3`. Core config is the place where we provide models and applications configurations for [DIAL Core](https://github.com/epam/ai-dial-core). 
2. Run [docker-compose](docker-compose.yml). It will run [DIAL Chat](https://github.com/epam/ai-dial-chat) with [Themes](https://github.com/epam/ai-dial-chat-themes), [DIAL Core](https://github.com/epam/ai-dial-core), Redis as storage for conversations and files, [DIAL Adapter OpenAI](https://github.com/epam/ai-dial-adapter-openai) to works with OpenAI models, [DIAL Adapter Bedrock](https://github.com/khshanovskyi/ai-dial-adapter-bedrock) to works with Anthropic models (and other), [DDG MCP Server](https://github.com/khshanovskyi/duckduckgo-mcp-server) for WEB Search, [Python Code Interpreter MCP Server](https://github.com/khshanovskyi/mcp-python-code-interpreter).
3. Open http://localhost:3000/ -> Open Marketplace and check if GPT 4o model is working, do the same for GPT 4.1 nano and DALL-E
4. Run [app.py](gpa/app.py). It will start application with Agent. Angent configuration is described in [core/config.json](core/config.json) -> `general-purpose-agent` config.
5. Test GPA:
   - `What is the weather in New York now?`. Expected result: triggered WEB Search
   - Attach [microwave_manual.txt](tests/microwave_manual.txt) and ask: `How should I clean the plate?`. Expected result: should call RAG tool.
   - `Generate picture with smiling cat`. Expected result: DALL-E is triggered with generated picture
   - `Search what is the weather in Kyiv now and based on result generate picture that will represent it`. Expected result: WEB Search + Image generation
   - `What is the sin of 43994289320`. Expected result: triggered Python Code Interpreter
   - Attach [report.csv](tests/report.csv) and ask: `I need chart bar from this data`. Expected result: should get file content and then call PyInterpreter, in response should be generated file as attachment that will be able to see

### Test multi-model
1. Add `ANTHROPIC_API_KEY` to [core/config.json](core/config.json) for Sonnet 4 and restart [docker-compose](docker-compose.yml)
2. Check that Sonnet 4 model is working 
3. In [app.py](gpa/app.py) change the `DEPLOYMENT_NAME` to `claude-sonnet-4` and restart app
4. Test it again with new Orchestration model. 

> DIAL works on [Unified protocol](https://docs.dialx.ai/platform/core/about-core#unified-api). 
> So, all the communication within the Platform is done on it. You can connect different models from different vendors 
> through appropriate adapters and communicate with them with Unified protocol.
