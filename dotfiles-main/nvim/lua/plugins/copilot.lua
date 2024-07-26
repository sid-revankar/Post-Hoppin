return {
	"zbirenbaum/copilot.lua",
	cmd = "Copilot",
	event = "InsertEnter",
	config = function()
		require("copilot").setup({
			suggestion = {
				enabled = true,
				auto_trigger = true,
				debounce = 30,
				keymap = {
					accept = "<leader><Tab>",
					accept_word = false,
					accept_line = false,
					next = "<leader><Tab><Left>",
					prev = "<leader><Tab><Right>",
					dismiss = "<C-]>",
				},
			},
		})
	end,
}
