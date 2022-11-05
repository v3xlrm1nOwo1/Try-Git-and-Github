# Try-Git <img src="https://user-images.githubusercontent.com/87325345/199744230-199900b7-12ee-4c1a-9f3b-f91c84a34d82.gif" width="70px" height="70" />

![git-github](https://user-images.githubusercontent.com/87325345/199505243-848a53d1-b9dc-40e0-9dd9-a369b0d4ad59.jpg)

<!-- ![git](https://user-images.githubusercontent.com/87325345/199501061-20b6040e-4324-40c5-8ffa-a9c3f9e68baa.png)-->
---

## 0 - Introduction To Git:

### What is Git:
🏮 Git is a distributed version control system to manage source code history.

### What is Version Control System:
🏮 The control system is It is a method that we as programmers use to keep track, save and record changes in our code. Basically we save an initial version of the code and when we make changes and update the code we can save it again and over and over and over and over every time we make changes to the code we can  Save it again.

### What is Repository:
🏮 The repository is the project directory, a container for the project you want to track using git.

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


---

## 7 - Show Branch:

🏮️ When you start the Git with the branch, you want to show In which branch are you.

<br>
<br>

🎯️ can see the current branch, but the * beside branch-name specifies that we are currently on that branch.
```zsh
git branch
```


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

```
- You must make sure that you are in the branch you want to merge in.
- HEAD is meaned the current branch.
```


### ⚠️ Note:
```
- In Git workflow, there are two long-lived branches: master or main and Develop branchs, and the branches remain 
  short-lived, such as features and bugs brancha. Any branch is merged into the Develop branch, then after making sure 
  that it is working well, it is merged into the master or main branch.

- You can use merge to update your local branch when there are updates in the (master, main) branch in the remote repository , 
  you bring the talk in the remote repository to the (master, main) branch in your repository using pull or fetch , then merge your 
  (master, main) into the branch you are working on.
```


---

# 11 - Git Clone:

🏮️ Git clone is used to copy or clone a different repository in your local machine.


```zsh
git clone <url>
```

```zsh
git clone https://github.com/BlackHeart-Dev/try-git.git
```

---


# 12 - Git Remote:

🏮️ Git remote is used to refer to a remote repository or your central repository, e.g: When you want to add a remote repository as your origin.

```zsh
git remote add <alias> <url>
```

```zsh
git remote add origin https://github.com/BlackHeart-Dev/try-git.git 
```

### 🎯️ Git Clone VS Git Remote:
```
- Git clone is used to copy or clone a different repository in your local machine.

- Git remote is used to refer to a remote repository or your central repository, 
  e.g: When you want to add a remote repository as your origin.
  
- Git clone creates a new git repository by copying an existing one located at the URI you specify.
  
- Git remote add just creates an entry in your git config that specifies a name for a particular URL. 
  You must have an existing git repo to use this.
  
- Git clone Will physically download the files into your computer. It will take space from your computer. 
  If the repo is 200Mb, then it will download that all and place it in the directory you cloned.
  
- Won't take space! It's more like a pointer! It doesn't increase your disk consumption. 
  It just gets a snapshot of what branches are available and their git commit history I believe. 
  It doesn't contain the actual file/folders of your project.
 
*from Stackoverflow.
```

### ⚠️ Note:
```
- origin is alias for remote repository, It is used to refer to the remote repository instead of 
  using the url every time you want to pull or push or fetch.
```

---

## 13 - Git Pull:

🏮️ <a href="https://www.atlassian.com/git/tutorials/syncing/git-pull">The git pull</a> command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows. The git pull command is actually a combination of two other commands, git fetch followed by git merge. In the first stage of operation git pull will execute a git fetch scoped to the local branch that HEAD is pointed at. Once the content is downloaded, git pull will enter a merge workflow. A new merge commit will be-created and HEAD updated to point at the new commit.

<br>

```zsh
git pull --set-upstream <remote> <branch>
```
or

```zsh
git pull -u <remote> <branch>
```

<br>

```zsh
git pull --set-upstream origin xz-y-10.2
```
or

```zsh
git pull -u origin xz-y-10.2
```


---

## 14 - Git Fetch:

🏮️ <a href="https://www.atlassian.com/git/tutorials/syncing/git-fetch">The git fetch</a> command downloads commits, files, and refs from a remote repository into your local repo. Fetching is what you do when you want to see what everybody else has been working on. It’s similar to svn update in that it lets you see how the central history has progressed, but it doesn’t force you to actually merge the changes into your repository. Git isolates fetched content from existing local content; it has absolutely no effect on your local development work. Fetched content has to be explicitly checked out using the git checkout command. This makes fetching a safe way to review commits before integrating them with your local repository.

<br>

```zsh
git fetch <remote-repo> 
```

```zsh
git fetch https://github.com/BlackHeart-Dev/try-git.git 
```

or

```zsh
git fetch origin
```

<h3> 🎯️ <a href="https://www.git-tower.com/learn/git/faq/difference-between-git-fetch-git-pull"> Git Clone VS Git Remote</a>:</h3>

```
- Git fetch really only downloads new data from a remote repository - but it doesn't integrate any of this new data into your working files. 
  Fetch is great for getting a fresh view on all the things that happened in a remote repository. Due to it's "harmless" nature, 
  you can rest assured: fetch will never manipulate, destroy, or screw up anything. This means you can never fetch often enough.
  
- Git pull, in contrast, is used with a different goal in mind: to update your current HEAD branch with the latest changes from the remote server. 
  This means that pull not only downloads new data; it also directly integrates it into your current working copy files. 
  This has a couple of consequences:
  > Since "git pull" tries to merge remote changes with your local ones, a so-called "merge conflict" can occur. 

  > Like for many other actions, it's highly recommended to start a "git pull" only with a clean working copy. 
    This means that you should not have any uncommitted local changes before you pull. 
    Use Git's Stash feature to save your local changes temporarily.
```



---

## 15 - Git Push:

🏮️ <a href="https://www.atlassian.com/git/tutorials/syncing/git-push">The git push</a> command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo. It's the counterpart to git fetch, but whereas fetching imports commits to local branches, pushing exports commits to remote branches. Remote branches are configured using the git remote command. Pushing has the potential to overwrite changes, caution should be taken when pushing.

```zsh
git push <url>
```

```zsh
git push https://github.com/BlackHeart-Dev/try-git.git
```

or

```zsh
git push origin
```

---

## 16 - workflow:

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

## 17 - Git Vs Github:

<h1 align="center">Git VS Github</h1>

<table align="center">
   <thead>
      <tr>
         <th>Github</th>
         <th>Git</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td align="center">Github is a sevice</td>
         <td align="center">Git is a software</td>
      </tr>
      <tr>
         <td align="center">Github is a graphical user interface</td>
         <td align="center">Git is a command-line tool</td>
      </tr>
      <tr>
         <td align="center">Github is a hosted on the web for git</td>
         <td align="center">Git is installed locally on your local machine</td>
      </tr>
      <tr>
         <td align="center">Github is maintained by Microsoft</td>
         <td align="center">Git is maintained by Linux</td>
      </tr>
      <tr>
         <td align="center">Github is focused on the centralized code hosting</td>
         <td align="center">Git is focused on version control and code sharing</td>
      </tr>
      <tr>
         <td align="center">Github is a hosting service for git repositories</td>
         <td align="center">Git is a distributed version control system to manage source code history</td>
      </tr>
   </tbody>
</table>

```
- By DataScienceDojo.
```

---
<h1 align="center">⚠️ Don't forget to add a star ⭐️</h1>
