# Installation Guide

Complete guide for installing AstroRepo and its skills.

## Prerequisites

- Claude Code installed
- Git (for repository cloning)
- Python 3.11+ (for some helper scripts)
- Bash (for shell scripts)

## Installation Methods

### Method 1: Install Entire Marketplace (Recommended)

Install all skills at once using Claude Code's plugin system:

```bash
/plugin add marketplace https://github.com/astrosteveo/astrorepo
```

**Advantages:**
- ✅ One command installation
- ✅ Automatic updates
- ✅ Easy management
- ✅ All skills available

**Verification:**
```bash
/plugin list
```

You should see `astrorepo` in the list.

### Method 2: Install Individual Skills

Install specific skills you need:

#### From Release (Recommended)

```bash
# Download specific skill
wget https://github.com/astrosteveo/astrorepo/releases/latest/download/statusline-creator.zip

# Extract to Claude skills directory
unzip statusline-creator.zip -d ~/.claude/skills/

# Make scripts executable (if applicable)
chmod +x ~/.claude/skills/statusline-creator/scripts/*.sh
```

#### From Source

```bash
# Clone repository
git clone https://github.com/astrosteveo/astrorepo.git
cd astrorepo

# Install specific skill
cp -r skills/statusline-creator ~/.claude/skills/

# Make scripts executable
chmod +x ~/.claude/skills/statusline-creator/scripts/*.sh
```

### Method 3: Install All Skills Manually

```bash
# Clone repository
git clone https://github.com/astrosteveo/astrorepo.git
cd astrorepo

# Install all skills
for skill in skills/*/; do
  cp -r "$skill" ~/.claude/skills/
done

# Make all scripts executable
find ~/.claude/skills -name "*.sh" -exec chmod +x {} \;
find ~/.claude/skills -name "*.py" -exec chmod +x {} \;
```

### Method 4: Development Installation

For contributing or developing:

```bash
# Clone repository
git clone https://github.com/astrosteveo/astrorepo.git
cd astrorepo

# Symlink skills (changes reflect immediately)
for skill in skills/*/; do
  skill_name=$(basename "$skill")
  ln -s "$(pwd)/skills/$skill_name" ~/.claude/skills/
done
```

## Post-Installation

### Verify Installation

Check installed skills:

```bash
/skills list
```

You should see all AstroRepo skills listed.

### Install Slash Commands (Optional)

For quick access to SDD framework:

```bash
cd astrorepo
cp commands/* ~/.claude/commands/
```

Now you can use:
- `/spec` - Create new specification
- `/validate-spec` - Validate specification
- `/implement-spec` - Implement from spec
- `/tests-from-spec` - Generate tests
- `/sync-spec` - Sync spec with code

### Install Hooks (Optional)

For automated workflows:

```bash
# Copy or merge hooks configuration
cp hooks/hooks.json ~/.claude/hooks.json

# Or merge with existing hooks
python tools/merge_hooks.py hooks/hooks.json ~/.claude/hooks.json
```

### Configure Environment

Some skills may require environment variables:

```bash
# Add to ~/.bashrc or ~/.zshrc
export CLAUDE_SKILLS_PATH=~/.claude/skills
export ASTROREPO_PATH=/path/to/astrorepo
```

## Upgrading

### Upgrade via Plugin System

```bash
/plugin update astrorepo
```

### Upgrade Manual Installation

```bash
cd astrorepo
git pull origin main

# Reinstall skills
for skill in skills/*/; do
  cp -r "$skill" ~/.claude/skills/
done
```

### Upgrade from Release

```bash
# Download latest release
wget https://github.com/astrosteveo/astrorepo/releases/latest/download/SKILL_NAME.zip

# Backup existing
mv ~/.claude/skills/SKILL_NAME ~/.claude/skills/SKILL_NAME.backup

# Install new version
unzip SKILL_NAME.zip -d ~/.claude/skills/
```

## Uninstallation

### Remove via Plugin System

```bash
/plugin remove astrorepo
```

### Remove Manual Installation

```bash
# Remove all AstroRepo skills
rm -rf ~/.claude/skills/spec-writer
rm -rf ~/.claude/skills/spec-validator
rm -rf ~/.claude/skills/implement-from-spec
rm -rf ~/.claude/skills/test-from-spec
rm -rf ~/.claude/skills/spec-sync
rm -rf ~/.claude/skills/statusline-creator

# Remove commands (optional)
rm ~/.claude/commands/spec.md
rm ~/.claude/commands/validate-spec.md
rm ~/.claude/commands/implement-spec.md
rm ~/.claude/commands/tests-from-spec.md
rm ~/.claude/commands/sync-spec.md
```

## Troubleshooting

### Skills Not Loading

**Problem:** Skills don't appear in `/skills list`

**Solutions:**
1. Restart Claude Code
2. Check installation directory: `ls ~/.claude/skills`
3. Verify SKILL.md exists in each skill directory
4. Check YAML frontmatter in SKILL.md

### Permission Denied Errors

**Problem:** Scripts can't execute

**Solution:**
```bash
# Make all scripts executable
find ~/.claude/skills -name "*.sh" -exec chmod +x {} \;
find ~/.claude/skills -name "*.py" -exec chmod +x {} \;
```

### Slash Commands Not Working

**Problem:** Slash commands don't trigger

**Solutions:**
1. Verify commands are in `~/.claude/commands/`
2. Check YAML frontmatter in command files
3. Restart Claude Code
4. Check for filename conflicts

### Plugin Installation Fails

**Problem:** `/plugin add` command fails

**Solutions:**
1. Check internet connection
2. Verify GitHub repository is accessible
3. Try manual installation instead
4. Check Claude Code version compatibility

### Skill Conflicts

**Problem:** Multiple versions of same skill

**Solution:**
```bash
# List all skills
ls -la ~/.claude/skills/

# Remove duplicates
rm -rf ~/.claude/skills/DUPLICATE_SKILL
```

### Python Dependencies Missing

**Problem:** Some scripts fail due to missing Python packages

**Solution:**
```bash
# Install required packages
pip install pyyaml

# Or use requirements file if provided
pip install -r requirements.txt
```

## Platform-Specific Notes

### Linux

Standard installation works as documented.

### macOS

```bash
# May need to allow scripts in Security & Privacy
# If scripts don't run, check:
xattr -d com.apple.quarantine ~/.claude/skills/*/scripts/*
```

### Windows (WSL)

```bash
# Use WSL for best compatibility
# Ensure line endings are LF, not CRLF
git config --global core.autocrlf input
```

## Verification Checklist

After installation, verify:

- [ ] Skills appear in `/skills list`
- [ ] Slash commands work (if installed)
- [ ] Scripts are executable
- [ ] No error messages in Claude Code
- [ ] Test a simple skill (e.g., statusline-creator)

## Getting Help

- **Issues:** https://github.com/astrosteveo/astrorepo/issues
- **Discussions:** https://github.com/astrosteveo/astrorepo/discussions
- **Documentation:** https://github.com/astrosteveo/astrorepo/docs

## Next Steps

- Read [Creating Skills](creating-skills.md) to develop your own
- Check [Contributing](contributing.md) to contribute
- Explore individual skill READMEs for usage details
