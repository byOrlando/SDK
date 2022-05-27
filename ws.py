import git
import time
from getStr import getStr

timeData = time.localtime()
commit_name = f"{timeData.tm_year}-{timeData.tm_mon}-{timeData.tm_mday}-{timeData.tm_hour}-{timeData.tm_min}" \
        f"-{timeData.tm_sec}"

dataStr, filename = getStr()

with open(f"./PythonTools/{filename}.md", 'a') as f:
    f.write(dataStr)

repo = git.Repo(path='.')
repo.git.add('.')
if repo.is_dirty():
    repo.git.commit(m=f'{commit_name} 更新')

remote = repo.remote()

remote.push()
