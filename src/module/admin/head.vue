<template>
    <!-- <div v-if="show" style="display: flex;">
        <div style="margin-right: 12px;">
            <span ></span>
            <t-switch size="small" v-model="">
                <template #label="slotProps">
                    <template v-if="slotProps.value">
                        <svg viewBox="0 0 24 24" class="dark-icon" style="height: 11px;">
                            <path
                                d="M11.01 3.05C6.51 3.54 3 7.36 3 12a9 9 0 0 0 9 9c4.63 0 8.45-3.5 8.95-8c.09-.79-.78-1.42-1.54-.95A5.403 5.403 0 0 1 11.1 7.5c0-1.06.31-2.06.84-2.89c.45-.67-.04-1.63-.93-1.56z"
                                fill="currentColor"></path>
                        </svg>
                    </template>
                    <template v-else>
                        <svg viewBox="0 0 24 24" class="light-icon"
                            style="height: 11px;color: var(--td-gray-color-10);">
                            <path
                                d="M6.05 4.14l-.39-.39a.993.993 0 0 0-1.4 0l-.01.01a.984.984 0 0 0 0 1.4l.39.39c.39.39 1.01.39 1.4 0l.01-.01a.984.984 0 0 0 0-1.4zM3.01 10.5H1.99c-.55 0-.99.44-.99.99v.01c0 .55.44.99.99.99H3c.56.01 1-.43 1-.98v-.01c0-.56-.44-1-.99-1zm9-9.95H12c-.56 0-1 .44-1 .99v.96c0 .55.44.99.99.99H12c.56.01 1-.43 1-.98v-.97c0-.55-.44-.99-.99-.99zm7.74 3.21c-.39-.39-1.02-.39-1.41-.01l-.39.39a.984.984 0 0 0 0 1.4l.01.01c.39.39 1.02.39 1.4 0l.39-.39a.984.984 0 0 0 0-1.4zm-1.81 15.1l.39.39a.996.996 0 1 0 1.41-1.41l-.39-.39a.993.993 0 0 0-1.4 0c-.4.4-.4 1.02-.01 1.41zM20 11.49v.01c0 .55.44.99.99.99H22c.55 0 .99-.44.99-.99v-.01c0-.55-.44-.99-.99-.99h-1.01c-.55 0-.99.44-.99.99zM12 5.5c-3.31 0-6 2.69-6 6s2.69 6 6 6s6-2.69 6-6s-2.69-6-6-6zm-.01 16.95H12c.55 0 .99-.44.99-.99v-.96c0-.55-.44-.99-.99-.99h-.01c-.55 0-.99.44-.99.99v.96c0 .55.44.99.99.99zm-7.74-3.21c.39.39 1.02.39 1.41 0l.39-.39a.993.993 0 0 0 0-1.4l-.01-.01a.996.996 0 0 0-1.41 0l-.39.39c-.38.4-.38 1.02.01 1.41z"
                                fill="currentColor"></path>
                        </svg>
                    </template>
                </template>
            </t-switch>
            <UseDark v-slot="{ isDark, toggleDark }">
                <button @click="toggleDark()">
                    Is Dark: {{ isDark }}
                </button>
            </UseDark>
        </div> 

    </div>
     -->


</template>

<script setup>
//import { Icon } from 'tdesign-icons-vue-next';
// import { UseDark } from '@vueuse/components'



</script>

<script>
export default {
    name: 'HeAd',
    data() {
        return {
            visible: false,
            showmenu: false,
            show: false,
            thememode: true,
        }
    },
    mounted() {
        var that = this
        if (this.getck('login') == 'true') {
            that.$data.show = true
        }
        else {
            that.$data.show = false
        }
    },
    methods: {

        handleClose(done) {
            console.log(done)
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

        }
    },

}
</script>
  
<style>
.t-switch {
    background: var(--td-gray-color-2) !important;
}

.t-is-checked {
    background: var(--td-gray-color-13) !important;
}

.menu {
    position: fixed;
    top: -8px;
    right: 0px;
    margin: 0px;
    transition: .5s all ease;
    z-index: -1;
}

.menushow {
    transform: translate(0px, 72px);
    box-shadow: 0 2px 4px -1px rgb(0 0 0 / 20%), 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%);
}

.t-avatar {
    background: transparent !important;
}

.t-default-menu {
    background: var(--td-bg-color-container) !important;
}

.t-icon-user {
    color: #fff !important;
}





.theme-toggler-content {
    background-color: #141414;
    color: #e5eaf3;
    transition: border-color .3s,background-color .3s;
    background-color: transparent;
    display: none;
    border-radius: 50%;
    height: 24px;
    padding: 0 12px;
}

.switch {
    margin: 0;
    display: inline-block;
    position: relative;
    width: 40px;
    height: 20px;
    border: 1px solid #4c4d4f;
    outline: none;
    border-radius: 10px;
    box-sizing: border-box;
    background: #2c2c2c;
    cursor: pointer;
    transition: border-color .3s,background-color .3s;
}

.switch__action {
    transform: translate(20px);
}
.switch__action, .switch__icon {
    width: 16px;
    height: 16px;
}
.switch__action {
    position: absolute;
    top: 1px;
    left: 1px;
    border-radius: 50%;
    background-color: #141414;
    transform: translate(0);
    color: #cfd3dc;
    transition: border-color .3s,background-color .3s,transform .3s;
}
</style>
  