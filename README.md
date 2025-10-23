# 🚀 AstroRepo

**AstroSteveo's curated collection of powerful Claude Code skills**

A comprehensive marketplace of production-ready skills for Claude Code, featuring spec-driven development workflows, productivity tools, and advanced automation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skills-blue)](https://claude.com/claude-code)

## 🌟 Features

- **📚 Spec-Driven Development** - Complete SDD framework with 5 integrated skills
- **🎨 Productivity Tools** - Beautiful statuslines and workflow automation
- **🛠️ Professional Quality** - Production-ready with testing, validation, and documentation
- **⚡ Advanced Integrations** - Hooks, slash commands, subagents, and helper scripts
- **🔄 Continuous Updates** - Regular improvements and new skills

## 📦 Quick Start

### Installation

Install the entire marketplace with Claude Code's plugin system:

```bash
/plugin add marketplace https://github.com/astrosteveo/astrorepo
```

Or install individual skills:

```bash
# Clone the repository
git clone https://github.com/astrosteveo/astrorepo.git
cd astrorepo

# Install specific skill
cp -r skills/statusline-creator ~/.claude/skills/
```

### Verification

Check installed skills:

```bash
/skills list
```

## 🎯 Available Skills

### Spec-Driven Development Suite

Complete workflow for building software with specifications:

#### **spec-writer**
Create comprehensive, testable specifications using the SDL format.

- Guided specification creation
- Edge case taxonomy integration
- Acceptance criteria generation
- Template system

**Triggers**: `/spec`, "write spec", "create specification"

#### **spec-validator**
Validate specifications before implementation to ensure completeness.

- Format validation
- Completeness checks
- Testability verification
- Edge case coverage analysis

**Triggers**: `/validate-spec`, "validate spec"

#### **implement-from-spec**
Build features following specifications with TDD workflow.

- Spec-guided implementation
- Automatic test running
- Iteration limits
- Progress tracking

**Triggers**: `/implement-spec`, "implement from spec"

#### **test-from-spec**
Generate comprehensive test suites from specifications.

- Unit, integration, and E2E tests
- Edge case coverage
- TDD workflow support

**Triggers**: `/tests-from-spec`, "generate tests from spec"

#### **spec-sync**
Keep specifications synchronized with code changes.

- Drift detection
- Coverage analysis
- Alignment validation
- Update suggestions

**Triggers**: `/sync-spec`, "sync specification"

### Productivity Tools

#### **statusline-creator**
Design beautiful, performant statuslines for Claude Code.

- 6 pre-built templates
- Custom design workflow
- Helper scripts for git/system info
- Testing and validation tools
- Hooks integration examples

**Features**:
- Templates: minimal, git-focused, full-featured, powerline, modern-clean, developer
- Dynamic data: git status, system metrics, custom commands
- Performance optimized: < 100ms execution
- ANSI colors, Unicode symbols, conditional display

**Triggers**: `/statusline`, "create statusline", "customize statusline"

## 🏗️ Repository Structure

```
astrorepo/
├── plugin.json              # Marketplace metadata
├── README.md                # This file
├── LICENSE                  # MIT License
├── skills/                  # All available skills
│   ├── spec-writer/
│   ├── spec-validator/
│   ├── implement-from-spec/
│   ├── test-from-spec/
│   ├── spec-sync/
│   └── statusline-creator/
├── agents/                  # Specialized subagents
│   ├── spec-architect.md
│   ├── implementation-reviewer.md
│   └── test-engineer.md
├── commands/                # Slash commands
│   ├── spec.md
│   ├── implement-spec.md
│   ├── validate-spec.md
│   ├── tests-from-spec.md
│   └── sync-spec.md
├── hooks/                   # Hook configurations
│   └── hooks.json
├── templates/               # Specification templates
│   ├── basic.md
│   └── feature.md
├── tools/                   # Skill development tools
│   ├── init_skill.py
│   ├── package_skill.py
│   └── quick_validate.py
├── docs/                    # Documentation
│   ├── installation.md
│   ├── creating-skills.md
│   └── contributing.md
└── .github/
    └── workflows/
        ├── validate-skills.yml
        └── package-release.yml
```

## 🎓 Usage Examples

### Example 1: Create a Statusline

```
User: "Create a minimal statusline for me"

Claude (using statusline-creator):
1. Reviews available templates
2. Recommends 'minimal' template
3. Installs: ./scripts/install_statusline.sh minimal --backup
4. Statusline appears: "project main"
```

### Example 2: Spec-Driven Feature Development

```
User: "/spec user authentication"

Claude (using spec-writer):
1. Gathers requirements
2. Creates comprehensive spec with SDL format
3. Validates completeness

User: "/implement-spec specs/user-authentication.md"

Claude (using implement-from-spec):
1. Reads specification
2. Generates tests first (TDD)
3. Implements feature
4. Runs tests and iterates
5. Completes implementation
```

### Example 3: Validate Existing Spec

```
User: "/validate-spec specs/api-endpoint.md"

Claude (using spec-validator):
1. Checks format compliance
2. Verifies completeness
3. Analyzes edge case coverage
4. Generates validation report (scored 0-100)
5. Provides improvement suggestions
```

## 🛠️ Creating Your Own Skills

AstroRepo includes professional tooling for skill development:

### Initialize New Skill

```bash
cd astrorepo
python tools/init_skill.py my-awesome-skill --path skills/
```

### Develop Skill

1. Edit `skills/my-awesome-skill/SKILL.md`
2. Add helper scripts to `scripts/`
3. Add reference docs to `references/`
4. Add assets to `assets/`

### Validate Skill

```bash
python tools/quick_validate.py skills/my-awesome-skill/
```

### Package Skill

```bash
python tools/package_skill.py skills/my-awesome-skill/ dist/
```

See [docs/creating-skills.md](docs/creating-skills.md) for detailed guide.

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-skill`
3. **Develop your skill** using the tools provided
4. **Validate**: `python tools/quick_validate.py skills/your-skill/`
5. **Test thoroughly** with real workflows
6. **Commit**: `git commit -m 'Add amazing-skill'`
7. **Push**: `git push origin feature/amazing-skill`
8. **Open Pull Request**

### Contribution Guidelines

- Follow existing skill structure patterns
- Include comprehensive documentation
- Add tests where applicable
- Validate before submitting
- Update README with new skill

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📋 Roadmap

### Current Focus (v1.x)
- ✅ SDD Framework (5 skills)
- ✅ Statusline Creator
- ✅ Professional tooling
- ✅ Comprehensive documentation

### Upcoming (v2.x)
- 🔄 AI code review skill
- 🔄 Project scaffolding skill
- 🔄 Documentation generator skill
- 🔄 Performance profiler skill
- 🔄 Git workflow automation skill

### Future (v3.x)
- 📋 Database schema designer
- 📋 API documentation generator
- 📋 CI/CD pipeline creator
- 📋 Security audit skill
- 📋 Refactoring assistant

## 📚 Documentation

- **[Installation Guide](docs/installation.md)** - Detailed setup instructions
- **[Creating Skills](docs/creating-skills.md)** - Skill development guide
- **[Contributing](docs/contributing.md)** - How to contribute
- **[Changelog](CHANGELOG.md)** - Version history

## 🔧 Troubleshooting

### Skills Not Loading

```bash
# Check plugin installation
/plugin list

# Reinstall marketplace
/plugin remove astrorepo
/plugin add marketplace https://github.com/astrosteveo/astrorepo
```

### Slash Commands Not Working

```bash
# Verify commands are installed
ls ~/.claude/commands/

# Reinstall commands
cp -r commands/* ~/.claude/commands/
```

### Permission Issues

```bash
# Make scripts executable
find skills/ -name "*.sh" -exec chmod +x {} \;
find skills/ -name "*.py" -exec chmod +x {} \;
```

## 📊 Stats

- **Total Skills**: 6
- **Total Lines of Code**: ~10,000+
- **Languages**: Python, Bash, Markdown
- **Test Coverage**: Comprehensive validation
- **Documentation**: 100% coverage

## 🌐 Community

- **Issues**: [GitHub Issues](https://github.com/astrosteveo/astrorepo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/astrosteveo/astrorepo/discussions)
- **Author**: [@astrosteveo](https://github.com/astrosteveo)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Anthropic** - For Claude Code and the skill system
- **Claude** - For helping build these skills
- **Community** - For feedback and contributions

## 🎯 Mission

To create the most comprehensive, production-ready collection of Claude Code skills that empower developers to build better software faster.

---

**Made with ❤️ by AstroSteveo**

*Star ⭐ this repo if you find it useful!*
