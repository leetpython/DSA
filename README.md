# LeetPy Solutions

## File Structure

```
algorithms/ --> TODO
data-structures/ --> TODO
solutions/
└── platform-name/
    ├── metadata.json
    └── question-id/
        ├── README.md
        ├── __init__.py
        └── metadata.json
```

## Metadata Format

### `platform-name/metadata.json`

```javascript
{
    "name": "LeetCode", // Human readable name
    "id": "leetcode", // Lowercase letters / digits / dashes
    "url": "https://leetcode.com/" // The platform's homepage URL
}
```

### `question-id/metadata.json`

```javascript
{
    "name": "Two Sum", // Human readable name
    "id": "two-sum", // Lowercase letters / digits / dashes (must be unique to the platform)
    "url": "https://leetcode.com/problems/two-sum", // The question's homepage URL
    "difficulty": "Easy", // Human readable difficulty level (May be blank)
    "tags": ["Array", "Hash Table"], // A list of 0 or more tags
    "keywords": [...] // A list of 0 or more keywords to be used while searching (independent of tags)
}
```