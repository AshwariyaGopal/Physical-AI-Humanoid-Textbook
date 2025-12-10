# Quickstart: VLA LLM Cognitive Planning API

This quickstart guide will help you quickly get started with the Vision-Language-Action (VLA) LLM Cognitive Planning API. This API allows you to translate natural language commands into structured YAML sequences of low-level ROS 2 actions for robotic systems.

## 1. API Overview

The VLA LLM Cognitive Planning API exposes a single primary endpoint: `/vla/plan`.
You send a natural language command to this endpoint, and it returns a YAML string representing a sequence of ROS 2 actions.

## 2. Making a Request

You can use `curl` or any HTTP client to send a `POST` request to the API.

### Example using `curl`

Assuming the API is running locally on `http://localhost:8000`:

```bash
curl -X POST http://localhost:8000/vla/plan \
-H "Content-Type: application/json" \
-d '{
  "command": "Go to the charging station and dock."
}'
```

### Example using Python `requests`

```python
import requests
import json

api_url = "http://localhost:8000/vla/plan"
command = "Pick up the red ball from the table and place it in the basket."

payload = {"command": command}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

    response_data = response.json()
    if response.status_code == 200:
        print("Generated ROS 2 Plan (YAML):")
        print(response_data["plan_yaml"])
    else:
        print(f"Error: {response_data.get('error', 'Unknown Error')}")
        print(f"Details: {response_data.get('details', 'No details provided.')}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

```

## 3. Expected Response

### Successful Response (Status Code: `200 OK`)

A successful response will contain a `plan_yaml` field with the generated ROS 2 action sequence.

```json
{
  "plan_yaml": "- action: nav2_action_server/NavigateToPose\n  parameters:\n    x: 1.0\n    y: 0.5\n    theta: 0.0\n- action: grasp_action_server/GraspObject\n  parameters:\n    object_id: \"red_ball\""
}
```

The `plan_yaml` field will contain a string that can be parsed as a YAML document.

### Error Response (Status Code: `400 Bad Request` or `500 Internal Server Error`)

If the command is invalid, ambiguous, or an internal error occurs, you will receive an error response.

```json
{
  "error": "AmbiguousCommand",
  "details": "The command 'Do something' is too vague. Please specify a clear action and target."
}
```
Or for a physically impossible command:
```json
{
  "error": "PhysicallyImpossible",
  "details": "The command 'Fly to the moon' cannot be executed by this robot."
}
```

## 4. Interpreting Errors

The `error` field provides a high-level category of the issue, while `details` offers a more specific explanation. Use these to refine your natural language commands or to debug integration issues.

