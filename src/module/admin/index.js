import {createApp } from 'vue'
import App from './index.vue'
// import Head from './head.vue'

import TDesign from 'tdesign-vue-next'

//import ElementPlus from 'element-plus'
// 引入组件库全局样式资源
import 'tdesign-vue-next/es/style/index.css';

const app = createApp(App)
app.use(TDesign).mount('#main')
