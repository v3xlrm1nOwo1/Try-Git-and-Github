# Try-Git <img src="https://user-images.githubusercontent.com/87325345/199744230-199900b7-12ee-4c1a-9f3b-f91c84a34d82.gif" width="70px" height="70" />

![git-github](https://user-images.githubusercontent.com/87325345/199505243-848a53d1-b9dc-40e0-9dd9-a369b0d4ad59.jpg)

<!-- ![git](https://user-images.githubusercontent.com/87325345/199501061-20b6040e-4324-40c5-8ffa-a9c3f9e68baa.png)-->
---

## 1 - Check Git Installed:

```zsh
git --version
```

---

## 2 - Git Config:

🏮️ When we start making changes to files, Git wants to know who's making those changes so they can keep track of them.
<br>
<br>

🎯️ Git Config For Just Directory.
```zsh
git config user.name YourName
```

```zsh
git config user.email "Example@example.com"
```

<br>

🎯️ Git Config For Any Directory For User

```zsh
git config --globle user.name YourName
```
```zsh
git config --globle user.email "Example@example.com"
```

### ⚠️ Note:

```
If Name or Email it contain Space, Enter Name and Email In " "
```

---

## 3 - Git Staging Environment:
🏮️ The Git Staging Environment can be thought of as an additional safety cover, as it can be used to create a very good commit, and make a comparison with the last commit.

<br>
<br>

🎯️ Add all changes in the current directory to the staging environment.
```zsh
git add .
```

<br>

🎯️ Add all changes to the staging environment.
```zsh
git add --all
```

<br>

🎯️ Add all files ending in .py staging environment.
```zsh
git add *.py
```

<br>

🎯️ Add all files starting with main staging environment.
```zsh
git add main.*
```

<br>

🎯️ Adding chunk of the changes to staging environment.
```zsh
git add -p
```

---


## 4 - Git Commit:

🏮️ Git Commit can be thought of as a save point, a point you can refer to if something goes wrong in the future or if you want to know how the code was at a particular point in time.

<br>
<br>

🎯️ Add all changes to the staging environment and create a commitment.
```zsh
git commit -a -m "Commit Message"
```

<br>

🎯️ Add all changes to the staging environment and create a commitment.
```zsh
git commit -am "Commit Message"
```

<br>

🎯️ Create a commitment for changes that have been added to the staging environment.
```zsh
git commit -m "Commit Message"
```

<br>

🎯️ Create a commitment for changes that have been added to the staging environment on nano or vim.
```zsh
git commit
```


### ⚠️ Note:

```
The commitment message should be a well descriptive message and the message length should not exceed 80 characters.
```
---

## 5 - Git Help:

🏮️ If you are having trouble remembering commands or command options, you can use Git help.

<br>
<br>

🎯️ See all possible commands in git.
```zsh
git help --all
```

<br>

🎯️ See all the available options for the specific command.
```zsh
git command --help
```

---

## 6 - Git Create Branch:

🏮️ When we start in git there is a branch that is created with the initialization of the repository called branch master where it is the production branch, and can create new brach and a branch is a copy of the repository at a certain point in time with different changes than the main branch.

<br>
<br>

🎯️ Create branch from current branch
```zsh
git branch branch-name
```

<br>

🎯️ Create branch from a previous commit.
```zsh
git branch branch_name commit-hash or HEAD~3
```

<br>

🎯️ Create branch from current branch using checkout.
```zsh
git checkout -b branch-name
```

<br>

🎯️ Create branch from a previous commit using checkout.
```zsh
git checkout -b branch_name commit-hash or HEAD~3
```

### ⚠️ Note:

```
'HEAD~number' this meaned the commit after current commit, like HEAD~4 this meaned the 3 commits after current commit.
```
<br>


---

## 7 - Show Branch:

🏮️ When you start the Git with the branch, you want to show In which branch are you.

<br>
<br>

🎯️ can see the current branch, but the * beside branch-name specifies that we are currently on that branch.
```zsh
git branch
```

<br>

---

## 8 - Change Branch Name:
🏮️ Sometimes you may want to change the name of the branch to a good name for different reasons.

<br>
<br>

🎯️ Change current branch name.
```zsh
git branch -M new-name
```

<br>

🎯️ Change different branch from current branch.
```zsh
git branch -M old-name new-name
```
<br>

---

## 9 - Swith From Current Branch To Other Branch:
🏮️ When you start the Git with the branch, you want to switch from one branch to another branch.

<br>
<br>

🎯️ Switch from current branch using checkout.
```zsh
git checkout branch_name
```
<br>

🎯️ Switch from current branch using switch.
```zsh
git switch branch_name
```
<br>

---

## 10 - Git Branch Merge And Merge Conflict:
🏮️ When you have finished working on a branch, you want to merge the changes into the master branch.
<br>
🎯️ Merge a branch into the current branch:

```zsh
git merge "The name of the branch to be merged"
```
<br>

🎯️ Merge Conflict:
Merge conflicts occur when competing changes are made to the same line of a file, or when one person edits a file and another person deletes the same file.

```zsh
$ git merge <branch-name>
Auto-merging <file-name>
CONFLICT (content): Merge conflict in <file-name>
Automatic merge failed; fix conflicts and then commit the result.
```

🎯️ So we need to fix that conflict. Open the file in our editor:

```zsh
<Some Text>
<<<<<<< HEAD
Changes in the current branch.
=======
Changes from the branch to be merged.
>>>>>>> <The name of the branch to be merged>
<Some Text>
```

### In Git workflow, there are two long-lived branches: master or main branch and Develop branch, and the branches remain short-lived, such as features and bugs branch. Any branch is merged into the Develop branch, then after making sure that it is working well, it is merged into the master or main branch Note:

```
- You must make sure that you are in the branch you want to merge in.
- HEAD is meaned the current branch.
```
<br>
<br>

---

pull


<br>
<br>

---

push


<br>
<br>

---

fetch


<br>
<br>

---

clone


<br>
<br>

---

## 11- workflow:
🏮️ Branches in Git are one of the best things about Git and perhaps one of the best features of Git, but what Git does is that it provides the tool but does not tell you how to use it. It leaves you and your team the freedom to use the tool, but as for branches, there are two strategies that are used frequently and Each new strategy is based on them, Git workflow and Github workflow.

<br>

### 🎯️ Git workflow:

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In Git workflow, there are two long-lived branches: master or main branch and Develop branch, and the branches remain short-lived, such as features and bugs branch. Any branch is merged into the Develop branch, then after making sure that it is working well, it is merged into the master or main branch.

![Git workflow](https://user-images.githubusercontent.com/87325345/199704078-58463d7d-840b-430a-87d3-6974402e2ab4.png)


<br>

### 🎯️ Github workflow:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In the Github workflow there are short-lived branches such as features and bugs branch and then after making sure that the branch is working fine, it is merged into the master or main branch.

![github-flow](https://user-images.githubusercontent.com/87325345/199710558-1f40b0a2-0a17-4b87-ae3a-feb654ed8904.png)


---
# ⚠️ Don't forget to add a star ⭐️
