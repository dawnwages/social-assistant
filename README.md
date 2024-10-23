# Advocacy AI Assistant

## Project Setup

```sh
npm install
```

### Run Project

The project consists of a Vue/Vite frontend and an Azure Functions API. The SWA CLI must be used to simulate the running env of a SWA application, including api request routing and auth. 

All commands are relative to the root folder. 

#### Run Vue/Vite App

```sh
npm run dev
```

### Run Functions API
Instructions to [install Azure Functions locally using Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-csharp#install-the-azure-functions-core-tools)
```sh
cd api
func start
```

### Run SWA Emulator

```sh
swa start http://localhost:5173
```

Access the application on http://localhost:4280
