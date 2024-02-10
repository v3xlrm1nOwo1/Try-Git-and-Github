from include import v3xlrm1nOwo1

url = 'https://github.com/v3xlrm1nOwo1/Try-Git-and-Github.git'

git = v3xlrm1nOwo1(url=url)

clone = git.clone()
print(clone)

add = git.add(file_name='main.py')
print(add)

commit = git.commit(message='init commit uwu')
print(commit)

push = git.push()
print(push)

