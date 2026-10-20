
# Git Audit Note

## 1. Git Diff Audit

I ran `git diff main...HEAD --stat` to review the committed changes on my branch.

The output showed:
- 1 file changed: `README.md`
- 1 insertion (+)
- 1 deletion (-)

I confirmed that the committed changes were limited to the README documentation. No code or data files were modified in the reviewed diff.

## 2. .gitignore Audit

I reviewed the `.gitignore` file using the command `cat .gitignore`.

The file includes the following ignore patterns:

- `/.quarto/` and `**/.quarto/`: Ignore Quarto-generated working directories.
- `*_files/`: Ignore auxiliary files generated during rendering.
- `.DS_Store` and `Thumbs.db`: Ignore operating system files.
- `.env` and `.env.*`: Ignore local environment files that may contain sensitive information.

The `.gitignore` file also states that required HTML/PDF submissions are intentionally not ignored.

After reviewing the existing rules, I determined that no changes to `.gitignore` were necessary for this assignment.

## 3. AI Use Disclosure

I used ChatGPT to help me understand the Assignment 3 submission requirements and navigate the Git and GitHub workflow.

AI assistance was used to:
- Explain how to review commits and pull requests on GitHub.
- Guide me through Git commands such as `git status`, `git diff main...HEAD --stat`, and `cat .gitignore`.
- Help draft and organize the Markdown submission documentation.
- Interpret the Git diff and `.gitignore` output.

I personally executed the Git commands, reviewed the outputs, and verified the information included in my submission.

## 4. M0 Group Repository Readiness

Our group consists of three members, and we have already created a shared GitHub repository for our group project.

However, one group member has not responded to our messages, so we have not been able to add them to the group repository yet.

**Current Status:**
- **Group membership:** Three members have been assigned to our group.
- **GitHub repository:** The group repository has been created.
- **Repository access:** Access for one member is still pending due to a lack of response.
- **Codespaces access:** Not yet confirmed for all group members.
- **Communication:** We have attempted to contact the third member but have not received a response.

**Next Steps:**

We will continue trying to contact the unresponsive member and help them gain access to the repository once they respond. If we are unable to reach them, we may need to inform the course instructor or TA for further guidance.

Overall, our group repository has been established, but full group participation and access still need to be confirmed before M0.