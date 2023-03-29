
<template>
    <!--alert-->
<!-- <div style="width: 600px;position: fixed;left: 0;right: 0;margin: 0 auto;margin-top: 40px;">
        <el-alert show-icon='true' type="error" :title="alert_title" :description="alert_desc" v-show="alert_show">
        </el-alert>
                    </div> -->
    <div id="bubble" class="bubble" :style="{ height: windowHeight + 'px', width: windowWidth + 'px' }"
        style="max-width:100%;"></div>
    <div>
        <div class="login" :style="{ height: windowHeight - 56 + 'px', width: windowWidth + 'px' }" style="max-width:100%;">
            <div class="login-box">
                <div class="head">
                    <div
                        style="font-weight: bold;color: rgb(255 255 255);letter-spacing: 3px;text-transform: uppercase;font-family: Montserrat;font-size: 60px;position: absolute;left: 0;right: 0;margin: 0 auto;width: 212px;padding-top: 45px;">
                        Login</div>
                    <!-- <img :src="lh" alt="" /> -->
                </div>
                <div class="form">
                    <div class="content">
                        <!--from start-->
                        <t-form ref="form" :rules="rules" :data="formData" :colon="true" :label-width="0"
                            :onSubmit="onSubmit">

                        <!-- <t-form-item name="jiqima">
                                <t-input v-model="formData.username" clearable placeholder="登陆机器码">
                                    <template #prefix-icon>
                                        <desktop-icon />
                                    </template>
                                </t-input>
                                            </t-form-item> -->

                            <t-form-item name="username">
                                <t-input id="button10000" v-model="formData.username" clearable placeholder="请输入账户名"
                                    ref="fromusername" :onEnter="formusernameenter" :onChange="quchukongge()">
                                    <template #prefix-icon>
                                        <desktop-icon />
                                    </template>
                                </t-input>
                            </t-form-item>

                            <t-form-item name="password">
                                <t-input id="button10046" v-model="formData.password" type="password" clearable
                                    placeholder="请输入密码" ref="frompassword">
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

    <!--提示-->
<t-dialog v-model:visible="showtestdialog" theme="info" header="温馨提示"
        body="由于部门名单更新，用户code有所变更，请查看新版人员表格确定自己的用户code。(默认密码：123456)" :closeBtn="false" :cancelBtn="关闭"
        :closeOnOverlayClick="false" :closeOnEscKeydown="false" confirmBtn="我已知晓"
                :onConfirm="clickasdasdasdasdasasdczxcvrw"></t-dialog>
</template>

<script setup>
import { reactive } from 'vue';
//import { MessagePlugin } from 'tdesign-vue-next';
import { DesktopIcon, LockOnIcon } from 'tdesign-icons-vue-next';


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


</script>

<script>
//import Axios from 'axios';
import lh from '../assets/login-header.png'
// import { Unlock, User } from "@element-plus/icons-vue";
import { MessagePlugin } from 'tdesign-vue-next';
//let userid = navigator.userAgent

export default {
    name: "LoginPage",
    setup() {
        return {
            lh,
            // Unlock,
            // User,
        }
    },
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
        }

    },
    mounted() {
        //获取焦点
        this.$refs['fromusername'].focus()
        console.log('【登录页加载】')
        var that = this;
        // <!--把window.onresize事件挂在到mounted函数上-->

        //保存cookie
        // var exdate = new Date();
        // exdate.setDate(exdate.getDate() + 30);
        // document.cookie = "ynlogin=true;path=/;expires=" + exdate.toGMTString();
        window.onresize = () => {
            return (() => {
                window.fullHeight = document.documentElement.clientHeight;
                window.fullWidth = document.documentElement.clientWidth;
                that.windowHeight = window.fullHeight;  //高
                that.windowWidth = window.fullWidth; //宽
            })()
        };
        window.fullHeight = document.documentElement.clientHeight;
        window.fullWidth = document.documentElement.clientWidth;
        that.windowHeight = window.fullHeight;  //高
        that.windowWidth = window.fullWidth; //宽
        //检测是否为skip error状态
        var skipe = this.getQueryVariable('skipe')

        if (skipe == 'yes' || skipe == 'true' || skipe != false) {
            this.$data.skiperror = true
        }
        //检测ban
        if (this.getck('ban') == 'true' && !this.skiperror) {
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
                    exdate.setDate(exdate.getDate() + 30);
                    document.cookie = "ban=false;path=/;expires=" + exdate.toGMTString();
                    clearInterval(this.timer);
                }
            }, 1000)
        }

    },
    methods: {
        //去除用户名输入框空格
        quchukongge() {
            this.$data.formData.username = id.replace(/\s*/g, "")
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
            // if (username == "" || password == ""){
            //     MessagePlugin.error('输完了吗？你就提交。。。', 5000)
            //     this.$data.disabled = true
            //     setTimeout(() => {
            //         MessagePlugin.error('小调皮，按钮给你锁了，哈哈哈哈', 5000)
            //     }, 1000);
            //     setTimeout(() => {
            //         MessagePlugin.error('真无语你这种人。。。', 5000)
            //         MessagePlugin.error('再见到按钮都给你删了', 5000)
            //         document.getElementById("button10086").style.display = "none"
            //     }, 2000);
            //     setTimeout(() => {
            //         MessagePlugin.error('框都给你删了', 5000)
            //         if (username != ""){
            //             document.getElementById("button10000").style.display = "none"
            //         }
            //         if (password != ""){
            //             document.getElementById("button10046").style.display = "none"
            //         }
            //     }, 3000);
            //     setTimeout(() => {
            //         MessagePlugin.success('看清楚再按，先给你解了', 5000)
            //         document.getElementById("button10086").style.display = ""
            //         document.getElementById("button10046").style.display = ""
            //         document.getElementById("button10000").style.display = ""
            //         this.$data.disabled = false
            //     }, 4000);
            //     return
            // }
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
                //show-alert
                console.log('错误状态')
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
                        exdate.setDate(exdate.getDate() + 30);
                        document.cookie = "ban=false;path=/;expires=" + exdate.toGMTString();
                        clearInterval(this.timer);
                    }
                }, 1000)
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

<style scoped>
body {
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
    background: url(../assets/blog_bg.jpg) repeat;
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
</style>
