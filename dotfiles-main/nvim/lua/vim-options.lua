vim.cmd("set expandtab")
vim.cmd("set tabstop=4")
vim.cmd("set softtabstop=4")
vim.cmd("set shiftwidth=4")
vim.cmd("set number relativenumber")
vim.cmd("set wrap linebreak textwidth=80")

vim.g.mapleader = " "

vim.opt.termguicolors = true

vim.keymap.set("n", "<S-l>", ":bnext<CR>", {})
vim.keymap.set("n", "<S-h>", ":bprevious<CR>", {})
vim.keymap.set("n", "<A-j>", "<Esc>:m .+1<CR>==", {})
vim.keymap.set("n", "<A-k>", "<Esc>:m .-2<CR>==", {})
vim.keymap.set("n", "<leader>x", "<cmd> bp|sp|bn|bd! <CR>", {})
vim.keymap.set("n", "<C-s>", "<Esc>:w<CR>", {})
vim.keymap.set("n", "<C-S-s>", "<Esc>:wa<CR>", {})
