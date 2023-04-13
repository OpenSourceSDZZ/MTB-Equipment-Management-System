<template>
    <!---->
    <div id="app">
        <a href="./panel.html" target="_blank">
            <div id="back_to_panel_big" class="back_to_panel_box_big" style="top: 30px;left: 35px;position: absolute;">
                <div class="back_to_panel_box_text"><t-icon name="arrow-left" size="20px"></t-icon><span>返回设备管理系统</span>
                </div>
            </div>
        </a>
        <div>
            <div class="main_box_big">
                <div class="main_box_tabs_big">
                    <div class="main_box_tabs_view">
                        <div class="main_box_tabs_view_tab" name="label" :class="{ tabs_active: TabsActive == 'label' }"
                            @click="handleTabsClick($event.target.__vnode.props.name, 1)">按标签排行</div>
                        <div class="main_box_tabs_view_tab" name="weight" :class="{ tabs_active: TabsActive == 'weight' }"
                            @click="handleTabsClick($event.target.__vnode.props.name, 2)">按权重排行</div>
                        <div class="main_box_tabs_view_tab" name="add" :class="{ tabs_active: TabsActive == 'add' }"
                            @click="handleTabsClick($event.target.__vnode.props.name, 2)">任务管理</div>
                        <div class="main_box_tabs_view_tab" name="admin" :class="{ tabs_active: TabsActive == 'admin' }"
                            @click="handleTabsClick($event.target.__vnode.props.name, 3)">设备管理系统</div>
                    </div>
                </div>
                <div class="main_box_content_big">
                    <div class="main_box_content_view" v-if="TabsActive == 'label'">
                        <t-table row-key="index" :data="xndata" :columns="columns" :bordered="true" :hover="false"
                            :table-layout="'auto'" cell-empty-content="" rowClassName="ran-empty-table--head-notshow">
                        </t-table>
                        <div class="ran-tree__item ran-tree--open">
                            <span class="ran-tree--transition">
                                <t-icon name="caret-right-small" class="ran-tree__icon" size="1.5em"></t-icon>
                            </span>
                            <t-tag theme="success" variant="light-outline">啊啊啊啊</t-tag>
                        </div>
                        <t-table row-key="index" :data="data" :columns="columns" :bordered="true" :hover="true"
                            :table-layout="'auto'" cell-empty-content="-"
                            :onCellClick="handleCellClick">
                        </t-table>
                    </div>

                    <div class="main_box_content_view" v-else-if="TabsActive == 'weight'">
                        <t-table row-key="index" :data="data" :columns="columns" :bordered="true" :hover="true"
                            :table-layout="'auto'" :size="'medium'" cell-empty-content="" @row-click="handleRowClick">
                        </t-table>
                    </div>

                    <div class="main_box_content_view" v-else-if="TabsActive == 'admin'">
                        <iframe src="./panel.html" style="width: 100%;height:1080px"></iframe>
                    </div>

                    <div class="main_box_content_view" v-else-if="TabsActive == 'add'">
                        <div id="login_block" v-if="login_block_show">
                            <div id="bubble" class="bubble"
                                :style="{ height: windowHeight + 'px', width: windowWidth + 'px' }" style="max-width:100%;">
                            </div>
                            <div>
                                <div class="login" :style="{ height: windowHeight - 56 + 'px', width: windowWidth + 'px' }"
                                    style="max-width:100%;">
                                    <div class="login-box">
                                        <div class="head">
                                            <div class="loginbox_title">任务管理系统-Login</div>
                                        </div>
                                        <div class="form">
                                            <div class="content">
                                                <!--from start-->
                                                <t-form ref="form" :rules="rules" :data="formData" :colon="true"
                                                    :label-width="0" :onSubmit="onSubmit">
                                                    <t-form-item name="username">
                                                        <t-input id="button10000" v-model="formData.username" clearable
                                                            placeholder="请输入账户名" ref="fromusername"
                                                            :onEnter="formusernameenter" :onChange="quchukongge()">
                                                            <template #prefix-icon>
                                                                <desktop-icon />
                                                            </template>
                                                        </t-input>
                                                    </t-form-item>
                                                    <t-form-item name="password">
                                                        <t-input id="button10046" v-model="formData.password"
                                                            type="password" clearable placeholder="请输入密码"
                                                            ref="frompassword">
                                                            <template #prefix-icon>
                                                                <lock-on-icon />
                                                            </template>
                                                        </t-input>
                                                    </t-form-item>

                                                    <t-form-item>
                                                        <t-button id="button10086" theme="primary" type="submit" block
                                                            :disabled="disabled">登录</t-button>
                                                    </t-form-item>
                                                </t-form>
                                                <!--form end-->
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- <a href="./panel.html" target="_blank">
                                <div id="back_to_panel_big" class="back_to_panel_box_big">
                                    <div class="back_to_panel_box_text"><t-icon name="arrow-left"
                                            size="20px"></t-icon><span>返回设备管理系统</span>
                                    </div>
                                </div>
                            </a> -->
                        </div>

                        <div class="admin_box" v-else>
                            <div id="left-control">
                                <div style="display: flex;gap: 4px;flex-direction: column;">
                                    <div class="max_width_30_percentage">
                                        <div>工作内容(任务名称)</div>
                                        <div>
                                            <t-input></t-input>
                                        </div>
                                    </div>

                                    <div class="max_width_30_percentage">
                                        <div>工作时间</div>
                                        <div>
                                            <t-date-picker :value="add_task_from.date" enable-time-picker allow-input
                                                clearable format="YYYY-MM-DD a hh:mm:ss" />
                                        </div>
                                    </div>

                                    <div class="max_width_30_percentage">
                                        <div>任务标签</div>
                                        <div>
                                            <t-select-input :value="selectValue3" placeholder="点击选择" multiple
                                                :popup-visible="popupVisible" @popup-visible-change="onPopupVisibleChange">
                                                <template #valueDisplay="{ value }">
                                                    <t-tag v-for="(item, index) in value" :theme="options[index].theme"
                                                        variant="light-outline" :key="item" style="margin-right: 4px">
                                                        <span class="displaySpan" :id="item" :tag="options[index].value">
                                                            <span>{{ item }}</span>
                                                        </span>
                                                    </t-tag>
                                                </template>
                                                <template #panel>
                                                    <ul class="tdesign-demo__select-input-ul-single">
                                                        <li v-for="item in options" :key="item.value"
                                                            @click="() => onOptionClick(item)">
                                                            <t-tag :theme="item.theme" variant="light-outline"
                                                                style="margin-right: 4px">
                                                                <span class="displaySpan" :tag="item.label">
                                                                    <span>{{ item.label }}</span>
                                                                </span>
                                                            </t-tag>
                                                        </li>
                                                    </ul>
                                                </template>
                                            </t-select-input>
                                        </div>
                                    </div>

                                    <div>
                                        <t-dialog :visible="admin_add_person_dialog_show" header="绑定成员" width='560px'
                                            id="admin_add_person_dialog">
                                            <t-input placeholder="搜索成员">
                                                <template #prefix-icon>
                                                    <t-icon name="search" size="20px" />
                                                </template>
                                            </t-input>
                                            <div class="admin_box_person_choose_box_view">
                                                <div :key="index" v-for="(item, index) of person_list"
                                                    class="admin_box_person_choose_box"
                                                    :class="{ active: item.choose == true }" :name="item.id"
                                                    @click="handle_choose_person_click($event.currentTarget.__vnode.props.name)">
                                                    <div
                                                        style="display: flex;flex-direction: column;width: 90%;margin: 16px auto;">
                                                        <div style="font: var(--td-font-mark-medium)">{{ item.name }}</div>
                                                        <div
                                                            style="display: flex;flex-direction: row;justify-content: space-between;">
                                                            <div style="width: 20%;">
                                                                <div style="margin-top: 4px;">ID</div>
                                                                <div style="margin-top: 8px;">{{ item.code }}</div>
                                                            </div>
                                                            <div style="width: 20%;">
                                                                <div style="margin-top: 4px;">班级</div>
                                                                <div style="margin-top: 8px;">{{ item.class }}</div>
                                                            </div>
                                                            <div style="width: 20%;">
                                                                <div style="margin-top: 4px;">身份</div>
                                                                <div style="margin-top: 8px;">{{ item.identity }}</div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </t-dialog>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div v-if="loading_progress">
        <div
            style="top: 0px;width: 100%;height: 100%;position: fixed;left: 0px;right: 0px;z-index: 1001;display: inline-flex;align-items: center;vertical-align: middle;justify-content: center;flex-direction: column;color: var(--td-text-color-primary);">
            <t-progress theme="circle" :percentage="progress_number" :size="120" />
            <div style="font: var(--td-font-title-large);margin-top: 16px;font-size: 28px;">{{ progress_text }}</div>
        </div>
        <div id="mask"
            style="top: 0px;width: 100%;position: fixed;margin: 0px auto;height: 100%;background: rgb(0 0 0 / 40%);z-index: 1000;">
        </div>
    </div>
    <footer class="mainapp_footer">
        Powered By Wesley With ❤️
    </footer>
</template>

<script setup>
import { reactive } from 'vue';
//import { MessagePlugin } from 'tdesign-vue-next';
import { DesktopIcon, LockOnIcon } from 'tdesign-icons-vue-next';
import { ErrorCircleFilledIcon, CheckCircleFilledIcon, CloseCircleFilledIcon } from 'tdesign-icons-vue-next';
import { ChevronDownIcon } from 'tdesign-icons-vue-next';
import { ControlPlatformIcon } from 'tdesign-icons-vue-next';



const rules = reactive({
    username: [
        { required: true, message: '请输入账户名', type: 'error', trigger: 'blur' },
        { min: 0, max: 20, message: '账户名有点长啊...', type: 'error', trigger: 'blur' },
    ],
    password: [
        { required: true, message: '请输入密码', type: 'error', trigger: 'blur' },
        { min: 1, max: 100, message: '密码好像有点短？', type: 'error', trigger: 'blur' },
    ]
});

const statusNameListMap = {
    0: { label: '一般任务', theme: 'success' },
    1: { label: '紧急任务', theme: 'warning' },
    2: { label: '计划任务', theme: 'primary' },
    3: { label: '已取消', theme: 'danger' },
};
const data =[];
const xndata = [{
        index: '',
        id: '',
        applicant: '',
        label: 0,
        channel: '',
        name: '',
        time: '',
        changetime: '',
        whocreate: '',
        weight: '',
        place: '',
    }]
const total = 28;
for (let i = 0; i < total; i++) {
    data.push({
        index: i + 1,
        id: i + 1,
        applicant: ['贾明', '张三', '王芳'][i % 3],
        label: i % 4,
        channel: ['电子签署', '纸质签署', '纸质签署'][i % 3],
        detail: {
            email: ['w.cezkdudy@lhll.au', 'r.nmgw@peurezgn.sl', 'p.cumx@rampblpa.ru'][i % 3],
        },
        name: ['宣传物料制作费用', 'algolia 服务报销', '相关周边制作费', '激励奖品快递费'][i % 4],
        time: ['2022-01-01 14:00', '2022-02-01 14:00', '2022-03-01 14:00', '2022-04-01 14:00', '2022-05-01 14:00'][i % 4],
        changetime: ['2022-01-01 14:00', '2022-02-01 14:00', '2022-03-01 14:00', '2022-04-01 14:00', '2022-05-01 14:00'][i % 5],
        whocreate: '人人人',
        weight: ['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'][i % 5],
        place: ['一个地方', '一个神奇的地方', '一个非常非常神奇的地方', '一个非常非常非常非常神奇的地方'][i % 4],
    });
}


//

const columns = ref([
    { colKey: 'id', title: '任务id', width: '80px' ,thClassName:['ran-empty-table--head-left']},
    { colKey: 'time', title: '工作时间', width: '150px' },
    { colKey: 'name', title: '工作内容', width: '260px' },

    { colKey: 'place', title: '工作地点', width: '250px' },
    {
        colKey: 'lable', title: '分类',
        width: '80px',
        align: 'center',
        cell: (h, { row }) => {
            return (
                <t-tag theme={statusNameListMap[row.label].theme} variant="light-outline">
                    {statusNameListMap[row.label].label}
                </t-tag>
            );
        },
    },
    {
        colKey: 'assigned', title: '人员安排', width: '178px', cell: (h, { row }) => {
            return (
                <span>
                    <t-tag theme="default" variant="light-outline" style="margin:0px 4px">
                        人人人
                    </t-tag>
                    <t-tag theme="default" variant="light-outline" style="margin:0px 4px">
                        人人人
                    </t-tag>
                    <t-tag theme="default" variant="light-outline" style="margin:0px 4px">
                        人人人
                    </t-tag>
                </span>
            );
        },
    },
    { colKey: 'needequipment', title: '所需设备',width: '140px' },
    { colKey: 'whocreate', title: '创建人', width: '100px', align: 'center', },
    { colKey: 'changetime', title: '修改时间', width: '200px' },
    { colKey: 'weight', title: '权重', width: '180px',thClassName:'ran-empty-table--head-tight' },
]);

const handleRowClick = (e) => {
    console.log(e);
};

const handleCellClick = (e) => {
    console.log("是否点击图标：" + e.e.target.__vnode.type == 'svg' || e.e.target.__vnode.type == 'use', "行：", e.rowIndex, "列：");
};

const ranTableHeadLine1Together = ({ col, rowIndex, colIndex }) => {
    if (rowIndex === 0) {
        return {
            colspan: 10,
            rowspan: 1,
        };
    }
};


const options = [
    { label: '一般任务', value: 'normal', theme: 'success' },
    { label: '紧急任务', value: 2, theme: 'warning' },
    { label: '计划任务', value: 3, theme: 'primary' },
    { label: '已取消', value: 4, theme: 'danger' },
];

const selectValue3 = ref([]);
const popupVisible = ref(false);

const onOptionClick = (item) => {
    selectValue3.value = item.label;
    popupVisible.value = false;
};
const onPopupVisibleChange = (val, context) => {
    console.log(context);
    popupVisible.value = val;
};

</script>

<script>
import { reactive, ref } from 'vue';

import { useDark, useToggle } from '@vueuse/core';

//import VueApexCharts from "vue3-apexcharts";

import { MessagePlugin } from 'tdesign-vue-next';
import { locale } from 'dayjs';
import axios from 'axios';
import FakeProgress from "fake-progress";

export default {
    name: 'Task',
    components: {

    },
    data() {
        return {
            formData: reactive({
                username: '',
                password: '',
            }),
            windowHeight: "0",
            windowWidth: "0",
            subtime: 0,
            bantime: 0,
            disabled: false,
            timer: null,
            skiperror: false,
            showtestdialog: true,

            //new
            login_block_show: true,
            TabsActive: 'label',
            admin_add_person_dialog_show: false,
            person_list: [],
            person_list_backup: [],
            choose_person_list: [],
            progress_number: 0,
            progress_text: '加载中...',
            loading_progress: false,
            add_task_from: {
                date: null
            },
        }
    },
    setup() {
        const isDark = useDark({
            selector: 'html',
            attribute: 'theme-mode',
            valueDark: 'dark',
            valueLight: 'light',
        })

        const toggleDark = useToggle(isDark)
        return {
            isDark,
            toggleDark,
        }
    },
    mounted() {
        //登陆界面显示才获取焦点，不然会报错
        if (this.$data.login_block_show && this.$data.TabsActive == 'add') {
            this.$refs['fromusername'].focus()
        }
        console.log('【登录页加载】')
        //页面大小改变时
        window.onresize = () => {
            return (() => {
                this.getPageWidthAndHeight()
            })()
        };
        this.getPageWidthAndHeight()

        //检测是否为skip error状态
        var skipe = this.getQueryVariable('skipe')
        if (skipe == 'yes' || skipe == 'true' || skipe != false) {
            this.$data.skiperror = true
        }
        //检测ban
        if (this.getck('ban') == 'true' && !this.skiperror && this.getck('LOGINERRORTIMEOUT') > this.gettimestamp('s')) {
            this.bantime = 120;
            //消息自动更新 ↓
            var content = () => { return ("您已输入错误超过 5 次，请" + this.bantime + "秒后再重试。(刷新会导致状态重载)") }
            this.showMessage('error', 0, content)
            this.disabled = true;
            //更新subtime
            this.timer = setInterval(() => {
                var that = this//代理
                that.bantime = that.bantime - 1
                if (that.bantime == 0) {
                    that.disabled = false;
                    //关闭所有消息
                    that.showMessage('close')
                    //重置次数
                    that.subtime = 0;
                    var exdate = new Date();
                    exdate.setDate(exdate.getDate() - 30);
                    document.cookie = "ban=false;path=/;expires=" + exdate.toGMTString();
                    clearInterval(this.timer);
                }
            }, 1000)
        }


        var p = new FakeProgress({
            timeConstant: 10000,
            autoStart: false
        })
        p.start()
        setInterval(() => {
            this.$data.progress_number = parseInt(p.progress * 100)
        }, 1);
        setTimeout(() => {
            p.end()
        }, 5000);

        /**NEW */
        // if (this.getck('key') != "" && this.getck('login') != "true") {
        //     this.$data.login_block_show = false
        // }
        // else {
        //     this.$data.login_block_show = true
        // }


        axios.post('http://10.3.146.103/json/user/list', { key: this.getck('key') }, { headers: { "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8" } }).then((res) => {
            if (res.data.errcode == -1) {
                MessagePlugin.error('请求出错：' + res.data.errmsg)
            }
            else if (res.data.errcode == 0) {
                let abc = []
                for (let index = 0; index < res.data.data.len; index++) {
                    const element = res.data.data[index];
                    var a = {
                        id: element.id,
                        name: element.username,
                        code: element.usercode,
                        class: element.class,
                        choose: false,
                        identity: (element.admin == 1 ? '管理员' : '成员')
                    }
                    abc.push(a)
                    if (index == res.data.data.len - 1) {
                        this.$data.person_list = abc
                        this.$data.person_list_backup = abc
                    }
                }
            }
            else if (errcode == -1003) {
                MessagePlugin.error('登录失效，获取信息失败，请重新登录')
            }
        })

    },
    methods: {
        thhhh() {
            console.log(123)
        },
        // 点击标签
        handleTabsClick(e) {
            this.$data.TabsActive = e
            this.getPageWidthAndHeight()
        },

        handle_choose_person_click(e) {
            //遍历数据
            for (let index = 0; index < this.$data.person_list.length; index++) {
                const element = this.$data.person_list[index];
                if (element.id == e) {
                    element.choose = !element.choose
                    if (element.choose == true) {
                        this.$data.choose_person_list.push(element)
                        console.log(this.$data.choose_person_list)
                    }
                    else {
                        for (let index = 0; index < this.$data.choose_person_list.length; index++) {
                            const element = this.$data.choose_person_list[index];
                            if (element.id == e) {
                                this.$data.choose_person_list.splice(index, 1)
                                console.log(this.$data.choose_person_list)
                            }
                        }
                    }
                }
            }
        },


        getPageWidthAndHeight() {
            var that = this;
            that.windowHeight = document.documentElement.clientHeight;
            that.windowWidth = document.documentElement.clientWidth;
            let a = {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
            }
            return a
        },



















        //去除用户名输入框空格
        quchukongge() {
            this.$data.formData.username = this.$data.formData.username.replace(/\s*/g, "")
        },
        clickasdasdasdasdasasdczxcvrw() {
            this.$data.showtestdialog = false
        },
        formusernameenter() {
            this.$refs['frompassword'].focus()
        },

        /**
        * @onSubmit
        * @desc 提交表单
        * @param a 验证信息
        */
        /**
         * 最新规则：
         * 1.是管理员则会显示管理界面不是管理员则只显示借出界面
         * 2.无论是不是管理员都有借出界面
         */
        onSubmit(a) {
            var username = this.formData.username
            var password = this.formData.password
            var loginurl = 'http://10.3.146.103/json/login'
            // var loginurl = 'http://test.ipv4-ran7.top/json/login'
            var skipe = this.skiperror
            if (a.validateResult == true) {
                const xhr = new XMLHttpRequest()
                xhr.open('post', loginurl, true)
                //正经返回数据
                //{"data":{"admin":0,"class":"\u57ce\u8f68221","login":"yes","name":"\u8d75\u6dd1\u83b9","password":"123456","usercode":"cg22150"},"errcode":0,"errmsg":"ok"}
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
                xhr.da
                xhr.onload = () => {
                    //去除回车、空格等一些空的占位符
                    var result = JSON.parse(xhr.response.replace(/\r|\n/ig, ""));
                    if (result.errcode == 0) {
                        // if (result.data.admin == 1) {
                        this.$data.subtime == 0 //还原次数
                        document.cookie = "login=true;path=/;expires=86400";
                        document.cookie = "key=" + result.key + ";path=/;expires=86400"
                        document.cookie = "username=" + result.data.name + ";path=/;expires=86400"
                        document.cookie = "usercode=" + result.data.username + ";path=/;expires=86400"
                        document.cookie = "userclass=" + result.data.class + ";path=/;expires=86400"
                        document.cookie = "logintime=" + result.data.login_time + ";path=/;expires=86400"
                        document.cookie = "keytimeout=" + result.data.timeout + ";path=/;expires=86400"
                        document.cookie = "admin=" + result.data.admin + ";path=/;expires=86400"
                        if (password == '123456') {
                            document.cookie = "need_change_password=need;path=/;expires=86400"
                        }
                        location.reload()
                    }
                    else if (result.errcode == -2001) {
                        //账户或密码错误
                        MessagePlugin.error('账户或密码错误', 5000)
                        this.$data.subtime++
                    }
                    else {
                        MessagePlugin.error("登陆失败：" + result.errcode + ", " + result.errmsg, 5000)
                        console.group("登录系统错误")
                        console.error("登录失败:", xhr)
                        console.groupEnd()
                    }
                }
                xhr.send('username=' + username + '&password=' + password)
            }
            else {
                if (skipe) {
                    console.warn('【Skip Error】: 保护状态')
                }
                else {
                    this.$data.subtime++
                }
            }

            //查询提交次数
            if (this.subtime == 5 && !skipe) {
                this.bantime = 120;
                console.log('错误状态')
                //gettimestamp
                var timeouttimestamp = this.gettimestamp('s') + 120
                document.cookie = "LOGINERRORTIMEOUT=" + timeouttimestamp + ";path=/;expires=130"
                //消息自动更新 ↓
                var content = () => { return ("您已输入错误超过 5 次，请" + this.bantime + "秒后再重试。") }
                this.showMessage('error', 0, content)
                this.disabled = true;
                //保存cookie
                var exdate = new Date();
                exdate.setDate(exdate.getDate() + 30);
                document.cookie = "ban=true;path=/;expires=" + exdate.toGMTString();
                //更新
                this.timer = setInterval(() => {
                    var that = this//代理
                    that.bantime = that.bantime - 1
                    if (that.bantime == 0) {
                        that.disabled = false;
                        //关闭所有消息
                        that.showMessage('close')
                        //重置次数
                        that.subtime = 0;
                        var exdate = new Date();
                        exdate.setDate(exdate.getDate() - 30);
                        document.cookie = "ban=false;path=/;expires=" + exdate.toGMTString();
                        clearInterval(this.timer);
                    }
                }, 1000)
            }
        },


        /**
        * @gettimestamp
        * @desc 获取时间戳
        * @param type 毫秒/秒
        */
        gettimestamp(e) {
            if (e == 's') {
                //秒
                return Math.floor(new Date().getTime() / 1000)
            }
            else {
                return new Date().getTime()
            }

        },

        /**
        * @getQueryVariable
        * @desc 获取参数
        * @param id 参数名
        */
        getQueryVariable(variable) {
            var query = window.location.search.substring(1);
            var vars = query.split("&");
            for (var i = 0; i < vars.length; i++) {
                var pair = vars[i].split("=");
                if (pair[0] == variable) { return pair[1]; }
            }
            return (false);
        },

        /**
        * @getck
        * @desc 获取cookie
        * @param sname cookie名
        */
        getck(sname) {
            var acookie = document.cookie.split("; ");
            try {
                for (var i = 0; i < acookie.length; i++) {
                    var arr = acookie[i].split("=");
                    if (sname == arr[0]) {
                        if (arr.length > 1)
                            return arr[1];
                        else
                            return false;
                    }
                }
                return false;
            }
            catch (e) {
                console.log('没有cookie', e)
                return false;
            }
        },

        /**
        * @showMessage
        * @desc 显示TDesign中的Message组件
        * @param
        * @type info 消息
        * @type success 成功
        * @type warning 警示
        * @type error 失败
        * @type question 询问
        * @type loading 加载
        * @content content = () => {return (<div>登录失败</div>)}
        */
        showMessage(type, time, content) {
            if (type == 'info') {
                MessagePlugin.info({ duration: time, content: content })
            }
            if (type == 'success') {
                MessagePlugin.success({ duration: time, content: content })
            }
            if (type == 'warning') {
                MessagePlugin.warning({ duration: time, content: content })
            }
            if (type == 'error') {
                MessagePlugin.error({ duration: time, content: content })
            }
            if (type == 'question') {
                MessagePlugin.question({ duration: time, content: content })
            }
            if (type == 'loading') {
                MessagePlugin.loading({ duration: time, content: content })
            }
            if (type == 'close') {
                MessagePlugin.closeAll()
            }
        },
    }
}
</script>

<style>
.ran-tree--transition .ran-tree__icon:hover {
    transition: .2s linear;
}

.ran-tree__icon:hover {
    background-color: var(--td-bg-color-container-hover);
}


.t-tree--transition .ran-tree__icon {
    transition: color,
        transform cubic-bezier(.38, 0, .24, 1) .2s;
}

.ran-tree--open .ran-tree__icon {
    transform: rotate(90deg) !important;
}

.ran-tree__item .ran-tree__icon {
    transform: rotate(0);
}

.ran-tree__item .ran-tree__icon {
    color: var(--td-text-color-secondary) !important;
}
.ran-tree__item .t-tag{
    user-select: none;
}

.ran-tree--open .ran-tree__icon {
    color: var(--td-text-color-brand) !important;
}



td.t-table__td-first-col:has(>div.ran-tree__item) {
    padding-left: 4px !important;
}

tr:hover:has(div.ran-tree__item) {
    background-color: unset !important;
}

.ran-empty-table--head-notshow{
    user-select: none;
    opacity: 0 !important;
}

.t-table__content:has(.ran-empty-table--head-notshow){
    border-bottom: none !important;
    border-left: none !important;
    border-radius: none !important;
}

.t-table--bordered th:first-child{
    border-left-width: 1px !important;
}
.t-table--bordered th:last-child{
    border-left-width: 1px !important;
}















/**改变tag的颜色 */
:root,
:root[theme-mode="dark"] {
    --td-success-color: #3ad9a5 !important;
    --td-error-color: #e26d76 !important;
    --td-brand-color: #659fff !important;
    --td-warning-color: #e1925e !important;
}

#admin_add_person_dialog .t-dialog__header {
    padding-bottom: 16px;
}

.admin_box {
    width: 100%;
}

.loading_lock {
    overflow: hidden;
}

/**左 */
.admin_box>#left-control {
    width: 50%;
    color: var(--td-text-color-primary);
    font: var(--td-font-body-medium);
}

/**最大宽度30% */
.max_width_30_percentage {
    max-width: 30%;
}

.admin_box_person_choose_box_view {
    height: 600px;
}

/**dialog的滚动条 */
.t-dialog__body::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

.t-dialog__body::-webkit-scrollbar-thumb {
    border: 2px solid transparent;
    background-clip: content-box;
    background-color: var(--td-scrollbar-color);
    border-radius: 15px;
}

.admin_box_person_choose_box {
    overflow: hidden;
    position: relative;
    border: 1px var(--td-bg-color-page) solid;
    background-color: var(--td-bg-color-page);
    border-radius: 8px;
    margin-top: 16px;
    user-select: none;
}

.admin_box_person_choose_box.active {
    border: 1px var(--td-brand-color) solid;
}

.admin_box_person_choose_box:first-child {
    margin-top: 24px;
}

.admin_box_person_choose_box.active::before {
    content: " ";
    z-index: 1;
    width: 31px;
    height: 31px;
    position: absolute;
    left: 0;
    top: 0;
    -webkit-transform: translate(-50%, -50%) rotate(45deg);
    transform: translate(-50%, -50%) rotate(45deg);
    background-color: var(--td-brand-color);
}

.admin_box_person_choose_box.active::after {
    content: " ";
    z-index: 1;
    left: 3px;
    top: 6px;
    width: 5px;
    height: 8px;
    position: absolute;
    display: table;
    border: 1px solid #fff;
    border-top: 0;
    border-left: 0;
    -webkit-transform: rotate(45deg) scale(1) translate(-50%, -50%);
    transform: rotate(45deg) scale(1) translate(-50%, -50%);
    opacity: 1;
    transition: all .2s cubic-bezier(.12, .4, .29, 1.46) .1s;
}

.main_box_big {
    width: 90%;
    height: -moz-fit-content;
    height: fit-content;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    margin-top: 120px;
    position: relative;
}

/**内容 */
.main_box_content_view {
    width: 97%;
    margin: 0 auto;
    margin-top: 35px;
    margin-bottom: 35px;
}

.main_box_content_big {
    width: 100%;
    background: var(--td-bg-color-container);
    border-radius: 15px;
    border-top-right-radius: 0px !important;
    border: 1px #fff solid;
    border-top: none;
}

.main_box_content_big::before {
    content: " ";
    height: 15px;
    display: flex;
    width: calc(100% - 493px);
    position: absolute;
    border: 1px #fff solid;
    border-top-left-radius: 15px;
    left: 0px;
    border-bottom: none;
    border-right: none;
    top: -1px;
}

/**标签组 */
.main_box_tabs_big {
    position: absolute;
    right: -2px;
    top: -41px;
}

.main_box_tabs_view {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    user-select: none;
}

.main_box_tabs_view_tab {
    width: 120px;
    display: flex;
    justify-content: center;
    color: var(--td-bg-color-container);
    background: var(--td-text-color-primary);
    height: 40px;
    align-items: center;
    font: var(--td-font-title-medium);
    border: 1px #fff solid;
    border-bottom: none;
}

.main_box_tabs_view_tab:first-child {
    border-top-left-radius: 15px;
}

.main_box_tabs_view_tab:last-child {
    border-top-right-radius: 15px;
}


.tabs_active {
    color: var(--td-text-color-primary);
    background: var(--td-bg-color-container);
}

/**第一个标签 */
.main_box_tabs_view_tab:first-child {
    position: relative;
    border-right: none;
    border-left: none;
}

.main_box_tabs_view_tab:first-child::after {
    content: " ";
    position: absolute;
    width: 21px;
    height: 32px;
    top: -1px;
    left: -1px;
    border-top-left-radius: 15px;
    border: 1px #fff solid;
    border-bottom: none;
    border-right: none;
}

.main_box_tabs_view_tab:last-child {
    position: relative;
    border-left: none;
}

.main_box_tabs_view_tab.tabs_active:first-child::before {
    content: " ";
    position: absolute;
    width: 15px;
    height: 15px;
    bottom: 0px;
    left: -15px;
    background: radial-gradient(circle at 0 0, transparent 15px, #fff 16px, var(--td-bg-color-container) 17px)
}

.main_box_tabs_view_tab:first-child::before {
    content: " ";
    position: absolute;
    width: 15px;
    height: 15px;
    bottom: 0px;
    left: -15px;
    background: radial-gradient(circle at 0 0, transparent 15px, #fff 16px, var(--td-text-color-primary) 16px);
}

.mainapp_footer {
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--td-text-color-primary);
    font: var(--td-font-body-medium);
    letter-spacing: 0.5px;

}

/**标签选择器 */
.tdesign-demo__select-input-ul-single {
    display: flex;
    flex-direction: column;
    padding: 0;
    gap: 2px;
}

.tdesign-demo__select-input-ul-single>li {
    display: block;
    border-radius: 3px;
    line-height: 22px;
    cursor: pointer;
    padding: 3px 8px;
    color: var(--td-text-color-primary);
    transition: background-color 0.2s linear;
    white-space: nowrap;
    word-wrap: normal;
    overflow: hidden;
    text-overflow: ellipsis;
}

.tdesign-demo__select-input-ul-single>li:hover {
    background-color: var(--td-bg-color-container-hover);
}






/**原有样式 */
body {
    background: var(--td-bg-color-page) !important;
    margin: 0px;
}

a {
    color: #fff;
    text-decoration: none
}

a:visited {
    color: #fff;
    text-decoration: none
}

a:focus {
    color: rgb(207, 207, 207);
    text-decoration: none
}

a:hover {
    color: rgb(207, 207, 207);
    text-decoration: none
}


.bubble {
    overflow: hidden;
    background: url(../../assets/blog_bg.jpg) repeat;
}

.login {
    position: absolute;
    bottom: 0;
    display: flex;
    width: 100vw;
    height: 100vh;
    align-items: center;
    justify-content: center;
}

.login-box {
    overflow: hidden;
    width: 430px;
    padding: 0;
    background: transparent;
    margin-top: -150px;
}

.loginbox_title {
    font-weight: bold;
    color: rgb(255, 255, 255);
    letter-spacing: 3px;
    text-transform: uppercase;
    font-family: Montserrat;
    font-size: 60px;
    position: absolute;
    left: 0px;
    right: 0px;
    margin: 0px auto;
    width: fit-content;
    padding-top: 0px;
}

.head {
    background: transparent;
    height: 135px;
}

img {
    display: block;
    width: 430px;
    margin: 0 auto;
    user-select: none;
}

.form {
    position: relative;
    background: var(--td-bg-color-container);
    border-radius: 14px;
}

.profile-avatar {
    display: block;
    position: absolute;
    height: 100px;
    width: 100px;
    border-radius: 50%;
    border: 4px solid var(--ba-bg-color-overlay);
    top: -50px;
    right: calc(50% - 50px);
    z-index: 2;
    user-select: none;
}

.content {
    padding: 55px 40px 40px 40px;
}

.submit-button {
    width: 100%;
    letter-spacing: 2px;
    font-weight: 300;
    margin-top: 15px;
    --el-button-bg-color: var(--el-color-primary);
}


/**new */
.back_to_panel_box_big {
    position: fixed;
    top: 60px;
    left: 100px;
    z-index: 999;
    background-color: #fff;
    width: 190px;
    height: 55px;
    border-radius: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    user-select: none;
}

.back_to_panel_box_text {
    color: var(--td-bg-color-page);
    font: var(--td-font-title-medium);
}
</style>