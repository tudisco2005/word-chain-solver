
# Word Connect Game

## Overview

Word Connect is a word-based puzzle game where players need to find words that connect to each other by changing one letter at a time. The game starts with a given start word and ends with a target word, and players must find the shortest path between them.

## How to Play

1. Start with a given start word
2. Find words that differ by only one letter
3. Connect the words to form a path from start to finish
4. Try to find the shortest possible path

## Implementation Details

The game is implemented using Python and utilizes Breadth-First Search (BFS) algorithm to find the shortest path between words.

### BFS Algorithm

The BFS implementation uses a queue to keep track of nodes to visit. It starts with the start word and explores all neighboring words until it reaches the target word.

```python
from collections import deque

def bfs(start: str, end: str, adyacents: dict[str, List[str]]) -> List[str]:
    queue: deque = deque()
    queue.append([start])
    visited: set[str] = set()

    while queue:
        node = queue.popleft()
        
        for child in node:
            if child == end:
                return node
            
            if child not in visited:
                visited.add(child)
                for ady in adyacents[child]:
                    queue.append(node + [ady])
    
    return []
```

### Word Connection Validation

Words are considered connected if they differ by only one letter. This is checked using the following function:

```python
def is_valid_connection(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    
    return diff_count == 1
```

## Usage

To play the game, you can modify the `START_WORD`, `END_WORD`, and `WORD_LENGTH` variables in the main script. The game will then generate a list of valid words within the specified length and create connections between them based on the `is_valid_connection` function.

## Contributing

Contributions to this project are welcome! Please feel free to submit pull requests or open an issue if you have suggestions or want to contribute to the game.
