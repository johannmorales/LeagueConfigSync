import os
import shutil
import tarfile
import tempfile
import tkinter as tk

from dotenv import load_dotenv
from git import Repo


def config_import():
    load_dotenv()

    config_local_path = os.getenv('CONFIG_LOCAL_PATH')
    config_repository = os.getenv('CONFIG_REPOSITORY')

    if os.path.exists(config_local_path):
        shutil.rmtree(config_local_path)

    repository = tempfile.mkdtemp()
    tar = tempfile.mktemp()
    repo = Repo.clone_from(config_repository, repository)
    with open(os.path.join(tar), "wb") as fp:
        repo.archive(fp)
    tarfile.open(tar).extractall(config_local_path)


def config_persist():
    load_dotenv()

    config_local_path = os.getenv('CONFIG_LOCAL_PATH')
    config_repository = os.getenv('CONFIG_REPOSITORY')
    if os.path.exists(config_local_path):
        shutil.rmtree(config_local_path)

    repository = tempfile.mkdtemp()
    tar = tempfile.mktemp()
    repo = Repo.clone_from(config_repository, repository)
    with open(os.path.join(tar), "wb") as fp:
        repo.archive(fp)
    tarfile.open(tar).extractall(config_local_path)


window = tk.Tk()
window.geometry("400x300")
window.title("LeagueConfigSync")
window.resizable(False, False)
tk.Button(text="Import", width=20, pady=5, command=config_import).pack(pady=(100, 10))
tk.Button(text="Persist", width=20, pady=5).pack(pady=(0, 10))

window.columnconfigure(0, weight=1)

window.mainloop()
