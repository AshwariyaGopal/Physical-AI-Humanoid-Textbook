# Research: Docusaurus Backend Integration

## Decisions

### 1. Frontend Framework: React (Docusaurus)
- **Decision**: Use React components within Docusaurus.
- **Rationale**:
  - Docusaurus is React-based, allowing seamless integration of custom components.
  - Matches the existing tech stack of the textbook platform.
  - "Swizzling" or creating a custom component is the standard way to extend Docusaurus.

### 2. State Management: React `useState` / `useEffect`
- **Decision**: Use standard React hooks for managing chat state (messages, loading, error).
- **Rationale**:
  - Simple requirements (single chat session per page load) do not justify complex state management libraries like Redux or Zustand.
  - Sufficient for handling the request/response lifecycle.

### 3. API Communication: `fetch` API
- **Decision**: Use the native browser `fetch` API.
- **Rationale**:
  - No need for extra dependencies like `axios` for simple POST requests.
  - Built-in, lightweight, and fully capable of handling JSON payloads.

### 4. Styling: CSS Modules or Infima
- **Decision**: Use Docusaurus's default styling system (likely CSS modules or Infima classes).
- **Rationale**:
  - Ensures visual consistency with the rest of the textbook.
  - Avoids introducing new CSS frameworks.

### 5. Backend Connection: Configurable URL
- **Decision**: Use `docusaurus.config.ts` `customFields` or environment variables (build-time) to configure the backend URL.
- **Rationale**:
  - Allows different URLs for development (`localhost:8000`) and production (deployed URL).
  - Standard Docusaurus configuration pattern.

## Implementation Details

### Chat Component
- **Path**: `src/components/Chat/index.tsx` (or similar).
- **Structure**:
  - `ChatWindow`: Container for messages.
  - `MessageList`: Renders user and assistant messages.
  - `InputArea`: Text input and submit button.
- **Integration**: Can be embedded in specific pages (MDX) or added to the global layout (swizzling `Root` or `DocItem`). For this feature, embedding via MDX or a specific page is a good start, but a floating widget or sidebar integration might be better for "textbook-wide" access.
  - *Refinement*: The spec asks to "enable users to ask questions... without leaving the page". A floating chat widget or a sidebar component is best. Let's aim for a **Floating Chat Widget** to avoid disrupting the reading flow.

### Backend Endpoint
- **URL**: Configurable, defaulting to `http://localhost:8000`.
- **Endpoint**: `/ask` (POST).
- **Payload**: `{"query": "..."}`.
- **Response**: `{"answer": "...", "sources": [...]}`.

## Unknowns & Risks
- **CORS**: The backend MUST have CORS configured to allow requests from the Docusaurus origin (localhost:3000 and production domain).
  - *Mitigation*: Ensure backend task includes CORS setup (Task T013 in Spec-3 covered this).
- **Deployment**: Docusaurus is static (SSG). The backend is dynamic. They will likely be hosted separately (e.g., Vercel for frontend, Railway/Render for backend) or backend requires a server.
  - *Assumption*: Backend deployment is out of scope for *this* feature (integration), but the frontend must be *ready* for it (configurable URL).

