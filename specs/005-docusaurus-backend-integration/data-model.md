# Data Model: Chat Interface

## Entities

### ChatMessage
Represents a single message in the chat history.

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | Unique identifier (UUID or timestamp-based). |
| `role` | `enum` | `'user'` or `'assistant'`. |
| `content` | `string` | The message text. |
| `timestamp` | `number` | Unix timestamp of when the message was sent/received. |
| `sources` | `Source[]` | Optional list of sources (only for assistant). |

### Source
Represents a citation provided by the assistant.

| Field | Type | Description |
|-------|------|-------------|
| `url` | `string` | URL of the referenced content. |
| `title` | `string` | Title or module name (if available). |
| `chunk_index` | `number` | Internal chunk reference. |

### AppState
Represents the local state of the chat widget.

| Field | Type | Description |
|-------|------|-------------|
| `isOpen` | `boolean` | Whether the chat widget is expanded or collapsed. |
| `messages` | `ChatMessage[]` | History of the current session. |
| `isLoading` | `boolean` | True if waiting for backend response. |
| `error` | `string \| null` | Error message if the last request failed. |
