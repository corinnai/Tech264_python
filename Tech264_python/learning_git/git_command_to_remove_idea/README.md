## Danger: If Sensitive Data is Accessible in a Previous Commit

**Problem**: Sensitive data can still be accessed from previous commits, even if removed in the latest commit.

### Solutions:

1. **Remove Previous Commits** (Risky):
   - Use `git reset` to remove the commits containing sensitive data. ⚠️ Be careful, this could result in losing work.
   
2. **Alternative Approach**:
   1. Delete the GitHub repository (makes the data safe).
   2. Remove the sensitive file from your local directory.
   3. Delete the `.git` folder from your local repository to remove all history.

---

## How to Remove Files You Don't Want to Commit

- **Folders starting with a dot** (`.`) are automatically ignored (e.g., `.git`).
- **.gitignore File**:
  - Use it to prevent files or folders from being committed.
  - Useful for ignoring:
    - Sensitive data like personal files, credentials, passwords.
    - Large files or unnecessary folders.
    - System files or IDE settings (e.g., `.idea`, `bin`, `out`).
  - **Note**: Files already committed will still appear in history.

---

## How to Remove Committed Files from Git History

1. Add files to `.gitignore` to prevent future commits.
2. Use the command:
   ```bash
   git rm --cached -r .idea