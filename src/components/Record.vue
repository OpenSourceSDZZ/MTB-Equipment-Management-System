<template>
    <div id="top" v-if="!noadmin">
        <div style="display: flex;flex-direction: row;justify-content: space-between;margin-top: 16px;">
            <div>
                <t-button theme="primary" @click="add_eq('新增设备'), dialogFormVisible = true" style="margin-right: 10px;">
                    <icon name="add" size="16px" />添加
                </t-button>
                <t-button theme="danger" :disabled="pldelclick">
                    <icon name="delete" size="16px" />批量删除
                </t-button>
            </div>
            <div style="display: flex;">
                <div style="width:200px;margin-right:10px;">
                    <t-select :value="selectvalue" :onChange="searchselectonChange">
                        <t-option key="1" label="通过设备Code搜索" value="1" />
                        <t-option key="2" label="通过借出人搜索" value="2" />
                        <t-option key="3" label="通过归还人搜索" value="3" />
                        <t-option key="4" label="通过借出日期搜索" value="4" />
                        <t-option key="5" label="通过归还日期搜索" value="5" />
                        <t-option key="6" label="通过状态搜索" value="6" />
                    </t-select>
                </div>
                <div style="width:400px;">
                    <t-input placeholder="搜索" :onChange="searchInput" v-model="searchinputvalue">
                        <template #prefix-icon>
                            <icon name="search" size="16px" />
                        </template>
                    </t-input>
                </div>
            </div>
        </div>
        <t-loading v-if="tablealready == false && searchtablealready == false" style="display: flex;margin-top: 80px;" />
        <!--main table-->
        <t-table row-key="id" :columns="columns" :data="tableData" :selectedRowKeys="selectedRowKeys"
            @select-change="rehandleSelectChange"
            :pagination="{ defaultCurrent: 1, defaultPageSize: 20, pageSizeOptions: [20, 30, 40, 50], total: tableData.length, }"
            :loading="tablelodingshow" v-if="tablealready == true && searchtablealready == false">
            <template #op-column>
                <p>操作</p>
            </template>
            <template #op="slotProps">
                <t-button variant="outline" theme="primary"
                    @click="rehandleClickedit(slotProps), dialogFormVisible = true, edit_dialog_title = '编辑设备信息'"
                    style="margin-left:-16px">编辑</t-button>
                <t-popconfirm theme="danger" content="确认删除吗" :onConfirm="onVisibleChange">
                    <t-button theme="danger" style="margin-left:16px">
                        <icon name="delete" size="16px" />删除
                    </t-button>
                </t-popconfirm>

            </template>
        </t-table>

        <!--search table-->
        <t-table row-key="id" :columns="searchcolumns" :data="searchtableData"
            v-model:selectedRowKeys="searchselectedRowKeys" @select-change="searchrehandleSelectChange"
            :pagination="{ defaultCurrent: 1, defaultPageSize: 20, pageSizeOptions: [20, 30, 40, 50], total: searchtableData.length, }"
            :loading="tablelodingshow" v-if="tablealready == false && searchtablealready == true">
            <template #op-column>
                <p>操作</p>
            </template>
            <template #op="slotProps">
                <t-button variant="outline" theme="primary"
                    @click="rehandleClickedit(slotProps), dialogFormVisible = true, edit_dialog_title = '编辑设备信息'"
                    style="margin-left:-16px">编辑</t-button>
                <t-popconfirm theme="danger" content="确认删除吗" :onConfirm="onVisibleChange">
                    <t-button theme="danger" style="margin-left:16px">
                        <icon name="delete" size="16px" />删除
                    </t-button>
                </t-popconfirm>

            </template>
        </t-table>
        <!--error table-->
        <span v-if="!tableData">表格出错，请刷新页面</span>
        <!--删除用户确认框-->
        <!-- <el-dialog v-model="centerDialogVisible" title="警 告" width="30%" center>
          <span>
              将要删除这个用户，确认删除？
          </span>
          <template #footer>
              <span class="dialog-footer">
                  <el-button @click="centerDialogVisible = false" type="primary" plain>我按错了</el-button>
                  <el-button type="danger" @click="centerDialogVisible = false">
                      是的，删除
                  </el-button>
              </span>
          </template>
      </el-dialog> -->

        <!--<div style="margin-top: 20px">
          <el-button @click="toggleSelection([tableData[1], tableData[2]])">切换第二、第三行的选中状态</el-button>
          <el-button @click="toggleSelection()">取消选择</el-button>
      </div>-->

        <!--弹出层-->


        <!--编辑信息弹出框-->
        <t-dialog v-model="dialogFormVisible" :title="edit_dialog_title" style="">
            <t-form :model="form" :rules="rules" ref="formRef" id="formlist">
                <t-form-item label="ID" :label-width="formLabelWidth" required>
                    <t-input v-model="form.id" autocomplete="off" disabled />
                </t-form-item>
                <t-form-item label="设备Code" :label-width="formLabelWidth" :required="add_from_mode" prop="eqcode">
                    <t-input v-model="form.eqcode" autocomplete="off" />
                </t-form-item>
                <t-form-item label="设备名" :label-width="formLabelWidth" :required="add_from_mode" prop="eqname">
                    <t-input v-model="form.eqname" autocomplete="off" />
                </t-form-item>
                <t-form-item label="归属" :label-width="formLabelWidth" prop="ascription">
                    <t-input v-model="form.ascription" autocomplete="off" />
                </t-form-item>
                <t-form-item label="SN" :label-width="formLabelWidth" prop="sn">
                    <t-input v-model="form.sn" autocomplete="off" />
                </t-form-item>
                <t-form-item label="型号" :label-width="formLabelWidth" prop="model">
                    <t-input v-model="form.model" autocomplete="off" />
                </t-form-item>
            </t-form>
            <template #footer>
                <span class="dialog-footer">
                    <t-button variant="outline" theme="default" @click="dialogFormVisible = false"
                        style="margin-right: 15px;">取消</t-button>
                    <t-button theme="primary" @click="dialogFormVisible = false, onSubmit()">完成，保存</t-button>
                </span>
            </template>
        </t-dialog>

        <div style="width: 600px;position: fixed;left: 0;right: 0;margin: 0 auto;margin-top: 40px;">
            <el-alert show-icon='true' type="error" :title="alert_title" :description="alert_desc" v-show="alert_show"
                @click="alertclick">
            </el-alert>
        </div>



    </div>
    <div v-if="noadmin">
        <h1>您没有管理员权限</h1>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { Icon } from 'tdesign-icons-vue-next';
import { NotifyPlugin } from 'tdesign-vue-next';

const columns = [
    {
        colKey: 'row-select',
        type: 'multiple',
        align: 'left',
        // 禁用行选中方式一：使用 disabled 禁用行（示例代码有效，勿删）。disabled 参数：{row: RowData; rowIndex: number })
        // 这种方式禁用行选中，当前行会添加行类名 t-table__row--disabled，禁用行文字变灰
        // disabled: ({ rowIndex }) => rowIndex === 1 || rowIndex === 3,

        // 禁用行选中方式二：使用 checkProps 禁用行（示例代码有效，勿删）
        // 这种方式禁用行选中，行文本不会变灰
        //checkProps: ({ rowIndex }) => ({ disabled: rowIndex % 2 !== 0 }),
        width: 10,
    },
    { colKey: 'id', title: 'ID', align: 'center', width: 50 },
    {
        colKey: 'eqcode',
        title: '设备code',
        width: 60,
    },
    { colKey: 'usercode', title: '借出者', width: 50 },
    { colKey: 'returnuser', title: '归还者', align: 'left', width: 70 },
    { colKey: 'date', title: '借出日期', align: 'left', width: 90 },
    { colKey: 'returndate', title: '归还日期', align: 'left', width: 90 },
    { colKey: 'status', title: '状态', align: 'left', width: 80 },
    {
        colKey: 'do',
        width: 400,
        title: '操作',
        cell: 'op',
        align: 'left',
    },
];

const searchcolumns = [
    {
        colKey: 'row-select',
        type: 'multiple',
        align: 'left',
        // 禁用行选中方式一：使用 disabled 禁用行（示例代码有效，勿删）。disabled 参数：{row: RowData; rowIndex: number })
        // 这种方式禁用行选中，当前行会添加行类名 t-table__row--disabled，禁用行文字变灰
        // disabled: ({ rowIndex }) => rowIndex === 1 || rowIndex === 3,

        // 禁用行选中方式二：使用 checkProps 禁用行（示例代码有效，勿删）
        // 这种方式禁用行选中，行文本不会变灰
        //checkProps: ({ rowIndex }) => ({ disabled: rowIndex % 2 !== 0 }),
        width: 10,
    },
    { colKey: 'id', title: 'ID', align: 'center', width: 50 },
    {
        colKey: 'eqcode',
        title: '设备code',
        width: 60,
    },
    { colKey: 'usercode', title: '借出者', width: 50 },
    { colKey: 'returnuser', title: '归还者', align: 'left', width: 70 },
    { colKey: 'date', title: '借出日期', align: 'left', width: 90 },
    { colKey: 'returndate', title: '归还日期', align: 'left', width: 90 },
    { colKey: 'status', title: '状态', align: 'left', width: 80 },
    {
        colKey: 'do',
        width: 400,
        title: '操作',
        cell: 'op',
        align: 'left',
    },
];


const onVisibleChange = (e) => {
    console.log('点击确认：', e)
};


</script>

<script>
import { reactive } from 'vue';
// import Axios from 'axios';
//import sha256 from 'js-sha256';


/////
// NotifyPlugin.error({ title: '错误', content: '没有内容' })
/////
let selectedRowKeys = ref([]);
let searchselectedRowKeys = ref([]);

const api1 = 'http://10.3.146.103/json/record/list'

export default {
    name: 'ReCord',
    setup() {
        const rules = reactive({
            eqcode: [
                { message: '请输入设备code', trigger: 'blur' },
                { min: 0, max: 10, message: '设备code不能大于10位', trigger: 'blur' },
            ],
            eqname: [
                { message: '请输入设备名', trigger: 'blur' },
                { min: 0, max: 100, message: '请输入正确的设备名', trigger: 'blur' },
            ],
            ascription: [
                { message: '请输入设备归属', trigger: 'blur' },
                { min: 0, max: 50, message: '这个设备归属好像有点问题？', trigger: 'blur' },
            ],
            sn: [
                { message: '请输入设备sn码(序列号)', trigger: 'blur' },
                { min: 0, max: 200, message: '这个sn码(序列号)好像有点问题？', trigger: 'blur' },
            ],
            model: [
                { message: '请输入设备型号', trigger: 'blur' },
                { min: 0, max: 100, message: '这个设备型号好像有点问题？', trigger: 'blur' },
            ],
        });
        return {
            rules,
        }

    },
    data() {
        return {
            tableData: [],
            searchtableData: [{}],
            searchtablealready: false,
            tableDatabackup: [],//备份
            tablealready: false,
            multipleSelection: [],
            result1: 'none',
            currentPage: 1,
            centerDialogVisible: false,//删除用户确认框
            dialogFormVisible: false,//编辑信息弹出框
            form: {
                eqcode: '',
                eqname: '',
                ascription: '',
                id: 0,
                sn: '',
                model: '',
            },
            formLabelWidth: '120px',
            formLabelWidth2: '150px',
            edit_dialog_title: '编辑设备信息',
            from_dialog_mode: 0,
            add_from_mode: false,
            //Alert
            alert_title: 'None',
            alert_desc: 'None',
            alert_show: false,
            selectvalue: '1',
            searchinputvalue: '',
            pldelclick: true,
            NotifyPlugin,
            //
            noadmin: false,
        }
    },
    mounted() {
        if (this.getck('admin') == '1') {
            this.$data.noadmin = false
            var key = this.getck('key')
            var that = this;
            const xhr = new XMLHttpRequest()
            xhr.open('post', api1, true)
            //正经返回数据
            //{"data":{"admin":0,"class":"\u57ce\u8f68221","login":"yes","name":"\u8d75\u6dd1\u83b9","password":"123456","usercode":"cg22150"},"errcode":0,"errmsg":"ok"}
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
            xhr.da
            xhr.onload = () => {
                var result = JSON.parse(xhr.response.replace(/\r|\n/ig, ""));
                var errcode = result.errcode
                if (errcode == 0) {
                    //success
                    for (let index = 0; index < result.data.len; index++) {
                        that.$data.tableData.push(result.data[index])
                        that.$data.tableDatabackup.push(result.data[index])
                        if (index == result.data.len - 1) {
                            this.tablealready = true
                        }
                    }

                }
                else if (errcode == -1003) {
                    MessagePlugin.error('登录失效，获取信息失败，请重新登录')
                    console.error('登录失效，需要重新登陆')
                }
                else {
                    alert('遇到了未知错误，请联系管理员')
                }
            }
            xhr.send('key=' + key)
        }
        else {
            this.$data.noadmin = true
        }
    },
    methods: {
        //搜索表格
        searchrehandleSelectChange(value/*, { selectedRowData }*/) {
            searchselectedRowKeys = value
            if (value.length > 0) {
                this.$data.pldelclick = false
            }
            else {
                this.$data.pldelclick = true
            }
        },
        //普通显示表格
        rehandleSelectChange(value/*, { selectedRowData }*/) {
            selectedRowKeys.value = value
            if (value.length > 0) {
                this.$data.pldelclick = false
            }
            else {
                this.$data.pldelclick = true
            }
        },
        rehandleClickedit(res) {
            var row = res.row
            this.$data.form = {
                eqcode: row.eq_code,
                eqname: row.name,
                ascription: row.ascription,
                id: row.id,
                sn: row.sn,
                model: row.model,
            }

            console.log(row.eq_code)
        },
        getck(sname) {//获取单个cookies
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
        //搜索的选择框
        searchselectonChange(e) {
            //还原批量删除的按钮
            // this.$data.pldelclick = true
            // selectedRowKeys = ref([]);
            // searchselectedRowKeys = ref([]);

            this.selectvalue = e
            this.searchinputvalue = ''
            this.$data.tablealready = true
            this.$data.searchtablealready = false
        },

        //每页条数改变时触发 选择一页显示多少行
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`);
            this.currentPage = 1;
            this.pageSize = val;
        },
        //当前页改变时触发 跳转其他页
        handleCurrentChange(val) {
            console.log(`当前页: ${val}`);
            this.currentPage = val;
        },
        //点击编辑
        handleEdit(r1, r2) {
            console.log(r1, r2)
            var id = r1
            var code = r2[1]
            var name = r2[3]
            var ascription = r2[2]
            var sn = r2[5]
            var model = r2[4]

            this.$data.from_dialog_mode = 0
            this.$data.add_from_mode = false
            //同步参数
            this.$data.form = {
                eqcode: code,
                eqname: name,
                ascription: ascription,
                id: id,
                sn: sn,
                model: model,

            }
        },
        //点击删除
        handleDelete(r1, r2) {
            console.log(r1, r2)
        },
        //新增
        add_eq(title) {
            this.$data.edit_dialog_title = title
            this.$data.from_dialog_mode = 1
            this.$data.add_from_mode = true
            this.$data.form = {
                eqcode: '',
                eqname: '',
                ascription: '',
                id: '',
                sn: '',
                model: '',

            }
        },
        //退出登录
        alertclick() {
            var key = this.getck('key')
            const xhr = new XMLHttpRequest()
            xhr.open('post', 'http://10.3.146.103/json/logout', true)
            //正经返回数据
            //{"data":{"admin":0,"class":"\u57ce\u8f68221","login":"yes","name":"\u8d75\u6dd1\u83b9","password":"123456","usercode":"cg22150"},"errcode":0,"errmsg":"ok"}
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
            xhr.da
            xhr.onload = () => {
                var result = JSON.parse(xhr.response.replace(/\r|\n/ig, ""));
                console.log(result)
            }
            xhr.send('key=' + key)
            document.cookie = "login=false;path=/;expires=86400";
            document.cookie = "logindata=none;path=/;expires=86400"
            this.$data.activeName = 'first'
            this.$data.dialogFormVisible = false
            //登出刷新
            location.reload()
        },

        searchInput(e) {
            var that = this
            //还原批量删除的按钮
            // this.$data.pldelclick = true;

            if (e != '') {
                var data = that.tableData
                var seledata = that.selectvalue
                var da = []
                if (seledata == '1') {
                    //设备名
                    var find1 = this.query(data, e, 'eqcode')
                    for (let index = 0; index < find1.length; index++) {
                        //var vv = JSON.parse(v)
                        that.$data.searchtableData = []
                        da.push(find1[index])
                        that.searchtableData = da
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                    if (find1.length == 0) {
                        that.$data.searchtableData = []
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                }
                if (seledata == '2') {
                    //设备code
                    var find2 = this.query(data, e, 'usercode')
                    for (let index = 0; index < find2.length; index++) {
                        //var vv = JSON.parse(v)
                        that.$data.searchtableData = []
                        da.push(find2[index])
                        that.searchtableData = da
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                    if (find2.length == 0) {
                        that.$data.searchtableData = []
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                }
                if (seledata == '3') {
                    //归属
                    var find3 = this.query(data, e, 'returncode')
                    for (let index = 0; index < find3.length; index++) {
                        //var vv = JSON.parse(v)
                        that.$data.searchtableData = []
                        da.push(find3[index])
                        that.searchtableData = da
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                    if (find3.length == 0) {
                        that.$data.searchtableData = []
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                }
                if (seledata == '4') {
                    //归属
                    var find3 = this.query(data, e, 'date')
                    for (let index = 0; index < find3.length; index++) {
                        //var vv = JSON.parse(v)
                        that.$data.searchtableData = []
                        da.push(find3[index])
                        that.searchtableData = da
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                    if (find3.length == 0) {
                        that.$data.searchtableData = []
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                }
                if (seledata == '5') {
                    //归属
                    var find3 = this.query(data, e, 'returndate')
                    for (let index = 0; index < find3.length; index++) {
                        //var vv = JSON.parse(v)
                        that.$data.searchtableData = []
                        da.push(find3[index])
                        that.searchtableData = da
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                    if (find3.length == 0) {
                        that.$data.searchtableData = []
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                }
                if (seledata == '6') {
                    //归属
                    var find3 = this.query(data, e, 'status')
                    for (let index = 0; index < find3.length; index++) {
                        //var vv = JSON.parse(v)
                        that.$data.searchtableData = []
                        da.push(find3[index])
                        that.searchtableData = da
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                    if (find3.length == 0) {
                        that.$data.searchtableData = []
                        that.$data.tablealready = false
                        that.$data.searchtablealready = true
                    }
                }
            }
            else {
                this.$data.tablealready = true
                this.$data.searchtablealready = false
            }
        },

        query(list, keyWord, attribute = 'name') {
            const reg = new RegExp(keyWord) // 创建正则表达式
            const arr = []
            for (let i = 0; i < list.length; i++) {
                if (reg.test(list[i][attribute])) {
                    arr.push(list[i])
                }
            }
            return arr
        },
        onSubmit() {
            // this.subtime++
            // var username = this.form.username
            // var password = this.form.pws
            // var usercode = this.form.usercode
            // var admin = this.form.admin
            // var classs = this.form.classs
            // var url = 'http://www.baidu.com'
            // if (admin == '') {
            //     //admin为空
            //     admin = 0
            //     //url
            //     url = 'http://10.3.146.103/json/user/add/' + usercode + '/' + username + '/' + classs + '/' + password + '/0'
            // }
            // else {
            //     url = 'http://10.3.146.103/json/user/add/' + usercode + '/' + username + '/' + classs + '/' + password + '/' + admin
            // }

            // if (username == '' || password < 4 || usercode == '' || classs == '') {
            //     //验证表单
            //     this.$refs['formRef'].validate()
            // }
            // else {
            //     const xhr = new XMLHttpRequest()
            //     xhr.open('get', url, true)
            //     //正经返回数据
            //     //{"data":{"admin":0,"class":"\u57ce\u8f68221","login":"yes","name":"\u8d75\u6dd1\u83b9","password":"123456","usercode":"cg22150"},"errcode":0,"errmsg":"ok"}
            //     xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
            //     xhr.da
            //     xhr.onload = () => {
            //         //var result = JSON.parse(xhr.response.replace(/\r|\n/ig, ""));

            //     }
            //     xhr.send()
            // }
        },

    },

}
</script>

<style scoped>
.t-message__list {
    top: 130px !important;
}

.el-dialog {
    background: var(--td-bg-color-container) !important;
}

.el-input__inner {
    background: var(--td-bg-color-container) !important;
}

.el-dialog__title {
    color: var(--td-text-color-primary) !important;
}

.t-button__text {
    display: flex;
    align-items: center;
}

.el-checkbox__inner {
    z-index: 0 !important;
}

.el-table::before {
    z-index: 0 !important;
}

/*滚动条样式*/
::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-thumb {
    border-radius: 50px;
    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    background: var(--td-bg-color-component-active);
}

::-webkit-scrollbar-track {
    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    border-radius: 0;
    background: rgba(0, 0, 0, 0.1);

}
</style>
