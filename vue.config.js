/*
 * @Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @Date: 2023-03-28 21:20:26
 * @LastEditors: wesley 985189328@qq.com
 * @LastEditTime: 2023-04-08 12:28:39
 * @FilePath: \MTB-Equipment-Management-System\vue.config.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEtask
 */

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
    },
    'task': {
      // 入口文件，相当于单页面的 main.js
      entry: 'src/module/Task/index.js',
      // 模板文件
      template: 'src/module/Task/index.html',
      // 编译后 dist 目录下输出的文件，可以包含子目录
      filename: 'task.html'
    }
  },
  assetsDir: 'static'
})