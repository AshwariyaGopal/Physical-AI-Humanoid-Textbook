# Quickstart: Docusaurus Chat Integration

## Prerequisites
- Node.js 18+
- Backend service running (see Spec-3/Spec-2) at `http://localhost:8000`

## Setup

1.  **Install dependencies** (if any new ones needed, likely none for standard React):
    ```bash
    npm install
    ```

2.  **Configure Backend URL**:
    Create or update `.env` file in the root:
    ```env
    BACKEND_URL=http://localhost:8000
    ```
    *Note: Docusaurus uses `customFields` in `docusaurus.config.ts` to expose env vars.*

3.  **Start Docusaurus**:
    ```bash
    npm start
    ```

4.  **Start Backend**:
    (In a separate terminal, navigate to backend directory)
    ```bash
    cd backend
    uvicorn main:app --reload
    ```

## Usage

1.  Open the textbook at `http://localhost:3000`.
2.  Look for the "Ask AI" floating button in the bottom-right corner.
3.  Click to open the chat widget.
4.  Type a question (e.g., "What is ROS 2?") and hit Enter.
5.  Verify the response appears with source links.
