<template>
    <div>
        <div
            style="font-size: 10px;color: var(--td-text-color-secondary);position: absolute;display: flex;flex-direction: column;text-align: end;right: 37px;top: 87px;">
            <span v-if="username == ''">User:非法登录？</span>
            <span v-else>User:{{ username }}</span>
            <span v-if="usercode == ''">Code:Fuck you</span>
            <span v-else>Code:{{ usercode }}</span>
        </div>

        <div style="display: flex;justify-content: center;">
            <t-tabs :value="tabsvalue" :theme="theme" @change="handlerChange"
                style="width: 98%;padding: 15px;padding-top: 0px;min-height: 310px;">
                <t-tab-panel value="first">
                    <template #label> <span class="lendtap"><t-icon name="logout"
                                class="tabs-icon-margin" />借出</span></template>
                    <div id="lendpage">
                        <div style="display: flex;flex-direction: row;justify-content: space-between;">
                            <!--use-->
                            <div style="min-width: 36%;">
                                <div>
                                    <t-card title="设备信息区块" style="margin: 0px 0px 13px;">
                                        <span v-if="eqinfo == ''">暂无数据</span>
                                        <span v-else>{{ eqinfo }}</span>
                                    </t-card>
                                </div>
                                <!-- <div>
                                  <t-checkbox v-model="checkboxvalue" :onChange="changecheckbox">批量模式</t-checkbox>
                                </div> -->
                                <div style="display: flex;align-items: center;margin: 5px 0px 12px;"
                                    class="helpotheruserlend_big">
                                    <t-checkbox class="helpotheruserlend_box" v-model="checkboxuservalue">帮借/转借</t-checkbox>
                                    <div style="display: flex;">
                                        <t-input :disabled="!checkboxuservalue" class="helpotheruserlend_input"
                                            placeholder="使用者Code" size="small" v-model="usercodes"
                                            style="margin: 0px 10px 0px 12px;" />
                                    </div>
                                    <t-tag theme="warning" variant="light-outline">
                                        <template #icon>
                                            <t-icon name="error-circle" />
                                        </template>
                                        只有管理员才可以帮借/转借!
                                    </t-tag>
                                </div>
                                <!---->
                                <!-- <div>
                                    <div style="display: flex;align-items: center;">
                                        <span class="bitian">*</span>
                                        <span
                                            style="color: var(--td-text-color-primary);font: var(--td-font-body-medium)">借出原因:
                                        </span>
                                        <t-input style="width: 181px;margin-left: 10px;" placeholder="请输入"
                                            v-model="lendeqcodeyyvalue"></t-input>
                                        <t-button variant="dashed" @click="showtaskbind = true">任务绑定</t-button>
                                        <t-tag theme="danger" variant="light-outline" style="margin-left: 10px;">
                                            <template #icon>
                                                <t-icon name="error-circle" />
                                            </template>
                                            Test Function!
                                        </t-tag>
                                    </div>
                                </div> -->
                                <!---->
                                <div style="margin-top: 13px;">
                                    <div style="display: flex;align-items: center;">
                                        <span class="bitian">*</span>
                                        <span
                                            style="color: var(--td-text-color-primary);font: var(--td-font-body-medium)">设备Code:
                                        </span>
                                        <t-input style="width: 181px;margin-left: 10px;" class="lendinput" ref="lendinput"
                                            placeholder="请输入" v-model="lendeqcodevalue" :onEnter="newlend" :autofocus="true"
                                            :oninput="requesteqinfo(lendeqcodevalue)"></t-input>
                                        <t-button class="lendbutton" style="margin-left: -10px;z-index: 2;"
                                            @click.end="newlend">借出</t-button>
                                    </div>
                                    <!-- <div style="width: 450px;height: 100px;background: var(--td-bg-color-page);"></div> -->
                                </div>
                            </div>
                            <!--INFO-->
                            <div>
                                <t-card title="本次借出设备列表">
                                    <div style="display: flex;flex-direction: row;align-items: center;">
                                        <t-table :data="thistime_lend_table_data"
                                            :columns="thistime_lend_table_topic"></t-table>
                                    </div>
                                </t-card>
                            </div>
                        </div>
                        <!--Button-->
                        <!-- <div style="margin-top: 16px;">
                            <t-button block @click="lend">借出</t-button>
                        </div> -->
                    </div>
                </t-tab-panel>
                <t-tab-panel value="second">
                    <template #label><span class="returntap"> <t-icon name="login"
                                class="tabs-icon-margin" />归还</span></template>
                    <div id="returnpage">
                        <div style="display: flex;flex-direction: row;justify-content: space-between;">
                            <!--use-->
                            <div class="returnview" style="min-width: 36%;">
                                <!---->
                                <div style="display: flex;align-items: center;margin: 5px 0px 12px;">
                                    <t-checkbox v-model="checkboxuservalue">帮还</t-checkbox>
                                    <div style="display: flex;">
                                        <t-input :disabled="!checkboxuservalue" placeholder="归还者Code" size="small"
                                            v-model="retusercodes" style="margin: 0px 10px 0px 12px;" />
                                    </div>
                                    <t-tag theme="warning" variant="light-outline">
                                        <template #icon>
                                            <t-icon name="error-circle" />
                                        </template>
                                        只有管理员才可以帮还!
                                    </t-tag>
                                </div>
                                <!---->
                                <div>
                                    <div style="display: flex;align-items: center;">
                                        <span class="bitian">*</span>
                                        <span
                                            style="color: var(--td-text-color-primary);font: var(--td-font-body-medium)">设备Code:
                                        </span>
                                        <t-input style="width: 181px;margin-left: 10px;" :autofocus="true" placeholder="请输入"
                                            ref="returninput" v-model="reteqcodevalue" :onEnter="reteqcodeinput"
                                            :oninput="reteqcodevalue = reteqcodevalue.replace(/\s*/g, '')"></t-input>
                                        <t-button class="returnbutton" style="margin-left: -10px;z-index: 2;"
                                            @click.end="reteqcodeinput()">归还</t-button>
                                    </div>
                                    <!-- <div style="width: 450px;height: 100px;background: var(--td-bg-color-page);"></div> -->
                                </div>
                                <!---->
                            </div>
                            <!--INFO-->
                            <div>
                                <t-card title="本次归还设备列表">
                                    <div style="display: flex;flex-direction: row;align-items: center;">
                                        <t-table :data="thistime_retu_table_data"
                                            :columns="thistime_retu_table_topic"></t-table>
                                    </div>
                                </t-card>
                            </div>
                        </div>
                    </div>
                </t-tab-panel>
            </t-tabs>
        </div>
    </div>
    <!--【TEST】Task bind【任务绑定】-->
    <t-dialog :visible="showtaskbind" header="任务绑定" width="60%" placement="center" :onClose="close_task_binddialog">
        <Taskbind></Taskbind>
        <template #footer>
            <div>
                <span>
                    找不到任务？->
                    <span>
                        <a href="javascript:void(1)" class="a-brand-color-5" @click="cant_find_task__need_issue">发布任务</a>
                    </span>
                </span>
            </div>
        </template>
    </t-dialog>
    <t-dialog id="nav_to_task_issue_confirmdialog" :visible="showconfirmdialog" header="操作确认" cancelBtn="我要继续我的操作"
        :closeBtn="false" :onClose="close_nav_to_task_issue_confirmdialog">
        <template #confirmBtn>
            <t-button theme="danger" @click="nav_to_task_issue">确认操作</t-button>
        </template>
        <div>
            将要执行“任务发布”操作。该操作将清空该页面已完成的操作(设备列表将清空)，是否继续？
        </div>
    </t-dialog>
    <!---->
    <t-loading :loading="loading" text="加载中..." fullscreen />
    <!--引导使用-->
    <t-guide v-model="current" :steps="steps" @change="handleChange" @finish="handleFinish" :onSkip="guide_skip"
        :finishButtonProps="{ content: Math.floor(Math.random() * 2) == 1 ? '我已经知道怎么使用这些功能，且保证正确、规范的使用这些功能！' : '哇嘎哒！！', theme: 'primary' }" />
    <!--音频-->
    <audio ref="lendmedia" :src="lendm" hidden controls="lend"></audio>
    <audio ref="returnmedia" :src="returnm" hidden controls="return"></audio>
</template>

<script setup>
import { ref } from 'vue';

const visible = ref(false);

const lendinput = ref(null);
const returninput = ref(null);

const steps = [
    {
        element: '.guide_more',
        title: '新手引导',
        body: '这是更多，点击它会弹出更多选项',
        placement: 'bottom-right',
    },
    {
        element: '.changepws',
        title: '新手引导',
        body: '点击这里可以修改密码',
        placement: 'right',
    },
    {
        element: '.moreinfo',
        title: '新手引导',
        body: '点击这里显示更多信息',
        placement: 'right',
    },
    {
        element: '.clogout',
        title: '新手引导',
        body: '点击这里退出登录',
        placement: 'right',
    },
    {
        element: '.guide_refresh',
        title: '新手引导',
        body: '这里是刷新按钮，点击它将会刷新整个页面',
        placement: 'bottom-right',
    },
    {
        element: '.guide_darktoggle',
        title: '新手引导',
        body: '这里可以在浅色和深色模式中切换',
        placement: 'bottom-right',
    },
    {
        element: '.lendtap',
        title: '新手引导',
        body: '点击这里显示借出界面',
        placement: 'bottom-left',
    },
    {
        element: '.returntap',
        title: '新手引导',
        body: '点击这里显示归还界面',
        placement: 'bottom-left',
    },
    {
        element: '.helpotheruserlend_big',
        title: '新手引导',
        body: '这里是帮借区域',
        placement: 'top',
    },
    {
        element: '.helpotheruserlend_box',
        title: '新手引导',
        body: '需要帮姐首先要这里打开选项开关',
        placement: 'top-left',
    },
    {
        element: '.helpotheruserlend_input',
        title: '新手引导',
        body: '然后在这里填写使用人的code',
        placement: 'top',
    },
    {
        element: '.lendinput',
        title: '新手引导',
        body: '要借出的设备code填这里',
        placement: 'top',
    },
    {
        element: '.lendbutton',
        title: '新手引导',
        body: '然后点击这里借出',
        placement: 'top-left',
    },
    {
        element: '.returnview',
        title: '新手引导',
        body: '归还也是大同小异',
        placement: 'left',
    },
];

const handlePrevStepClick = ({ e, prev, current, total }) => {
    console.log(e, prev, current, total);
};

const handleNextStepClick = ({ e, next, current, total }) => {
    console.log(e, next, current, total);
};

// const value = ref('topic');
const theme = ref('normal');

</script>

<script>
import { MessagePlugin } from 'tdesign-vue-next';
import Taskbind from '../Task/bind.vue';
import { ErrorCircleFilledIcon, CheckCircleFilledIcon, CloseCircleFilledIcon } from 'tdesign-icons-vue-next';
import lendmmmm from '@/assets/media/借出成功.mp3'
import rettmmmm from '@/assets/media/归还成功.mp3'

//
export default {
    name: 'lEnd',
    components: {
        Taskbind
    },
    expose: ['current'],
    data() {
        return {
            checkboxuservalue: false,//帮借
            lendeqcodevalue: '',//设备码
            // lendeqcodeyyvalue: '',//借出原因
            usercodes: '',//帮借转借人
            eqinfo: '',//显示信息
            usercode: '',//cookie
            username: '',//cookie
            reteqcodevalue: '',
            retusercodes: '',
            loading: false,
            //test function
            // showtaskbind: false,
            // showconfirmdialog: false,
            //media
            lendm: lendmmmm,
            returnm: rettmmmm,
            //thistimelendlist
            thistime_lend_table_topic: [
                { colKey: 'eqname', title: '设备名称', width: '250' },
                { colKey: 'eqcode', title: '设备Code', width: '150' },
                {
                    colKey: 'status',
                    title: '借出状态',
                    width: '150',
                    cell: (h, { row }) => {
                        return (
                            <t-tag shape="round" theme={row.status.theme} variant="light-outline">
                                {row.status.icon}
                                {row.status.text}
                            </t-tag>
                        );
                    },
                },
                { colKey: 'user', title: '借出人' },
                { colKey: 'dothisthinguser', title: '操作人' },
                { colKey: 'lendtime', title: '借出时间', ellipsis: true },
                { colKey: 'more', title: '备注' },
            ],
            thistime_lend_table_data: [],
            thistime_retu_table_topic: [
                { colKey: 'eqname', title: '设备名称', width: '250' },
                { colKey: 'eqcode', title: '设备Code', width: '150' },
                {
                    colKey: 'status',
                    title: '归还状态',
                    width: '150',
                    cell: (h, { row }) => {
                        return (
                            <t-tag shape="round" theme={row.status.theme} variant="light-outline">
                                {row.status.icon}
                                {row.status.text}
                            </t-tag>
                        );
                    },
                },
                { colKey: 'user', title: '归还人' },
                { colKey: 'lendtime', title: '归还时间', ellipsis: true },
                { colKey: 'more', title: '备注' },
            ],
            thistime_retu_table_data: [],
            showmask: true,
            //
            current: -1,
            guide_last_choose: 0,
            //tabs
            tabsvalue: 'first'
        }
    },
    mounted() {
        var uucode = this.getck("usercode")
        var uuname = this.getck("username")
        this.$data.username = uuname
        this.$data.usercode = uucode
        if (this.getck("need_change_password") == "need") {
            return
        }
        else {
            setTimeout(() => {
                this.$data.current = 0
            }, 1500);
        }
    },
    methods: {
        //引导
        handleChange(current) {
            if (current == 1 && this.guide_last_choose == 0) {
                this.$data.current = 0
                document.getElementById("moremenu").classList = "menu menushow"
                setTimeout(() => {
                    this.$data.current = 1
                }, 400);
            }
            if (current == 3 && this.guide_last_choose == 4) {
                this.$data.current = this.$data.guide_last_choose
                document.getElementById("moremenu").classList = "menu menushow"
                setTimeout(() => {
                    this.$data.current = 3
                }, 400);
            }
            if (current == 4) {
                document.getElementById("moremenu").classList = "menu"
            }
            if (current == 13 && this.guide_last_choose == 12) {
                this.$data.tabsvalue = 'second'
            }
            console.log(current)
            if (current == 12 && this.guide_last_choose == 13) {
                this.$data.tabsvalue = 'first'
            }
            this.$data.guide_last_choose = current
        },
        //guide完成
        handleFinish() {
            this.$data.tabsvalue = 'first'
            this.$refs.lendinput.focus()
        },
        //guide跳过
        guide_skip(e) {
            if (e.current >= 1 && e.current < 4) {
                document.getElementById("moremenu").classList = "menu"
            }
        },
        //tabs
        handlerChange(newValue) {
            this.$data.tabsvalue = newValue
        },

        //输入设备代码，查询
        eqcodeinput(a) {
            this.$refs.returnmedia.currentTime = 0;
            this.$refs.returnmedia.play()
        },

        changecheckbox(a) {
            console.log(a)
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

        /**
        * @requesteqinfo
        * @desc 请求设备信息
        * @param
        */
        requesteqinfo(a) {
            this.$data.lendeqcodevalue = this.$data.lendeqcodevalue.replace(/\s*/g, "")
            var loginurl = 'http://10.3.146.103/equipment/' + a
            const xhr = new XMLHttpRequest()
            xhr.open('get', loginurl, true)
            xhr.timeout = 3000;
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
            xhr.da
            xhr.withCredentials = false;
            xhr.ontimeout = () => {
                xhr.abort()
                this.showMessage('warning', 3000, '【获取设备信息】请求超时')
            }
            xhr.onload = () => {
                if (xhr.status == 200) {
                    this.$data.eqinfo = xhr.response
                    // var resall = xhr.response.split(' ')
                    // var bianhao = resall[0].split(/编号:/)[1]
                    // var shebeicode = resall[1].split(/Code:/)[1]
                    // var shebeiname = resall[2].split(/设备名称:/)[1]
                    // var xinghao = resall[3].split(/型号:/)[1]
                    // var guishu = resall[4].split(/归属:/)[1]
                    // var sn = resall[5].split(/SN码:/)[1]

                    // // console.log(resall, bianhao, shebeicode, shebeiname, xinghao, guishu, sn)
                    // var aaa = { "id": bianhao, "eqcode": shebeicode, "eqname": shebeiname, "eqsn": sn, "eqasc": guishu, "eqmodel": xinghao, "type": "primary" }
                    // this.$data.list.push(aaa)
                    // this.$data.haseqidlist.push(shebeicode)
                }
                else {
                    this.$data.eqinfo = "暂无数据"
                }
            }
            xhr.onerror = () => {
                console.warn('请求出现了一个错误!')
                this.$data.eqinfo = ""
                this.showMessage('warning', 5000, '请求出错')
            }
            xhr.send()
        },

        /**
        * @searcheqlistinfo
        * @desc 搜索是否在列表内
        * @param
        */
        searcheqlistinfo(e) {
            var re = this.haseqidlist
            if (re.length == 0) {
                return false
            }
            else {
                for (let iiiiiii = 0; iiiiiii <= re.length; iiiiiii++) {
                    const element = this.haseqidlist[iiiiiii];
                    if (e == element) {
                        return true
                    }
                }
            }
        },

        //获取单个cookies
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
                console.log('没有cookie')
            }
        },

        /**
         * @newlend
         * @desc 借出主函数
         */
        newlend() {
            //Update:20230304
            //开启加载蒙版

            this.$data.loading = true
            //Ver
            var key = this.getck("key")
            var eqcode = this.$data.lendeqcodevalue
            if (eqcode == "") {
                console.warn("【借出失败：Unknown Code】")
                this.showMessage('error', 5000, '借出失败：无效的设备名')
                this.$data.loading = false
                return false
            }
            var loginuser = this.getck("usercode")
            var usercode
            if (this.$data.checkboxuservalue) {
                usercode = this.$data.usercodes
            }
            else {
                usercode = loginuser
            }

            //key是否存在
            if (key) {
                this.$data.loading = true
                //检查一下key时效性
                const xhr = new XMLHttpRequest()
                xhr.open('post', 'http://10.3.146.103/json/key/check', true)
                //正经返回数据
                //{"data":{"admin":0,"class":"\u57ce\u8f68221","login":"yes","name":"\u8d75\u6dd1\u83b9","password":"123456","usercode":"cg22150"},"errcode":0,"errmsg":"ok"}
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
                xhr.da
                xhr.timeout = 3000
                xhr.ontimeout = () => {
                    xhr.abort()
                    this.$data.loading = false
                    this.showMessage('warning', 5000, '请求超时')
                }
                xhr.onload = () => {
                    console.group('【Key验证】')
                    this.$data.loading = false
                    //去除回车、空格等一些空的占位符
                    var result = JSON.parse(xhr.response.replace(/\r|\n/ig, ""));
                    //key无效
                    if (result.status == -1003) {
                        console.error('Key失效')
                        console.groupEnd()
                        //key超时
                        const content = () => {
                            return (
                                <div>
                                    登录失效，请重新登陆。
                                </div>
                            );
                        };
                        MessagePlugin.error({ content: content, duration: 3000 })
                    }
                    else if (result.status == 0) {
                        this.$data.loading = true
                        console.log('Key处于时效内')
                        console.groupEnd()
                        console.group('【借出】')
                        //检查完毕，开始借出
                        const xhr2 = new XMLHttpRequest()
                        xhr2.open('post', 'http://10.3.146.103/json/equipment/lend', true)
                        xhr.timeout = 3000
                        xhr.ontimeout = () => {
                            xhr.abort()
                            this.$data.loading = false
                            this.showMessage('warning', 3000, '借出失败：请求超时')
                        }
                        xhr2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
                        xhr2.da
                        xhr2.onload = () => {
                            this.$data.loading = false
                            var res = JSON.parse(xhr2.response)
                            //还原输入框
                            this.$data.lendeqcodevalue = ""
                            if (xhr2.status == 500) {
                                //服务端错误，一般是找不到该设备
                                console.error('【借出失败：找不到该设备】')
                                this.showMessage("error", 5000, "借出失败：找不到该设备！")
                            }
                            if (res.errcode == 0) {
                                console.log('【借出成功】')
                                this.showMessage("success", 3000, "借出登记完成")
                                this.$refs.lendmedia.currentTime = 0;
                                this.$refs.lendmedia.play()
                            }
                            else if (res.errcode == -1003) {
                                console.error('【借出失败：Key失效】')
                                this.showMessage("error", 5000, "借出失败：登陆失效，请重新登录")
                            }
                            else if (res.errcode == -3001) {
                                console.error('【借出失败：找不到该用户】')
                                this.showMessage("error", 5000, "借出失败：找不到该用户！")
                            }
                            else if (res.errcode == -3002) {
                                console.error('【借出失败：找不到该设备】')
                                this.showMessage("error", 5000, "借出失败：找不到该设备！")
                            }
                            else if (res.errcode == -3003) {
                                console.error('【借出失败：用户没有权限为别人借出设备】')
                                this.showMessage("error", 5000, "借出失败：无权限为别人借出设备！")
                            }
                            else if (res.errcode == -3004) {
                                console.error('【借出失败：该设备已经登记过借出！】')
                                this.showMessage("error", 5000, "借出失败：该设备已被借出")
                            }
                            else {
                                this.showMessage("error", 5000, "借出失败：" + res.errmsg)
                            }
                            console.groupEnd()
                            var myDate = new Date();
                            var y = myDate.getFullYear();    //获取完整的年份(4位,1970-????)
                            var m = myDate.getMonth() + 1;       //获取当前月份(0-11,0代表1月)
                            var d = myDate.getDate();        //获取当前日(1-31)
                            var h = myDate.getHours();       //获取当前小时数(0-23)
                            var mi = myDate.getMinutes();     //获取当前分钟数(0-59)
                            var s = myDate.getSeconds();     //获取当前秒数(0-59)
                            if (h >= 0 && h <= 9) {
                                h = "0" + h;
                            }
                            if (m >= 1 && m <= 9) {
                                m = "0" + m;
                            }
                            if (d >= 1 && d <= 9) {
                                d = "0" + d;
                            }
                            if (mi >= 0 && mi <= 9) {
                                mi = "0" + mi;
                            }
                            //写入表格
                            var abc = {
                                eqname: res.data.lendname,
                                eqcode: eqcode,
                                //
                                status: {
                                    text: res.errcode == 0 ? '借出成功' : '借出失败',
                                    theme: res.errcode == 0 ? 'success' : 'danger',
                                    icon: res.errcode == 0 ? <CheckCircleFilledIcon /> : <CloseCircleFilledIcon />,
                                },
                                user: res.data.lenduser,
                                lendtime: y + '-' + m + '-' + d + ' ' + h + ':' + mi + ':' + s,
                                dothisthinguser: this.$data.username,
                                more: res.errmsg == 'ok' ? '' : res.errmsg
                            }
                            this.$data.thistime_lend_table_data.unshift(abc)
                        }
                        xhr2.send("key=" + key + "&user=" + usercode + "&code=" + eqcode)

                    }
                }
                xhr.send('key=' + key)
            }
            else {
                const content = () => {
                    return (
                        <div>
                            【Error】错误的登录态。
                        </div>
                    );
                };
                MessagePlugin.error({ content: content, duration: 3000 })
            }

        },

        /**
         * @reteqcodeinput
         * @desc 归还主函数
         */
        reteqcodeinput() {
            this.$data.loading = true
            var user
            var code = this.$data.reteqcodevalue //归还设备
            if (code == "") {
                console.warn("【归还失败：Unknown Code】")
                this.showMessage('error', 5000, '归还失败：无效的设备名')
                this.$data.loading = false
                return false
            }
            var key = this.getck("key")
            if (this.$data.checkboxuservalue) {
                user = this.$data.retusercodes
            }
            else {
                user = this.$data.usercode
            }

            const xhr = new XMLHttpRequest()
            xhr.open('post', 'http://10.3.146.103/json/equipment/return', true)
            xhr.timeout = 3000;
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
            xhr.da
            xhr.withCredentials = false;
            xhr.ontimeout = () => {
                xhr.abort()
                this.$data.loading = false
                this.showMessage('warning', 5000, '请求超时')
            }
            xhr.onerror = () => {
                this.$data.loading = false
                console.warn('请求出现了一个错误!')
                this.showMessage('warning', 5000, '请求出错')
            }
            xhr.onload = () => {
                this.$data.loading = false
                var res = JSON.parse(xhr.response)
                console.group("【归还】")
                if (res.errcode == -1003) {
                    console.warn("【归还失败：Key过期】")
                    this.showMessage('error', 5000, '归还失败：登录失效，请重新登录')
                }
                else if (res.errcode == -3006) {
                    console.warn("【归还失败：找不到该设备】")
                    this.showMessage('error', 5000, '归还失败：找不到该设备')
                }
                else if (res.errcode == -3005) {
                    console.warn("【归还失败：找不到该用户】")
                    this.showMessage('error', 5000, '归还失败：找不到该用户')
                }
                else if (res.errcode == -3007) {
                    console.warn("【归还失败：没有权限为别人归还设备】")
                    this.showMessage('error', 5000, '归还失败：你没有权限为别人归还设备')
                }
                else if (res.errcode == -3008) {
                    console.warn("【归还失败：该设备已经登记归还】")
                    this.showMessage('warning', 3000, '归还失败：该设备已登记归还')
                }
                else if (res.errcode == 0) {
                    console.warn("【归还成功】")
                    this.showMessage('success', 3000, '归还成功')
                    this.$refs.returnmedia.currentTime = 0;
                    this.$refs.returnmedia.play()
                }
                console.groupEnd()
                var myDate = new Date();
                var y = myDate.getFullYear();    //获取完整的年份(4位,1970-????)
                var m = myDate.getMonth() + 1;       //获取当前月份(0-11,0代表1月)
                var d = myDate.getDate();        //获取当前日(1-31)
                var h = myDate.getHours();       //获取当前小时数(0-23)
                var mi = myDate.getMinutes();     //获取当前分钟数(0-59)
                var s = myDate.getSeconds();     //获取当前秒数(0-59)
                if (h >= 0 && h <= 9) {
                    h = "0" + h;
                }
                if (m >= 1 && m <= 9) {
                    m = "0" + m;
                }
                if (d >= 1 && d <= 9) {
                    d = "0" + d;
                }
                if (mi >= 0 && mi <= 9) {
                    mi = "0" + mi;
                }
                //写入表格
                var abc = {
                    eqname: res.data.returnname,
                    eqcode: code,
                    //
                    status: {
                        text: res.errcode == 0 ? '归还成功' : '归还失败',
                        theme: res.errcode == 0 ? 'success' : 'danger',
                        icon: res.errcode == 0 ? <CheckCircleFilledIcon /> : <CloseCircleFilledIcon />,
                    },
                    user: this.$data.username,
                    lendtime: y + '-' + m + '-' + d + ' ' + h + ':' + mi + ':' + s,
                    more: res.errmsg == 'ok' ? '' : res.errmsg
                }
                this.$data.thistime_retu_table_data.unshift(abc)
            }
            xhr.send("key=" + key + "&user=" + user + "&code=" + code)
            this.$data.reteqcodevalue = ""
        },


        /** */
        // cant_find_task__need_issue() {
        //     //关闭绑定任务的弹窗
        //     this.$data.showtaskbind = false
        //     this.$data.showconfirmdialog = true
        // },

        // nav_to_task_issue() { location.href = location.pathname + "?type=issue&from=taskbind&why=cant_find_task&do=createtask" },
        // close_task_binddialog() { this.$data.showtaskbind = false },
        // close_nav_to_task_issue_confirmdialog() { this.$data.showconfirmdialog = false },
    },

}
</script>

<style>
#lendpage,
#returnpage {
    margin-top: 10px;
    background: var(--td-bg-color-container);
}

.t-tabs__operations--left{
    display: none !important;
}
.t-tabs__operations--right{
    display: none !important;
}

.t-card__body {
    padding-top: 0px !important;
}

.bitian {
    margin-right: 3px;
    color: var(--td-error-color);
}

.r-run {
    height: 10px;
    width: 10px;
    border-radius: 50%;
    margin-right: 8px;
}

.r-run--success {
    background: var(--td-success-color);
}

.r-run--danger {
    background: var(--td-error-color);
}

.r-run--warning {
    background: var(--td-warning-color);
}

.r-run--primary {
    background: var(--td-brand-color);
}

/** */

.a-brand-color-5 {
    color: var(--td-brand-color-5);
    text-decoration: none;
}

.a-brand-color-5:active {
    color: var(--td-brand-color-5);
    text-decoration: none;
}

.a-brand-color-5:hover {
    color: var(--td-brand-color-5);
    text-decoration: none;
}
</style>
