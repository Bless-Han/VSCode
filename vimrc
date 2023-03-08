sy on
set nu
" set for python
set tabstop=4
set shiftwidth=4
set expandtab
set relativenumber

" leader key -------------------
" space as leader key
let mapleader=" "
" leader+e to open NERDTree
nnoremap <leader>e :NERDTreeToggle<cr>
" leader+rr to resource ~/.config/nvim/init.vim
nnoremap <leader>rr :source ~/.config/nvim/init.vim<cr>
" leader + re to open ~/.config/nvim/init.vim
nnoremap <leader>re :e ~/.config/nvim/init.vim<cr>
" leader + i + i to open input file
nnoremap <leader>ii :e %:r.input<cr>
" leader + s to ":w
nnoremap <leader>s :w<cr>
" leader + c to :%y+ to copy all lines
nnoremap <leader>y :%y+<cr>
" leader + ce: Copilot enable
nnoremap <leader>ce :Copilot enable<cr>
" leader + cd: Copilot disable
nnoremap <leader>cd :Copilot disable<cr>

" ctrl key ----------------------

" ctrl+; to run python
nnoremap <C-;> :!time python "%" < "%:r.input"<cr>
" inoremap ctrl + ; to run python
inoremap <C-;> <Esc>:!time python "%" < "%:r.input"<cr>
" inoremap <C-p> Up
inoremap <C-p> <Up>
" inoremap <C-n> Down
inoremap <C-n> <Down>
" inoremap <C-b> Left
inoremap <C-b> <Left>
" inoremap <C-f> Right
inoremap <C-f> <Right>
" inoremap <C-a> Home
inoremap <C-a> <Home>
" inoremap <C-e> End
inoremap <C-e> <End>
" inoremap <C-enter> <C-o>o"
inoremap <C-enter> <C-o>o
" inoremap Ctrl + shift + enter to <C-o>O"
inoremap <C-S-enter> <C-o>O
" inoremap <C-d> <C-o>dl"
inoremap <C-d> <C-o>dl
" nnoremap and vnoremap ctrl + / to comment
nnoremap <C-/> :Commentary<cr>
vnoremap <C-/> :Commentary<cr>
" inoremap ctrl + / to comment
inoremap <C-/> <Esc>:Commentary<cr>

" 安装 Vundle 插件管理器 ---------------------
set rtp+=~/.config/nvim/bundle/Vundle.vim

call vundle#begin()

" 在此处添加插件列表
" NERDTree：以树形目录的形式展示文件，方便浏览文件夹中的文件。
Plugin 'scrooloose/nerdtree'
" vim-airline：状态栏插件，可以显示文件名、文件类型、Git 分支等信息。
Plugin 'vim-airline/vim-airline'
" vim-fugitive：Git 插件，可以在 Vim 中使用 Git 命令，比如查看 Git 日志、提交代码等。
Plugin 'tpope/vim-fugitive'
" vim-surround：快速添加、删除、修改括号、引号等符号。
Plugin 'tpope/vim-surround'
" auto-save：自动保存插件，可以在 Vim 中自动保存文件。
Plugin '907th/vim-auto-save'
" ALE (Asynchronous Lint Engine)：异步语法检查插件，可以在编辑器中实时检查代码的语法错误。
Plugin 'w0rp/ale'
" auto-pairs：自动补全括号、引号等符号。
Plugin 'jiangmiao/auto-pairs'
" vim-slime：在 Vim 中运行 Python 代码。
Plugin 'jpalardy/vim-slime'
" vim-tmux-navigator：在 Vim 和 Tmux 之间切换。
Plugin 'christoomey/vim-tmux-navigator'
" fzf.vim：模糊搜索插件，可以在 Vim 中搜索文件、搜索历史记录、搜索 Git 提交记录等。
Plugin 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plugin 'junegunn/fzf.vim'
" vim-easymotion：快速跳转插件，可以在 Vim 中快速跳转到指定行、指定单词等。
Plugin 'easymotion/vim-easymotion'
" nerdcommenter：快速注释代码，支持多种编程语言。
Plugin 'scrooloose/nerdcommenter'
" undotree：查看 Vim 的撤销树。
Plugin 'mbbill/undotree'



call vundle#end()
" 自动保存 
let g:auto_save = 1

" 一键运行 Python 代码
let g:slime_python_ipython = 1
let g:slime_target = "tmux"
let g:slime_default_config = {"socket_name": "default", "target_pane": ":.1"}

