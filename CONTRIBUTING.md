# Contributing (For New Members)

Welcome! This guide walks you through how to contribute code to this repo. No prior Git experience is assumed.

## 1. Install Git

- **Mac:** Open Terminal and run `xcode-select --install`
- **Windows:** Download from [git-scm.com](https://git-scm.com/downloads)
- **Linux:** `sudo apt install git`

## 2. Set Up Your GitHub Account

If you don't have one, create a free account at [github.com](https://github.com).

Configure Git with your name and email (use the email linked to your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 3. Fork the Repository

A "fork" is your own personal copy of the repo on GitHub. You make changes there first, then ask to merge them back into the main repo.

1. Go to [github.com/dchavan2192/UAS_BOLZ](https://github.com/dchavan2192/UAS_BOLZ)
2. Click the **Fork** button (top right corner of the page)
3. On the "Create a new fork" page, leave everything as default and click **Create fork**
4. You now have your own copy at `github.com/YOUR_USERNAME/UAS_BOLZ`

## 4. Clone Your Fork to Your Computer

This downloads your fork so you can edit files locally:

```bash
git clone https://github.com/YOUR_USERNAME/UAS_BOLZ.git
cd UAS_BOLZ
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## 5. Add the Upstream Remote

This connects your local copy to the original (main) repo so you can stay up to date:

```bash
git remote add upstream https://github.com/dchavan2192/UAS_BOLZ.git
```

Verify both remotes are set up:

```bash
git remote -v
# You should see:
# origin    https://github.com/YOUR_USERNAME/UAS_BOLZ.git (fetch)   <-- your fork
# origin    https://github.com/YOUR_USERNAME/UAS_BOLZ.git (push)
# upstream  https://github.com/dchavan2192/UAS_BOLZ.git (fetch)     <-- main repo
# upstream  https://github.com/dchavan2192/UAS_BOLZ.git (push)
```

## 6. Create a Branch for Your Work

**Never work directly on `master`.** Always create a new branch — think of it as a separate workspace for your changes:

```bash
git checkout -b your-branch-name
```

Use a descriptive name, for example: `fix-fusion-node-timeout`, `add-lidar-support`, `update-nav2-params`.

## 7. Make Your Changes

Edit files, add new scripts, fix bugs, etc. When you're done, check what changed:

```bash
git status          # shows which files you modified or added
git diff            # shows the actual line-by-line changes
```

## 8. Stage, Commit, and Push Your Changes

This is a three-step process: **stage** (pick which files to include) -> **commit** (save a snapshot with a message) -> **push** (upload to your fork on GitHub).

```bash
# Stage the files you changed
git add file1.py file2.py

# Commit with a clear message explaining WHAT you changed and WHY
git commit -m "Fix fusion node crash when IMU disconnects"

# Push your branch to your fork on GitHub
git push origin your-branch-name
```

**Commit message tips:**
- Good: `"Fix fusion node crash when IMU disconnects"`, `"Add goto_goal timeout parameter"`
- Bad: `"stuff"`, `"updates"`, `"fixed it"`

If you changed many files and want to stage them all:

```bash
git add -A                   # stages everything
git status                   # REVIEW what's staged before committing
git commit -m "Your message"
git push origin your-branch-name
```

## 9. Open a Pull Request (PR) to Merge Back to the Main Repo

A Pull Request says "hey, I made these changes in my fork — please review and merge them into the main repo."

1. Go to your fork on GitHub (`github.com/YOUR_USERNAME/UAS_BOLZ`)
2. You'll see a yellow banner saying **"Compare & pull request"** — click it
3. Make sure the base says `dchavan2192/UAS_BOLZ` `master` and the head says `YOUR_USERNAME/UAS_BOLZ` `your-branch-name`
4. Write a short description of what your changes do and why
5. Click **Create pull request**

Someone will review your code and either merge it or leave comments for changes.

## 10. Keeping Your Fork Up to Date

Other people will merge changes into the main repo. Before starting new work, always pull those changes into your fork:

```bash
# Switch back to master
git checkout master

# Pull the latest from the main repo
git pull upstream master

# Push it to your fork so it's also up to date
git push origin master

# Now create a new branch for your next task
git checkout -b my-next-feature
```

## Common Mistakes and How to Fix Them

| Mistake | Fix |
|---|---|
| Committed to `master` instead of a branch | `git checkout -b new-branch` (moves your commits to a new branch) |
| Forgot to pull before starting work | `git pull upstream master` then `git merge master` into your branch |
| Pushed the wrong file (e.g. `.DS_Store`) | Add it to `.gitignore`, then `git rm --cached .DS_Store` and commit |
| Commit message has a typo | `git commit --amend -m "New message"` (only if you haven't pushed yet) |
| Want to undo your last commit (not pushed) | `git reset --soft HEAD~1` (keeps your changes, undoes the commit) |

## Tips

- **Ask questions.** If something in the codebase is confusing, open a GitHub Issue or ask in the group chat.
- **Test before pushing.** If you changed a script, run it and make sure it works.
- **One feature per branch.** Don't mix unrelated changes in the same pull request.
- **Pull before you push.** Always sync with upstream before starting new work.
- **Read the platform README** for whichever platform you're working on — they document known issues, gotchas, and the reasoning behind design decisions.
