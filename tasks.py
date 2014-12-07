from invoke import task
import subprocess
import os


def git(git_cwd="~/", *args):
    return subprocess.check_call(['git'] + list(args), cwd=git_cwd)


def get_home():
    return os.path.expanduser("~")


def create_sym_link():
    link = get_home() + "/.vimrc"
    if not os.path.isfile(link):
        os.symlink(get_home() + "/.vim/vimrc", link)


def init_submodules():
    link = get_home() + "/.vim/"
    git(link, "submodule", "init")
    git(link, "submodule", "update", "--recursive")


@task
def build():
    print "Creating sym link"
    create_sym_link()
    print "Init submodules "
    init_submodules()
    pass
