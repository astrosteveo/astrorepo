# AstroRepo Setup Guide

Your AstroRepo marketplace is ready! Follow these steps to push it to GitHub and start using it.

## 📦 What's Been Created

### Repository Structure
```
astrorepo/
├── 6 Skills Ready
│   ├── spec-writer
│   ├── spec-validator
│   ├── implement-from-spec
│   ├── test-from-spec
│   ├── spec-sync
│   └── statusline-creator
├── Professional Tooling
│   ├── init_skill.py
│   ├── package_skill.py
│   └── quick_validate.py
├── Complete Documentation
│   ├── README.md
│   ├── CONTRIBUTING.md
│   ├── CHANGELOG.md
│   └── docs/installation.md
├── GitHub Actions CI/CD
│   ├── validate-skills.yml
│   └── package-release.yml
└── Integration Examples
    ├── Slash commands
    ├── Hooks
    └── Subagents
```

### Current Status
- ✅ Git repository initialized
- ✅ Initial commit created
- ✅ All skills migrated
- ✅ Documentation complete
- ✅ CI/CD configured
- ⏳ Ready to push to GitHub

## 🚀 Push to GitHub

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: **`astrorepo`**
3. Description: **"AstroSteveo's curated collection of powerful Claude Code skills"**
4. Visibility: **Public** (recommended for marketplace)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **"Create repository"**

### Step 2: Push Your Code

```bash
cd /home/astrosteveo/workspace/astrorepo

# Add GitHub remote
git remote add origin git@github.com:astrosteveo/astrorepo.git

# Push to GitHub
git push -u origin main
```

### Step 3: Verify on GitHub

Visit https://github.com/astrosteveo/astrorepo and verify:
- [ ] README displays correctly
- [ ] All files are present
- [ ] GitHub Actions are enabled
- [ ] License shows as MIT

## 🎯 Using Your Marketplace

### Install in Claude Code

Once pushed to GitHub:

```bash
/plugin add marketplace https://github.com/astrosteveo/astrorepo
```

### Verify Installation

```bash
/plugin list
# Should show: astrorepo

/skills list
# Should show all 6 skills
```

### Test a Skill

```bash
/statusline
# Should trigger statusline-creator skill
```

## 📦 Creating Your First Release

### Option 1: Via GitHub UI

1. Go to https://github.com/astrosteveo/astrorepo/releases
2. Click **"Create a new release"**
3. Click **"Choose a tag"** → Type: `v1.0.0` → Click **"Create new tag"**
4. Release title: **`v1.0.0 - Initial Release`**
5. Description: Copy from CHANGELOG.md
6. Click **"Publish release"**

GitHub Actions will automatically package all skills and attach them to the release!

### Option 2: Via Command Line

```bash
# Create and push tag
git tag -a v1.0.0 -m "Release v1.0.0 - Initial release with 6 skills"
git push origin v1.0.0

# GitHub Actions automatically creates release
```

### What Happens

The `package-release.yml` workflow will:
1. ✅ Validate all skills
2. ✅ Package each skill as .zip
3. ✅ Generate checksums
4. ✅ Create GitHub release
5. ✅ Attach all skill packages

## 🔄 Workflow Examples

### Add a New Skill

```bash
cd /home/astrosteveo/workspace/astrorepo

# Initialize new skill
python tools/init_skill.py my-new-skill --path skills/

# Develop the skill
# Edit skills/my-new-skill/SKILL.md

# Validate
python tools/quick_validate.py skills/my-new-skill/

# Test locally
cp -r skills/my-new-skill ~/.claude/skills/

# Commit and push
git add skills/my-new-skill
git commit -m "feat(skills): Add my-new-skill for awesome functionality"
git push origin main
```

### Update Existing Skill

```bash
# Make changes
vim skills/statusline-creator/SKILL.md

# Validate
python tools/quick_validate.py skills/statusline-creator/

# Test
cp -r skills/statusline-creator ~/.claude/skills/

# Commit and push
git add skills/statusline-creator
git commit -m "fix(statusline-creator): Improve ANSI code handling"
git push origin main
```

### Create New Release

```bash
# Update version in plugin.json
vim plugin.json
# Change "version": "1.0.0" to "1.1.0"

# Update CHANGELOG.md
vim CHANGELOG.md
# Add new version section

# Commit changes
git add plugin.json CHANGELOG.md
git commit -m "chore: Bump version to 1.1.0"
git push origin main

# Create and push tag
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0

# GitHub Actions handles the rest!
```

## 🛠️ Local Testing

Before pushing changes, always test locally:

### Test Individual Skill

```bash
# Validate
python tools/quick_validate.py skills/SKILL_NAME/

# Install locally
cp -r skills/SKILL_NAME ~/.claude/skills/

# Test in Claude Code
# Use the skill and verify it works
```

### Test All Skills

```bash
# Validate all
for skill in skills/*/; do
  echo "Validating $(basename $skill)..."
  python tools/quick_validate.py "$skill"
done

# Install all locally
for skill in skills/*/; do
  cp -r "$skill" ~/.claude/skills/
done
```

## 📊 Monitoring

### GitHub Actions

After pushing, check:
- https://github.com/astrosteveo/astrorepo/actions

You should see workflows running for:
- ✅ Skill validation (on every push/PR)
- ✅ Release packaging (on tags)

### Issues and Discussions

Enable:
- **Issues** - For bug reports and feature requests
- **Discussions** - For questions and community

Settings → Features → Enable Issues & Discussions

## 🎨 Customization

### Update README

```bash
vim README.md
# Add your personal touches
# Update screenshots if you add them
# Add badges
```

### Add More Documentation

```bash
# Create more docs
touch docs/creating-skills.md
touch docs/troubleshooting.md

# Edit and commit
git add docs/
git commit -m "docs: Add more documentation"
git push
```

## 🌟 Promotion

Share your marketplace:

### README Badges

Add to README.md:

```markdown
[![GitHub Stars](https://img.shields.io/github/stars/astrosteveo/astrorepo?style=social)](https://github.com/astrosteveo/astrorepo)
[![GitHub Forks](https://img.shields.io/github/forks/astrosteveo/astrorepo?style=social)](https://github.com/astrosteveo/astrorepo)
```

### Social Media

- Share on Twitter/X
- Post in Claude community
- Share on Reddit (r/ClaudeAI)
- LinkedIn post

### Documentation Site (Optional)

Create GitHub Pages:

```bash
# Enable in Settings → Pages
# Source: Deploy from a branch
# Branch: main
# Folder: /docs
```

## 🔐 Security

### Enable Security Features

1. **Dependabot** - Settings → Code security → Enable Dependabot
2. **Secret Scanning** - Settings → Code security → Enable
3. **Code Scanning** - Settings → Code security → Set up CodeQL

### Protected Branches

Settings → Branches → Add rule:
- Branch name: `main`
- ✅ Require pull request reviews
- ✅ Require status checks to pass
- ✅ Require conversation resolution

## 📈 Next Steps

1. **Push to GitHub** (Step 2 above)
2. **Create v1.0.0 release**
3. **Install in Claude Code** and test
4. **Share with community**
5. **Start planning v2.0** features!

## 💡 Tips

- **Frequent commits** - Commit early and often
- **Descriptive messages** - Follow commit guidelines
- **Test thoroughly** - Before every release
- **Update docs** - Keep documentation current
- **Engage community** - Respond to issues/PRs
- **Regular releases** - Keep marketplace fresh

## ❓ Troubleshooting

### Push Fails (Permission Denied)

```bash
# Use HTTPS instead
git remote set-url origin https://github.com/astrosteveo/astrorepo.git

# Or set up SSH keys
# See: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
```

### GitHub Actions Fail

- Check workflow logs in Actions tab
- Verify Python version compatibility
- Check file paths are correct
- Ensure all required files exist

### Skills Not Loading After Install

```bash
# Restart Claude Code
# Verify installation
ls -la ~/.claude/plugins/marketplaces/astrorepo/

# Reinstall if needed
/plugin remove astrorepo
/plugin add marketplace https://github.com/astrosteveo/astrorepo
```

## 🎉 You're Ready!

Your AstroRepo marketplace is fully set up and ready to share with the world!

**What you have:**
- ✅ 6 production-ready skills
- ✅ Professional tooling
- ✅ Complete documentation
- ✅ Automated CI/CD
- ✅ Community guidelines
- ✅ Git repository ready to push

**Next:** Push to GitHub and create your first release!

---

**Questions?** Open an issue or start a discussion on GitHub.

**Made with ❤️ by AstroSteveo**
