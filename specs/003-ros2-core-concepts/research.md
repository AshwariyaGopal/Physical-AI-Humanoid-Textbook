# Research: ROS 2 Core Concepts Chapter

**Created**: 2025-12-10

This document summarizes the research and key decisions made for the "ROS 2 Core Concepts" textbook chapter.

## 1. Analogies for Core Concepts

### Decision
-   **Nodes**: Will be described as "workers" or "computational brains" in a factory.
-   **Topics**: Will use the analogy of a "public announcement system" or a "radio station" where anyone can broadcast (publish) or tune in (subscribe).
-   **Services**: Will use the analogy of a "vending machine" or a "service counter" where a specific request is made and a direct, guaranteed response is expected.

### Rationale
These analogies are chosen for their simplicity and clear mapping to the underlying concepts. They provide a strong mental model for beginners to build upon. The factory analogy helps unify the concepts into a single coherent system.

### Alternatives Considered
-   **Post office analogy**: Considered for topics, but the one-to-many nature is better captured by a radio broadcast.
-   **Phone call analogy**: Considered for services, but the vending machine better represents a stateless, immediate transaction which is common for services.

## 2. `rclpy` Code Example Design

### Decision
A single, well-commented Python script will be created. The script will be designed to be launched in different "modes" using command-line arguments (e.g., `python ros2_basics.py publisher`, `python ros2_basics.py server`). This keeps the initial codebase minimal and focused.

### Rationale
For a beginner's first exposure to `rclpy`, managing multiple files can be a distraction from the core API concepts. A single file allows them to see all the components (Node, Publisher, Subscriber, Server, Client) in one place and understand their interactions more easily. It reduces setup friction and cognitive load.

### Alternatives Considered
-   **Multiple Files**: Creating a separate file for each node (e.g., `publisher_node.py`, `subscriber_node.py`). While this is more representative of a real ROS 2 package structure, it was deemed too complex for a first "hello world" style example. This structure will be introduced in later chapters.
-   **Jupyter Notebook**: A notebook could provide interactive cells. However, a standalone Python script is more aligned with standard ROS 2 development practices and is easier to integrate into a launch file later.

### Proposed Code Structure

```python
# Full code to be generated in the implementation phase.
# This is a structural placeholder.

import rclpy
from rclpy.node import Node
# ... other imports

class UniversalNode(Node):
    def __init__(self, mode):
        super().__init__(f'universal_node_{mode}')
        if mode == 'publisher':
            # init publisher
            pass
        elif mode == 'subscriber':
            # init subscriber
            pass
        elif mode == 'server':
            # init server
            pass
        # ... and so on

def main(args=None):
    # parse sys.argv to get the mode
    mode = # ... parse from args
    
    rclpy.init(args=args)
    
    node = UniversalNode(mode)
    
    if mode == 'client':
        # handle client logic
        pass
    else:
        rclpy.spin(node)
        
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```