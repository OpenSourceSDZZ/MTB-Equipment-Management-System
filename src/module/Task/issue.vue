<template>
    <div>
        <div
            style="font-size: 10px;color: var(--td-text-color-secondary);position: absolute;display: flex;flex-direction: column;text-align: end;right: 37px;top: 87px;">
            <span>From:{{ from? from: 'Click Page' }}</span>
            <span>Why:{{ why? why: 'Add Task' }}</span>
        </div>

        <div style="display: flex;justify-content: center;padding: 0px 16px;">
            <div id="issuepage" style="width: 98%;padding: 20px;">
                <div style="display: flex;flex-direction: row;justify-content: space-between;">
                    <!--use-->
                    <div style="min-width: 40%;">
                        <t-card title="任务信息">
                            <!---->
                            <div style="display: flex;align-items: center;margin: 5px 0px 12px;margin-left: 10px;">
                                <t-checkbox v-model="checkboxuservalue">帮发布</t-checkbox>
                                <div style="display: flex;">
                                    <t-input :disabled="!checkboxuservalue" placeholder="发布人Code" size="small"
                                        v-model="usercodes" style="margin: 0px 10px 0px 12px;" />
                                </div>
                                <t-tag theme="warning" variant="light-outline">
                                    <template #icon>
                                        <t-icon name="error-circle" />
                                    </template>
                                    请确认你有任务发布权限!
                                </t-tag>
                            </div>
                            <!---->
                            <div>
                                <div style="display: flex;align-items: center;margin-left: 10px;">
                                    <span
                                        style="color: var(--td-text-color-primary);font: var(--td-font-body-medium)">任务编号:
                                    </span>
                                    <t-input style="width: 181px;margin-left: 10px;" size="small" value="系统自动生成"
                                        :disabled="true"></t-input>
                                </div>
                                <!-- <div style="width: 450px;height: 100px;background: var(--td-bg-color-page);"></div> -->
                            </div>
                            <!---->
                            <div style="margin-top: 13px;">
                                <div style="display: flex;align-items: center;">
                                    <span class="bitian">*</span>
                                    <span
                                        style="color: var(--td-text-color-primary);font: var(--td-font-body-medium)">任务名称:
                                    </span>
                                    <t-input style="width: 181px;margin-left: 10px;" placeholder="请输入"
                                        v-model="lendeqcodeyyvalue"></t-input>
                                </div>
                            </div>
                            <!---->
                            <div style="margin-top: 13px;">
                                <div style="display: flex;align-items: center;">
                                    <span class="bitian">*</span>
                                    <span
                                        style="color: var(--td-text-color-primary);font: var(--td-font-body-medium)">任务时间:
                                    </span>
                                    <t-date-range-picker style="margin-left: 10px;" enable-time-picker clearable />
                                </div>
                            </div>
                            <!---->
                            <div style="margin-top: 13px;">
                                <div style="display: flex;margin-left: 10px;" class="ran-transfer-height-220px">
                                    <span
                                        style="color: var(--td-text-color-primary);font: var(--td-font-body-medium)">人员设置:</span>
                                    <t-transfer class="biaoji" style="margin-left: 10px;" v-model="targetValue"
                                        theme="primary" :operation="['移除', '加入']" :data="list" :search="true"
                                        :title="['人员列表', '参与人员']"></t-transfer>
                                </div>
                            </div>



                        </t-card>
                    </div>
                    <!--INFO-->
                    <div style="width: 50%;margin-right: 115px;">
                        <t-card title="任务描述">
                            <div>
                                <t-textarea class="ran-textarea-height-188px" placeholder="请输入内容"
                                    :autosize="{ maxRows: 1880 }" />
                            </div>
                        </t-card>
                        <t-card title="携带设备" style="margin-top: 13px;">
                            <div style="display: flex;">
                                <div>
                                    <t-input style="width: 181px;" placeholder="请输入（回车自动添加）"
                                        v-model="lendeqcodeyyvalue" />
                                </div>
                                <div style="width: 100%;margin-left: 10px;">
                                    <t-textarea
                                        class="ran-textarea-resize_none ran-textarea-placeholder-primary ran-textarea-value-primary"
                                        placeholder="暂无数据" v-model="witheqlist" :autosize="{ maxRows: 1880 }"
                                        :disabled="true" />
                                </div>
                            </div>
                        </t-card>
                    </div>
                </div>
                <!--Button-->
                <div style="margin-top: 16px;">
                    <t-button block @click="lend">确认发布</t-button>
                </div>

            </div>
        </div>
    </div>
    <!---->
</template>

<script setup>
import { ref } from 'vue';
const list = [];
for (let i = 0; i < 20; i++) {
    list.push({
        value: i.toString(),
        label: `内容 #00${i + 1}`,
    });
}

const targetValue = ref([]);
</script>

<script>

export default {
    name: 'TaskIssue',
    props: {
        from: String,
        why: String,
    },
    data() {
        return {
            witheqlist: '1. 01001 xxx:设备名\n2. 01002 xxx:设备名\n3. 01004 xxx:设备名\n4. 01004 xxx:设备名'
        }
    },
    mounted() {

    },
    methods: {

    },

}
</script>

<style>
.ran-textarea-placeholder-primary>textarea::placeholder {
    color: var(--td-text-color-primary) !important;
}

.ran-textarea-height-188px>textarea {
    min-height: 188px !important;
    max-height: 188px !important;
    height: 188px !important;
    resize: none;
}

.ran-textarea-resize_none>textarea {
    resize: none;
}

.ran-textarea-value-primary>textarea {
    color: var(--td-text-color-primary) !important;
}

.ran-transfer-height-220px>div.biaoji {
    height: 220px !important;
}

.ran-transfer-height-220px>div.biaoji>div.t-transfer__list {
    height: 172px !important;
}

#issuepage {
    background: var(--td-bg-color-container);
}

.t-card__body {
    padding-top: 0px !important;
}

.bitian {
    margin-right: 3px;
    color: var(--td-error-color);
}
</style>
