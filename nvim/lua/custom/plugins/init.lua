return {
  -- {
  --   'akinsho/bufferline.nvim',
  --   version = '*',
  --   dependencies = 'nvim-tree/nvim-web-devicons',
  --   config = function()
  --     vim.opt.termguicolors = true
  --     require('bufferline').setup {}
  --     Options = {
  --       mode = 'buffers',
  --       offsets = {
  --         filetype = 'neo-tree',
  --         text = 'File Explorer',
  --         highlight = 'Directory',
  --         separator = true,
  --       },
  --     }
  --   end,
  -- },
  {
    'stevearc/oil.nvim',
    opts = {},
    -- Optional dependencies
    dependencies = { 'nvim-tree/nvim-web-devicons' },
    config = function()
      require('oil').setup {}
      vim.keymap.set('n', '-', '<CMD>Oil<CR>', { desc = 'Open parent directory' })
    end,
  },
  {
    'christoomey/vim-tmux-navigator',
    lazy = false,
  },
}
