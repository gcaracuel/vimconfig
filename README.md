# Python Vim Config

## Installation:

    cp -fr ~./vim ~/.vim.backup
    rm -fr ~./vim
    git clone git://github.com/camilocot/vimconfig.git ~/.vim

### Invoke install 

    sudo pip install invoke
    cd ~/.vim
    invoke build

### Manual install 
Create symlinks:

    ln -s ~/.vim/vimrc ~/.vimrc

Switch to the `~/.vim` directory, and fetch submodules:

    cd ~/.vim
    git submodule init
    git submodule update --recursive

