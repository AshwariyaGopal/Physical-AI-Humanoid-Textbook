# Data Model: ROS 2 Core Concepts Chapter

**Created**: 2025-12-10

This document defines the data model for the content of the "ROS 2 Core Concepts" chapter. As this feature is purely for documentation, the model describes the structure of the Markdown content itself.

## 1. Primary Entity: `DocumentationChapter`

Represents the entire chapter as a single Markdown file.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| **Title** | `String` | The main title of the chapter (H1). |
| **LearningGoals** | `List<String>` | A bulleted list of learning objectives presented at the start. |
| **Sections** | `List<Section>` | An ordered list of the main sections that make up the chapter. |

## 2. Supporting Entity: `Section`

Represents a major section within the chapter, typically denoted by an H2 heading.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| **Title** | `String` | The title of the section. |
| **Content** | `Markdown` | The main explanatory text, including theory, paragraphs, and lists. |
| **CodeExample** | `CodeBlock` (optional) | A syntax-highlighted block of code (e.g., Python). |
| **Subsections** | `List<Section>` (optional) | A list of nested subsections (H3), if any. |

## 3. Example Structure (Conceptual)

```
DocumentationChapter {
  Title: "ROS 2 Core Concepts",
  LearningGoals: [
    "Understand the role of ROS 2 as a robot middleware.",
    "Explain the components of the ROS 2 Computational Graph.",
    ...
  ],
  Sections: [
    Section {
      Title: "ROS 2 Nodes: The Building Blocks",
      Content: "...",
      CodeExample: "...",
      Subsections: []
    },
    Section {
      Title: "ROS 2 Topics: Asynchronous Data Streams",
      Content: "...",
      Subsections: [
        Section {
          Title: "Publishers",
          Content: "...",
          ...
        }
      ]
    },
    ...
  ]
}
```