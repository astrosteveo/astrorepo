# Contributing to AstroRepo

Thank you for your interest in contributing to AstroRepo! This guide will help you get started.

## 🌟 Ways to Contribute

- **Create New Skills** - Add new skills to the marketplace
- **Improve Existing Skills** - Enhance documentation, add features, fix bugs
- **Report Issues** - Help us identify bugs and improvements
- **Improve Documentation** - Make docs clearer and more comprehensive
- **Share Ideas** - Suggest new features and skills

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/astrorepo.git
cd astrorepo

# Add upstream remote
git remote add upstream https://github.com/astrosteveo/astrorepo.git
```

### 2. Create a Branch

```bash
# Update your fork
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/my-awesome-skill
```

### 3. Make Changes

Follow the guidelines below based on what you're contributing.

## 📚 Creating a New Skill

### Step 1: Initialize Skill

```bash
# Use the init tool
python tools/init_skill.py my-awesome-skill --path skills/

# This creates:
# skills/my-awesome-skill/
# ├── SKILL.md
# ├── scripts/
# ├── references/
# └── assets/
```

### Step 2: Develop Your Skill

Edit `skills/my-awesome-skill/SKILL.md`:

```markdown
---
name: my-awesome-skill
description: Brief description of what this skill does and when to use it. Should be specific and clear.
---

# My Awesome Skill

## Overview

Detailed explanation of what this skill enables...

## Core Capabilities

### 1. Main Feature

Describe main functionality...

### 2. Additional Features

...

## Resources

Document scripts, references, and assets...
```

**Guidelines:**

1. **Clear Description** - Explain what the skill does and when to trigger it
2. **Comprehensive Instructions** - Another Claude instance should understand how to use it
3. **Examples** - Provide real-world usage scenarios
4. **Resource Documentation** - Explain all bundled resources

### Step 3: Add Bundled Resources

#### Scripts (`scripts/`)

Executable code for deterministic operations:

```python
#!/usr/bin/env python3
"""
Brief description of what this script does.
"""

# Your code here
```

Make executable:
```bash
chmod +x skills/my-awesome-skill/scripts/my_script.py
```

#### References (`references/`)

Documentation Claude should read when using the skill:

```markdown
# Reference Documentation

Detailed information, API docs, schemas, etc.
```

#### Assets (`assets/`)

Files used in output (templates, images, etc.):

```
assets/
├── templates/
│   └── example.json
└── images/
    └── logo.png
```

### Step 4: Validate

```bash
# Validate your skill
python tools/quick_validate.py skills/my-awesome-skill/

# Should output: ✅ Skill is valid!
```

### Step 5: Test

Test your skill thoroughly:

1. **Manual Testing** - Use the skill in Claude Code
2. **Edge Cases** - Test error conditions
3. **Documentation** - Verify instructions are clear
4. **Resources** - Ensure scripts work, references are helpful

### Step 6: Document

Update README.md to include your skill:

```markdown
#### **my-awesome-skill**
Brief description of the skill.

- Feature 1
- Feature 2

**Triggers**: "keywords", "that trigger", "this skill"
```

## 🔧 Improving Existing Skills

### Finding Issues

- Check [Issues](https://github.com/astrosteveo/astrorepo/issues)
- Look for `good first issue` or `help wanted` labels
- Identify unclear documentation
- Find bugs through usage

### Making Changes

1. **Small Changes** - Documentation fixes, typos → direct PR
2. **Large Changes** - New features, refactoring → open issue first

### Testing Changes

```bash
# Validate after changes
python tools/quick_validate.py skills/SKILL_NAME/

# Test in Claude Code
cp -r skills/SKILL_NAME ~/.claude/skills/
```

## 🐛 Reporting Issues

### Bug Reports

Use this template:

```markdown
**Describe the bug**
Clear description of what's wrong.

**To Reproduce**
Steps to reproduce:
1. Use skill '...'
2. Do action '...'
3. See error

**Expected behavior**
What should happen.

**Actual behavior**
What actually happens.

**Skill**
Which skill has the issue.

**Environment**
- OS: [e.g., Linux, macOS, Windows]
- Claude Code version: [e.g., 1.0.0]
- Python version: [e.g., 3.11]

**Additional context**
Any other relevant information.
```

### Feature Requests

```markdown
**Is your feature request related to a problem?**
Description of the problem.

**Describe the solution**
What you'd like to see.

**Describe alternatives**
Other solutions you've considered.

**Additional context**
Any other relevant information.
```

## 📝 Commit Guidelines

### Commit Message Format

```
type(scope): Brief description

Detailed explanation of changes (optional)

Fixes #issue_number (if applicable)
```

**Types:**
- `feat` - New feature or skill
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Formatting, style changes
- `refactor` - Code refactoring
- `test` - Adding tests
- `chore` - Tooling, dependencies

**Examples:**

```bash
# New skill
git commit -m "feat(skills): Add code-review skill with AI analysis"

# Bug fix
git commit -m "fix(statusline-creator): Fix ANSI code escaping in JSON"

# Documentation
git commit -m "docs(readme): Add troubleshooting section"

# Multiple files
git commit -m "feat(sdd): Enhance spec-validator with edge case detection

- Add edge case taxonomy validation
- Improve validation scoring
- Update documentation

Fixes #42"
```

## 🔀 Pull Request Process

### Before Submitting

1. **Validate** - Run validation on changed skills
2. **Test** - Thoroughly test your changes
3. **Document** - Update relevant documentation
4. **Clean** - Remove debug code, clean up comments
5. **Update** - Pull latest from upstream

```bash
# Update your branch
git checkout main
git pull upstream main
git checkout feature/my-awesome-skill
git rebase main
```

### Submitting PR

1. **Push** to your fork:
   ```bash
   git push origin feature/my-awesome-skill
   ```

2. **Create PR** on GitHub

3. **Fill PR Template**:

```markdown
## Description

Brief description of changes.

## Type of Change

- [ ] New skill
- [ ] Bug fix
- [ ] Feature enhancement
- [ ] Documentation update
- [ ] Tooling improvement

## Testing

Describe testing performed.

## Checklist

- [ ] Skill validates successfully
- [ ] Tested in Claude Code
- [ ] Documentation updated
- [ ] Commit messages follow guidelines
- [ ] No merge conflicts
- [ ] All checks pass
```

### Review Process

1. **Automated Checks** - GitHub Actions validate your PR
2. **Code Review** - Maintainer reviews changes
3. **Feedback** - Address requested changes
4. **Approval** - PR gets approved
5. **Merge** - Maintainer merges PR

## 🎨 Code Style

### Python

- Follow PEP 8
- Use type hints
- Add docstrings
- Maximum line length: 100 characters

```python
#!/usr/bin/env python3
"""
Module description.
"""

from typing import Dict, List


def my_function(param: str) -> Dict[str, str]:
    """
    Brief description.

    Args:
        param: Parameter description

    Returns:
        Return value description
    """
    return {"result": param}
```

### Bash

- Use `#!/bin/bash` shebang
- Set strict mode: `set -euo pipefail`
- Comment complex logic
- Use meaningful variable names

```bash
#!/bin/bash
# Description of what this script does

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

main() {
    local input="$1"
    # Process input
    echo "Result: $input"
}

main "$@"
```

### Markdown

- Use ATX-style headers (`#`)
- One sentence per line in paragraphs
- Code blocks with language specifiers
- Lists with consistent formatting

## 🏗️ Skill Structure Best Practices

### Progressive Disclosure

1. **Metadata** - Always in context (name, description)
2. **SKILL.md** - Loaded when skill runs (<5k words)
3. **References** - Loaded as needed (unlimited)

### Resource Organization

- **scripts/** - For code that's repeatedly rewritten
- **references/** - For documentation Claude reads
- **assets/** - For files used in output

### Documentation

- Clear trigger conditions
- Concrete examples
- Workflow descriptions
- Resource explanations

## 🧪 Testing

### Manual Testing

1. Install skill in Claude Code
2. Test main workflows
3. Test edge cases
4. Verify error handling
5. Check documentation clarity

### Validation

```bash
# Validate single skill
python tools/quick_validate.py skills/my-skill/

# Validate all skills
for skill in skills/*/; do
  python tools/quick_validate.py "$skill"
done
```

## 📊 Quality Standards

Skills should meet these standards:

- [ ] Passes validation
- [ ] Has clear, specific description
- [ ] Includes usage examples
- [ ] Documents all resources
- [ ] Scripts are executable
- [ ] References are helpful
- [ ] Assets are used appropriately
- [ ] README updated
- [ ] No obvious bugs
- [ ] Works in real scenarios

## 🎯 Skill Ideas

Looking for contribution ideas?

**Development Tools:**
- Code review skill
- Refactoring assistant
- Performance profiler
- Security auditor

**Documentation:**
- API doc generator
- Changelog creator
- README builder

**Testing:**
- E2E test generator
- Load test creator
- Security test builder

**DevOps:**
- CI/CD pipeline creator
- Dockerfile generator
- Kubernetes config builder

**Productivity:**
- Git workflow automation
- Project scaffolder
- Time tracker
- Task manager

## 💬 Communication

- **Issues** - For bugs and feature requests
- **Discussions** - For questions and ideas
- **PR Comments** - For code-specific discussions

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in skill documentation (if applicable)

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

- Open a [Discussion](https://github.com/astrosteveo/astrorepo/discussions)
- Comment on related [Issue](https://github.com/astrosteveo/astrorepo/issues)
- Reach out to [@astrosteveo](https://github.com/astrosteveo)

Thank you for contributing to AstroRepo! 🚀
