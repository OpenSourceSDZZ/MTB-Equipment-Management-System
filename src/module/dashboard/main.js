import { createApp } from 'vue';
import TDesign from 'tdesign-vue-next';
import App from './dashboard.vue';
// 引入组件库全局样式资源
import 'tdesign-vue-next/es/style/index.css';


const app = createApp(App);
app.use(TDesign).mount('#app')