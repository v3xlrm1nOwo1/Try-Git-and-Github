# Try-Git 
![git-github](https://user-images.githubusercontent.com/87325345/199505243-848a53d1-b9dc-40e0-9dd9-a369b0d4ad59.jpg)

<!-- ![git](https://user-images.githubusercontent.com/87325345/199501061-20b6040e-4324-40c5-8ffa-a9c3f9e68baa.png)-->
---

## 1 - Check Git Installed

```zsh
git --version
```

---

## 2 - Git Config

When we start making changes to files, Git wants to know who's making those changes so they can keep track of them.
<br>

Git Config For Just Directory.
```sh
git config user.name YourName
```

```sh
git config user.email "Example@example.com"
```

Git Config For Any Directory For User

```zsh
git config --globle user.name YourName
```

```git
git config --globle user.email "Example@example.com"
```

### ⚠️ Note:

```
If Name or Email it contain Space, Enter Name and Email In " "
```

---

## 3 - Git Staging Environment:

Add all changes in the current directory to the staging environment.
```sh
git add .
```

Add all changes to the staging environment.
```sh
git add --all
```

Add all files ending in .py staging environment.
```sh
git add *.py

```
Add all files starting with main staging environment.
```sh
git add main.*
```

Adding chunk of the changes to staging environment.
```
git add -p
```

---


## 4 - Git Commit:

Add all changes to the staging environment and create a commitment.
```git
git commit -a -m "Commit Message"
```

Add all changes to the staging environment and create a commitment.
```git
git commit -am "Commit Message"
```

```git
git commit -m "Commit Message"
```

```git
git commit
```

---

## 5 - Git Help:

```sh
git help --all
```

```zsh
git command --help
```
