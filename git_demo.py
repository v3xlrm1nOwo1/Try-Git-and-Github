'''
- By: v3xlrm1nOwo1(黒い心臓).
- Demo git.
'''
class v3xlrm1nOwo1:
    def __init__(self, url):
        self.url = url

    def clone(self):
        return f'git clone {self.url}'
    
    def add(self, file_name):
        return f'git add {file_name}'

    def commit(self, message):
        return f'git commit -m {message}'
    
    def push(self):
        return f'git push --set-upstream origin main'

