# Git audit note

## Diff summary

In the readMe file that introduces my workspace, I added "This is **Sky Ng (skyngubc)** ".

To confirm that there was only a documentation only update, I went to the git commit area of VSCode and clicked and viewed the changes that I made. 



## .gitignore check

I checked [.gitignore](../../.gitignore) to ensure generated or temporary files are not being tracked unintentionally. The repository already contains safe patterns for generated or local-only files such as `.DS_Store`, `.Rhistory`, `.RData`, `.env`, and `.quarto/`.

If a generated file were being tracked, the safe fix would be to add a specific ignore rule such as:

```gitignore
# generated output
*.log
.quarto/
.DS_Store
```

Then, if the file had already been staged, I would remove it from Git tracking with:

```bash
git rm --cached path/to/file
```

This keeps source files and required project artifacts visible while preventing machine-generated files from polluting the repository history.

## AI-use sentence

I used AI to help summarize the diff and draft the wording for this note; I re-read the diff myself and confirmed that the summary matches the actual change.

## M0 readiness note

Our group has currently started working on M0. Contact information has been exchanged, and tasks have been allocated. I am responsible for the communications plan, and I have also started writing the AI use note. I have already created the relevant branches and sent out a commit waiting to be reviewed. 

As of right now, all members have joined and gained access to the repo. We will communicate through instagram. And around 1-2 of our members have confirmed that they can use codespaces. 