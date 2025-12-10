# Data Model: URDF for Humanoid Bipedal Kinematics Chapter

**Created**: 2025-12-10

This document defines the data model for the content of the "URDF for Humanoid Bipedal Kinematics" chapter. As this feature is purely for documentation, the model describes the structure of the Markdown content itself.

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
| **CodeExample** | `CodeBlock` (optional) | A syntax-highlighted block of code (e.g., XML for URDF). |
| **Table** | `MarkdownTable` (optional) | A markdown formatted table (e.g., URDF vs SDF comparison). |
| **Subsections** | `List<Section>` (optional) | A list of nested subsections (H3), if any. |

## 3. Example Structure (Conceptual)

```
DocumentationChapter {
  Title: "URDF for Humanoid Bipedal Kinematics",
  LearningGoals: [
    "Define kinematic structure using URDF.",
    "Understand humanoid bipedal kinematics constraints.",
    "Compare URDF and SDF for physics simulation.",
  ],
  Sections: [
    Section {
      Title: "URDF Core Components: Links and Joints",
      Content: "...",
      CodeExample: "...",
      Subsections: []
    },
    Section {
      Title: "URDF vs. SDF: Robot Description for Simulation",
      Content: "...",
      Table: "...",
      Subsections: []
    },
    ...
  ]
}
```
