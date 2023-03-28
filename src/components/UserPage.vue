<template>
    <div id="top" v-if="!noadmin">
        <div style="display: flex;flex-direction: row;margin-top: 16px;">
            <t-button theme="primary" @click="add_user('新增用户'), dialogFormVisible = true" style="margin-right: 10px;">
                <icon name="add" size="16px" />添加
            </t-button>
            <t-button theme="danger">
                <icon name="delete" size="16px" />批量删除
            </t-button>
        </div>
        <!--<el-table ref="multipleTable" :data="tableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)"
          tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="55">
          </el-table-column>
          <el-table-column label="ID" width="120">
              <template v-slot="scope">{{ scope.row[0] }}</template>
          </el-table-column>
          <el-table-column prop="3" label="姓名" width="150">
          </el-table-column>
          <el-table-column prop="1" label="用户Code" width="200">
          </el-table-column>
          <el-table-column prop="2" label="班级" width="200">
          </el-table-column>
          <el-table-column prop="4" label="操作">
              <template v-slot="scope">
                  <el-button size="mini" type="primary"
                      @click="handleEdit(scope.$index, scope.row), dialogFormVisible = true, edit_dialog_title = '编辑用户信息'"
                      icon="el-icon-edit-outline">编辑</el-button>
                  <el-button size="mini" type="danger"
                      @click="handleDelete(scope.$index, scope.row), centerDialogVisible = true"
                      icon="el-icon-delete">删除</el-button>
              </template>

          </el-table-column>
      </el-table>-->


        <t-table row-key="id" :columns="tablecolumns" :data="tabledata" :selected-row-keys="selectedRowKeys"
            @select-change="rehandleSelectChange"
            :pagination="{ defaultCurrent: 1, defaultPageSize: 10, pageSizeOptions: [10, 20, 45, 60], total: tabledata.length, }"
            max-height="700px">
            <template #op-column>
                <p>操作</p>
            </template>
            <template #op="slotProps">
                <t-button variant="outline" theme="primary" @click="rehandleClickOp(slotProps)">编辑</t-button>
                <t-button theme="danger" @click="rehandleClickOp(slotProps)">删除</t-button>
            </template>
        </t-table>

        <!--删除信息确认框-->
        <t-dialog v-model="centerDialogVisible" theme="warning" header="警 告" body="将要删除这个用户，确认删除？" cancelBtn="按错了"
            :closeBtn="false" on-close="" on-confirm="" /><!--centerDialogVisible = false -->


        <!--编辑信息弹出框-->
        <el-dialog v-model="dialogFormVisible" :title="edit_dialog_title">
            <el-form :model="form" :rules="rules" ref="formRef" id="formlist">
                <el-form-item label="ID" :label-width="formLabelWidth" required>
                    <el-input v-model="form.id" autocomplete="off" disabled />
                </el-form-item>
                <el-form-item label="UserCode" :label-width="formLabelWidth" :required="add_from_mode" prop="usercode">
                    <el-input v-model="form.usercode" autocomplete="off" />
                </el-form-item>
                <el-form-item label="姓名" :label-width="formLabelWidth" :required="add_from_mode" prop="name">
                    <el-input v-model="form.name" autocomplete="off" />
                </el-form-item>
                <el-form-item label="班级" :label-width="formLabelWidth" :required="add_from_mode" prop="classs">
                    <el-input v-model="form.classs" autocomplete="off" />
                </el-form-item>
                <el-form-item label="Admin-mode" :label-width="formLabelWidth">
                    <el-input v-model="form.admin" autocomplete="off" />
                </el-form-item>
                <el-form-item label="密码(自动转sha256)" :label-width="formLabelWidth2" prop="pws">
                    <el-input v-model="form.pws" autocomplete="off" />
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取消</el-button>
                    <el-button type="primary" @click="dialogFormVisible = false, onSubmit()">
                        完成，保存
                    </el-button>
                </span>
            </template>
        </el-dialog>

    </div>
    <div v-if="noadmin">
        <h1>您没有管理员权限</h1>
    </div>
</template>
<script setup>
import { ref } from 'vue';

// const data = new Array(5).fill(null).map((item, index) => ({
//   tid: index + 100,
//   id: `JQTest${index + 1}`,
//   status: index % 2,
//   owner: 'jenny;peter',
//   description: 'test',
// }));

const selectedRowKeys = ref([]);

const rehandleClickOp = ({ text, row }) => {
    console.log(text, row);
};

const rehandleSelectChange = (value, { selectedRowData }) => {
    selectedRowKeys.value = value;
    console.log(value, selectedRowData);
};
</script>
<script>
import { reactive } from 'vue';
import axios from 'axios';

import 'tdesign-vue-next';
import { Icon } from 'tdesign-icons-vue-next';


const api1 = 'http://10.3.146.103/json/user/list'


export default {
    name: 'UserPage',
    setup() {
        const rules = reactive({
            usercode: [
                { message: '请输入usercode', trigger: 'blur' },
                { min: 0, max: 10, message: 'usercode不能大于10位', trigger: 'blur' },
            ],
            name: [
                { message: '请输入用户名', trigger: 'blur' },
                { min: 2, max: 10, message: '请输入正确的用户名', trigger: 'blur' },
            ],
            classs: [
                { message: '请输入用户班级', trigger: 'blur' },
                { min: 0, max: 20, message: '这个班级好像有点问题？', trigger: 'blur' },
            ],
            pws: [
                { message: '请输入密码', trigger: 'blur' },
                { min: 4, max: 100, message: '密码好像有点短？', trigger: 'blur' },
            ],
        });
        return {
            rules,
        }

    },
    data() {
        return {
            multipleSelection: [],
            result1: 'none',
            currentPage: 1,
            centerDialogVisible: false,//删除用户确认框
            dialogFormVisible: false,//编辑信息弹出框
            form: {
                usercode: '',
                name: '',
                classs: '',
                pws: '',
                id: 0,
                admin: 0,
            },
            formLabelWidth: '120px',
            formLabelWidth2: '150px',
            edit_dialog_title: '编辑用户信息',
            from_dialog_mode: 0,
            add_from_mode: false,
            tablelodingshow: true,
            //
            noadmin: false,
            tabledata: [
            ],
            tablecolumns: [
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
                    width: 50,
                },
                { colKey: 'id', title: 'ID', align: 'center', width: 100 },
                { colKey: 'username', title: '姓名', width: 150 },
                { colKey: 'usercode', title: '用户Code', width: 150 },
                { colKey: 'class', title: '班级', align: 'left', width: 150 },
                { colKey: 'password', title: '密码', align: 'left' },
                {
                    colKey: 'do',
                    title: '操作',
                    cell: 'op',
                    align: 'left',
                },
            ]
        }
    },
    mounted() {
        //var that = this;
        if (this.getck('admin') == '1') {
            this.$data.noadmin = false
            var key = this.getck('key')
            axios.post(api1, { key: key }, { headers: { "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8" } }).then((res) => {
                if (res.data.errcode == -1) {
                    MessagePlugin.error('请求出错：' + res.data.errmsg)
                }
                else if (res.data.errcode == 0) {
                    let abc = []
                    for (let index = 0; index < res.data.data.len; index++) {
                        const element = res.data.data[index];
                        abc.push(element)
                        this.$data.tabledata = abc
                    }
                }
                else if (errcode == -1003) {
                    MessagePlugin.error('登录失效，获取信息失败，请重新登录')
                }
            })
        }
        else {
            this.$data.noadmin = true

            // let data = new FormData()
            // data.append('key', key)
            // Axios.post(api1, data).then((response) => {
            //     // that.$data.result1 = JSON.parse(response.request.response)
            //     // that.$data.tableData = that.$data.result1.data
            //     console.log(response)
            //     // if (response) {
            //     //     this.$data.tablelodingshow = false
            //     // }
            //     // if (errcode == 0) {
            //     //     //success
            //     //     for (let index = 0; index < result.data.len; index++) {
            //     //         that.$data.tableData.push(result.data[index])
            //     //         that.$data.tableDatabackup.push(result.data[index])
            //     //         if (index == result.data.len - 1) {
            //     //             this.tablealready = true
            //     //         }
            //     //     }

            //     // }
            //     // else if (errcode == -1002) {
            //     //     this.alert_title = '错误提示'
            //     //     this.alert_desc = '登陆状态已经失效，点击该信息重新登陆'
            //     //     this.alert_show = true
            //     // }
            //     // else {
            //     //     alert('遇到了未知错误，请联系管理员')
            //     // }
            // }).catch((error) => {
            //     console.log(error);
            // })

        }

    },
    methods: {
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
        toggleSelection(rows) {
            if (rows) {
                rows.forEach(row => {
                    this.$refs.multipleTable.toggleRowSelection(row);
                });
            } else {
                this.$refs.multipleTable.clearSelection();
            }
        },
        handleSelectionChange(val) {
            this.multipleSelection = val;
            console.log(val.length)
        },
        handleEdit(r1, r2) {
            console.log(r1, r2)
            var id = r1
            var usercode = r2[1]
            var name = r2[3]
            var classs = r2[2]
            var admin = r2[4]
            var pws = r2[5]
            this.$data.from_dialog_mode = 0
            this.$data.add_from_mode = false
            //同步参数
            this.$data.form = {
                usercode: usercode,
                name: name,
                classs: classs,
                pws: pws,
                id: id,
                admin: admin,
            }
        },
        handleDelete(r1, r2) {
            console.log(r1, r2)
        },

        add_user(title) {
            this.$data.edit_dialog_title = title
            this.$data.from_dialog_mode = 1
            this.$data.add_from_mode = true
            this.$data.form = {
                usercode: '',
                name: '',
                classs: '',
                pws: '',
                id: 'Auto',
                admin: '',
            }
        },


        onSubmit() {
            this.subtime++
            var username = this.form.username
            var password = this.form.pws
            var usercode = this.form.usercode
            var admin = this.form.admin
            var classs = this.form.classs
            var url = 'http://www.baidu.com'
            if (admin == '') {
                //admin为空
                admin = 0
                //url
                url = 'http://10.3.146.103/json/user/add/' + usercode + '/' + username + '/' + classs + '/' + password + '/0'
            }
            else {
                url = 'http://10.3.146.103/json/user/add/' + usercode + '/' + username + '/' + classs + '/' + password + '/' + admin
            }

            if (username == '' || password < 4 || usercode == '' || classs == '') {
                //验证表单
                this.$refs['formRef'].validate()
            }
            else {
                const xhr = new XMLHttpRequest()
                xhr.open('get', url, true)
                //正经返回数据
                //{"data":{"admin":0,"class":"\u57ce\u8f68221","login":"yes","name":"\u8d75\u6dd1\u83b9","password":"123456","usercode":"cg22150"},"errcode":0,"errmsg":"ok"}
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
                xhr.da
                xhr.onload = () => {
                    //var result = JSON.parse(xhr.response.replace(/\r|\n/ig, ""));

                }
                xhr.send()
            }
        },

    },

}
</script>

<style>
.el-checkbox__inner {
    z-index: 0 !important;
}

.el-table::before {
    z-index: 0 !important;
}
</style>
