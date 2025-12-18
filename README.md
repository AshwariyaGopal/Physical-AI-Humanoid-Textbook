# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## Installation

```bash
yarn
```

## Local Development

```bash
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```bash
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deployment

Using SSH:

```bash
USE_SSH=true yarn deploy
```

Not using SSH:

```bash
GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

## AI Assistant Integration

This textbook features an integrated RAG-based AI assistant.

### Setup
1. Ensure the backend FastAPI service is running (see `backend/README.md`).
2. Set the `BACKEND_URL` in your `.env` file or environment.
3. Start the Docusaurus site.

### Usage
Click the "Ask Assistant" button in the bottom-right corner of any page to open the chat interface.
"# Physical-AI-Humanoid-Textbook" 
