import git
import time
timeData = time.localtime()
fileName = f"{timeData.tm_year}-{timeData.tm_mon}-{timeData.tm_mday}-{timeData.tm_hour}-{timeData.tm_min}-{timeData.tm_sec}"

with open(f"./PythonTools/{fileName}.py", 'a')as f:
    f.write("import time")


repo = git.Repo(path='.')
repo.git.add('.')
if repo.is_dirty():
    repo.git.commit(m=f'{fileName} 更新')
remote = repo.remote()


remote.push()
