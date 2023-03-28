
const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  // devServer: {
  //   allowedHosts: [
  //     'ran7.gnway.cc',
  //   ],
  // },
  lintOnSave: false,
  transpileDependencies: true,
  pages: {
    'admin': {
      // 入口文件，相当于单页面的 main.js
      entry: 'src/module/admin/index.js',
      // 模板文件
      template: 'src/module/admin/index.html',
      // 编译后 dist 目录下输出的文件，可以包含子目录
      filename: 'panel.html'
    }
  },
  assetsDir: 'static'
})