<template>
    <t-head-menu :theme="isDark ? 'dark' : 'light'" class="big_menu" id="headmenu"
        style="position: fixed;top: 0px;transition: .5s all ease;" @click="headmoveout">
        <template #logo>
            <div style="width: 40px;height: 40px;margin-left: 13px;display: flex;align-items: center;">
                <t-button shape="square" variant="text" style="border: none;width: 40px;height: 40px;"
                    :onClick="togglesonmenu">
                    <template #icon><t-icon name="bulletpoint" style="width: 25px;height: 25px;" /></template>
                </t-button>
            </div>
            <span style="font-size: 21px;font-weight: bold;margin-left: 18px;user-select: none;">{{
                header_title
            }}</span>
        </template>
        <!--右上角操作区-->
        <template #operations>
            <a href="javascript:void(0);" @click="toggleDark()" @click.end="shou_dong_qie_huan_le()"
                class="mar8 guide_darktoggle" style="display: flex;">
                <ion-icon class="ioicon t-menu__operations-icon" :name="isDark ? 'sunny' : 'moon-outline'"></ion-icon>
            </a>
            <a href="javascript:void(1);" title="重载页面" @click="pagereload()" class="mar8 guide_refresh"
                style="display: flex;">
                <t-icon class="t-menu__operations-icon" name="refresh" />
            </a>
            <a href="javascript:void(2);" v-if="!loginpage_show" @click="showandclose" :showandclose="showandclose"
                class="mar8 guide_more" title="More">
                <t-icon class="t-menu__operations-icon" name="ellipsis" />
            </a>
        </template>
    </t-head-menu>
    <!--侧边栏-->
    <t-menu :theme="isDark ? 'dark' : 'light'" default-value="l2" style="margin-right: 40px" :value="mini_menu_choose"
        :style="showsonmenu ? 'transform: translate(0px,0px);' : 'transform: translate(-232px,0px);'" class="son_menu"
        @mousemove="headmoveover" :onChange="changeminimenuchoose">
        <template #logo>
            <img width="136" class="t-menu__logo--center" style="display:none;"
                src="https://www.tencent.com/img/index/menu_logo_hover.png" alt="logo" />
        </template>
        <t-menu-item value="l1" v-if="loginpage_show || isadmin">
            <template #icon>
                <t-icon :name="loginpage_show ? 'login' : 'laptop'" />
            </template>
            {{ loginpage_show ? '登录' : '后台管理' }}
        </t-menu-item>
        <t-menu-item value="l2" v-show="!loginpage_show">
            <template #icon>
                <t-icon name="cart" />
            </template>
            设备借出/归还
        </t-menu-item>
        <t-menu-item value="l7">
            <template #icon>
                <t-icon name="dashboard" />
            </template>
            仪表板
        </t-menu-item>
        <!-- <t-menu-item value="l6" v-show="!loginpage_show"> -->
        <!-- @click="MessagePlugin.info({ content: '还没有开发这个功能', duration: 3000 })" -->
        <!-- <template #icon>
                <ion-icon name="today-outline" style="width: 20px;height: 20px;margin-right: 8px;"></ion-icon>
            </template>
            任务发布
        </t-menu-item> -->
        <a href="http://10.3.146.100" target="_blank" style="text-decoration: none;">
            <t-menu-item value="l3">
                <template #icon>
                    <t-icon name="cloud" />
                </template>
                共享网盘
            </t-menu-item>
        </a>
        <a href="http://10.3.146.103" target="_blank" style="text-decoration: none;">
            <t-menu-item value="l4">
                <template #icon>
                    <t-icon name="server" />
                </template>
                设备管理系统面板
            </t-menu-item>
        </a>
        <t-menu-item value="l5">
            <template #icon>
                <t-icon name="root-list" />
            </template>
            更新日志
        </t-menu-item>

        <span
            style="user-select: none;display: flex;justify-content: center;position: absolute;bottom: 15px;font: var(--td-font-body-small);width: 83px;margin: 0 auto;left: 0px;right: 0px;color: var(--td-text-color-primary)">Version:
            {{ version }}</span>
        <!-- <t-menu-item value="l3">
            <template #icon>
                <t-icon name="play-circle" />
            </template>
            视频区
        </t-menu-item> -->
        <!-- <t-menu-item value="l4">
            <template #icon>
                <t-icon name="user-circle" />
            </template>
            个人中心
        </t-menu-item> -->
    </t-menu>
    <!--Sonmenu-->
    <div id="moremenu" class="menu" :class="showmenu ? 'menushow' : ''">
        <t-menu width="150px" :value="iiiid" :onChange="changeiiiid" class="ran-more-menu-ul-padding-8">
            <t-menu-item value="0" @click="showchangepwsdia" showchangerrrrr="" class="changepws">
                <template #icon>
                    <icon name="edit" size="218px" />
                </template>
                修改密码
            </t-menu-item>
            <t-menu-item value="1" @click="showinfodialog" showchangerrrrr="" class="moreinfo">
                <template #icon>
                    <icon name="layers" size="218px" />
                </template>
                更多信息
            </t-menu-item>
            <t-menu-item value="2" @click="loginoutt" showchangerrrrr="" class="clogout">
                <template #icon>
                    <icon name="login" size="218px" />
                </template>
                退出登陆
            </t-menu-item>
        </t-menu>
    </div>

    <LoginPage v-if="loginpage_show && !showdashboard"></LoginPage>
    <div style="height: 20px;background-color: var(--td-bg-color-page);" v-else></div>

    <div style="height: 56px;" v-if="!loginpage_show && !showdashboard"></div>
    <!--登录页不显示 借出页不显示 发布页不显示时才显示-->
    <t-tabs :default-value="1" v-if="!loginpage_show && !showlend && !showissue && !showdashboard" :onChange="handleClick"
        style="margin-top: 16px;margin-bottom: 16px;margin-right: 22px;padding: 12px;"
        :style="showsonmenu ? 'margin-left: 254px;' : 'margin-left: 22px;'">
        <t-tab-panel :value="1" label="使用须知">
            <div>
                <h1>使用"后台管理"功能请确保你有管理员权限</h1>
                <h2>请规范你的操作行为，误操作由操作人员负责！</h2>
            </div>
        </t-tab-panel>
        <t-tab-panel :value="2" label="用户管理">
            <UserPage style="padding:20px"></UserPage>
        </t-tab-panel>
        <t-tab-panel :value="3" label="设备管理">
            <EquipmentPage style="padding:20px"></EquipmentPage>
        </t-tab-panel>
        <t-tab-panel :value="4" label="数据管理">
            <Record style="padding:20px"></Record>
        </t-tab-panel>
        <!-- <t-tab-panel :value="0" label="任务管理"></t-tab-panel> -->
    </t-tabs>
    <div v-if="!loginpage_show && showlend && !showissue && !showdashboard" class="toggle_menu_animation__function"
        :style="showsonmenu ? 'margin-left: 232px;' : 'margin-left: 0px;'">
        <Lend></Lend>
    </div>
    <div v-if="!loginpage_show && !showlend && showissue && !showdashboard" class="toggle_menu_animation__function"
        :style="showsonmenu ? 'margin-left: 232px;' : 'margin-left: 0px;'">
        <Issue :from="issuepagedata.from" :why="issuepagedata.why"></Issue>
    </div>
    <div v-if="!showlend && !showissue && showdashboard" class="toggle_menu_animation__function"
        :style="showsonmenu ? 'margin-left: 232px;' : 'margin-left: 0px;'">
        <Dashboard ref="dashboard_son"></Dashboard>
    </div>

    <!--mask-->
    <div id="mask" v-show="showmask" @click="dianjimengbantuichudenglu"></div>
    <!--Footer-->
    <!---->
    <footer class="t-layout__footer" style="user-select: none;" v-if="!showdashboard"
        :style="loginpage_show ? 'position: absolute;bottom: 0px;color: rgb(255, 255, 255);display: flex;margin: 0px auto;width: 397px;left: 0px;right: 0px;justify-content: center;font: var(--td-font-body-medium);' : 'text-align: center;font: var(--td-font-body-medium);'">
        Copyright @ 2023
        <span :style="loginpage_show ? 'margin: 0px 5px;' : ''">
            <t-popup>
                MTB.
                <template #content>
                    <div>前端：<a href="https://www.ipv4-ran7.top/" target="_blank">Wesley(城轨222 文俊亮)</a><br />后端：<a
                            href="https://ddos-ling.top/" target="_blank">DDoS_LING(网络211 梁仕途)</a></div>
                </template>
            </t-popup>
        </span>
        All Rights Reserved
    </footer>
    <!---->
    <footer class="t-layout__footer" v-if="showdashboard"
        style="user-select: none;bottom: 0px;display: flex;margin: 0px auto;width: 397px;left: 0px;right: 0px;justify-content: center;font: var(--td-font-body-medium);">
        Copyright @ 2023
        <span style="margin: 0px 5px;">
            <t-popup>
                MTB.
                <template #content>
                    <div>前端：<a href="https://www.ipv4-ran7.top/" target="_blank">Wesley(城轨222 文俊亮)</a><br />后端：<a
                            href="https://ddos-ling.top/" target="_blank">DDoS_LING(网络211 梁仕途)</a></div>
                </template>
            </t-popup>
        </span>
        All Rights Reserved
    </footer>
    <!---->

    <!--提示区-->
    <t-dialog v-model:visible="visible" header="提示" theme="warning" body="将要退出登陆" :closeBtn="false" :on-confirm="logout" />

    <!--改密码-->
    <t-dialog v-model:visible="showchangepasswordia" :closeBtn="false" :cancelBtn="change_password_dialog_cancelbtn_show" :width="780" :closeOnOverlayClick="false"
        :closeOnEscKeydown="false" confirmBtn="确认修改" :onConfirm="changepws">
        <template #header>
            <div>
                <t-icon name="edit" color="var(--td-brand-color-7)" size="25px" />
                <span style="vertical-align: middle">修改密码</span>
            </div>
        </template>
        <template #body>
            <span v-if="firsttimelogin">当前密码较简单，请更改密码后使用</span>
            <t-form ref="changepwsform" :rules="changepwsrule" :data="changepwsformdata" label-align="right"
                :label-width="125" style="margin-top: 14px;margin-bottom: 10px;" :onValidate="change_password_main">
                <t-form-item label="原密码" name="oldpassword">
                    <t-input ref="old_password_input" v-model="changepwsformdata.oldpassword" type="password" :onEnter="tonext_input('new_password_input')"></t-input>
                </t-form-item>
                <t-form-item label="新密码" name="newpassword">
                    <t-input ref="new_password_input" v-model="changepwsformdata.newpassword" type="password" :onEnter="tonext_input('new2_password_input')"></t-input>
                </t-form-item>
                <t-form-item label="再次输入新密码" name="new2password">
                    <t-input ref="new2_password_input" v-model="changepwsformdata.new2password" type="password"></t-input>
                </t-form-item>
            </t-form>
        </template>
    </t-dialog>

    <!--Update-->
    <div class="randrawerfoot" :class="updatashow ? 'showrandrawer' : ''"></div>
    <t-drawer v-model:visible="updatashow" :size="800" header="更新日志" :footer="false">
        <div style="margin-bottom: 10px;letter-spacing: .5px;font: var(--td-font-title-small);">
            <span>#括号内容表示当前版本下同时产出的功能</span>
        </div>
        <t-timeline mode="same">
            <!-- <t-timeline-item dot-color="success" :loading="true">
                <h2>🌈 2.2.0 <t-tag theme="success" variant="light"
                        style="background-color: rgba(2,156,212,.1);color: #029cd4;margin: 0px;font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;padding: 0px 8px;">Stable</t-tag>
                    <t-tag size="large">Future</t-tag>
                </h2>
                <ul style="list-style-type: disc;">
                    <li>
                        即将上线，敬请期待！
                    </li>
                </ul>
            </t-timeline-item> -->
            <t-timeline-item dot-color="success" :loading="true">
                <h2>🌈 2.1.230322 <t-tag theme="success" variant="light"
                        style="background-color: rgba(2,156,212,.1);color: #029cd4;margin: 0px;font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;padding: 0px 8px;">RC</t-tag>
                    <t-tag size="large">2023-03-22</t-tag>
                </h2>
                <h3 id="❗-BREAKING-CHANGES">❗ BREAKING CHANGES</h3>
                <ul style="list-style-type: disc;">
                    <li>
                        无操作登出时间延长至 120 秒
                    </li>
                    <li>
                        大部分输入框都禁止输入空格
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Dashboard</t-tag>:
                        Head头部由切换打开/关闭改为点击（按屏幕尺寸决定是否启用）
                    </li>
                </ul>
                <h3 id="💎-features">💎 Features </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        <t-tag size="small" theme="danger" variant="light">数据管理</t-tag>: 借出数据管理[修改、删除] (未实现)
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Guide</t-tag>: 引导层
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Input</t-tag>: 禁止输入空格
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">借出、归还</t-tag>
                        <ul>
                            <li>设备code输入框自动focus</li>
                            <li>显示借出人与操作人</li>
                        </ul>
                    </li>
                </ul>
                <h3 id="🚀-Update">🚀 Update </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        超时弹窗规则更新
                    </li>
                </ul>
                <h3 id="🐞-bug-fixes">🐞 Bug Fixes </h3>
                <ul>
                    <!---->
                    <li>
                        <t-tag size="small" theme="danger" variant="light">修复已知问题</t-tag>:
                        <ul>
                            <li>借出/归还后输入框未清空</li>
                            <li>帮借(转借)/帮还失败</li>
                            <li>超时未退出登录</li>
                            <li>超时蒙层导致无法使用</li>
                        </ul>
                    </li>
                </ul>
            </t-timeline-item>
            <t-timeline-item dot-color="primary" class="blueline">
                <h2>🌈 2.1.0 <t-tag theme="primary" variant="light"
                        style="background-color: var(--td-success-color-1);color: var(--td-success-color-5);margin: 0px;font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;padding: 0px 8px;">Beta</t-tag>
                    <t-tag size="large">2023-03-03</t-tag>
                </h2>
                <h3 id="💎-features">💎 Features </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        <t-tag size="small" theme="danger" variant="light">设备借出、归还</t-tag>: 功能上线 (<a href="#0020">#0020</a>)
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Page/Server</t-tag>: 概览 (<a
                            href="#0020">#0020</a>/<a href="?type=dashboard">Dashboard</a>)
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">API</t-tag>:
                        <ul>
                            <li>设备借出</li>
                            <li>设备归还</li>
                            <li>设备管理-3个</li>
                            <li>账号管理-3个</li>
                            <li>仪表盘接口-5个</li>
                        </ul>
                    </li>
                </ul>
                <h3 id="🚀-Update">🚀 Update </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        <t-tag size="small" theme="danger" variant="light">设备管理</t-tag>:
                        <ul>
                            <li>鉴权系统(<a href="#0020">#0020</a>)</li>
                        </ul>
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">账户管理</t-tag>:
                        <ul>
                            <li>鉴权系统 (<a href="#0020">#0020</a>)</li>
                        </ul>
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Index</t-tag>: <t-tag size="small" theme="danger"
                            variant="light">Footer</t-tag>内容更改
                        (<a href="#0015">#0015</a>)
                    </li>
                </ul>
                <h3 id="🐞-bug-fixes">🐞 Bug Fixes </h3>
                <ul>
                    <!---->
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Theme</t-tag>: 自动与手动冲突
                        (<a href="#0015">#0015</a>)
                    </li>
                </ul>
            </t-timeline-item>
            <t-timeline-item dot-color="primary" class="blueline">
                <h2>🌈 2.0.5 <t-tag theme="primary" variant="light"
                        style="background-color: var(--td-success-color-1);color: var(--td-success-color-5);margin: 0px;font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;padding: 0px 8px;">Beta</t-tag>
                    <t-tag size="large">2023-01-05</t-tag>
                </h2>
                <h3 id="❌-Unrealized">❌ Unrealized </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        <t-tag size="small" theme="danger" variant="light">后台管理</t-tag>:
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">设备管理</t-tag>新增与删除【包括批量删除】 (<a
                                    href="#9999">#9999</a>)</li>
                            <li><t-tag size="small" theme="danger" variant="light">用户管理</t-tag>全部功能(<a
                                    href="#9999">#9999</a>)</li>
                            <li><t-tag size="small" theme="danger" variant="light">任务管理</t-tag>全部功能(<a
                                    href="#9999">#9999</a>)</li>
                        </ul>
                    </li>
                </ul>
                <h3 id="💎-features">💎 Features </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Theme</t-tag>: 样式根据时间自动切换
                    </li>
                </ul>
                <h3 id="🚀-Update">🚀 Update </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Menu</t-tag>:
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">选项</t-tag>重载页面按钮(<a
                                    href="#0015">#0015</a>)</li>

                        </ul>
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Console</t-tag>:
                        <ul>
                            <li>Console添加样式方便定位与查看 (<a href="#0015">#0015</a>)</li>
                        </ul>
                    </li>
                </ul>
            </t-timeline-item>
            <t-timeline-item dot-color="primary" class="blueline">
                <h2>🌈 2.0.4 <t-tag theme="primary" variant="light"
                        style="background-color: var(--td-brand-color-2);color: var(--td-brand-color-7);margin: 0px;font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;padding: 0px 8px;">Alpha</t-tag>
                    <t-tag size="large">2022-12-17</t-tag>
                </h2>
                <h3 id="🚀-features">🚀 Update </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Function</t-tag>:
                        <ul>
                            <li>请求超时提示 (<a href="#0013">#0013</a>)</li>
                            <li>修改账户密码 (<a href="#0013">#0013</a>)</li>
                            <li>设备借出与归还 (<a href="#0012">#0012</a>)</li>
                        </ul>
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Console</t-tag>:
                        <ul>
                            <li>逐步console，方便随时Debug (<a href="#0013">#0013</a>)</li>
                        </ul>
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Timeout</t-tag>:
                        <ul>
                            <li>60内页面没有<t-tag size="small" theme="danger" variant="light">点击事件</t-tag>自动退出登录 (<a
                                    href="#0011">#0013</a>)</li>
                        </ul>
                    </li>
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Menu</t-tag>:
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">Header-Menu</t-tag>: 顶部菜单栏 (<a
                                    href="#0011">#0011</a>)</li>
                        </ul>
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">Sidebar-Menu</t-tag>: 侧边可以打开的菜单栏 (<a
                                    href="#0011">#0011</a>)</li>
                        </ul>
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">More-Menu</t-tag>: More菜单栏 (<a
                                    href="#0011">#0011</a>)</li>
                        </ul>
                    </li>
                </ul>
                <h3 id="🐞-bug-fixes">🐞 Bug Fixes </h3>
                <ul>
                    <!---->
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Xhr(Axios)</t-tag>: 请求设置3s超时
                        (<a href="#0013">#0013</a>)
                    </li>
                    <!---->
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Menu</t-tag>:
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">Header-Menu</t-tag>: 图标错位 (<a
                                    href="#0011">#0011</a>)</li>
                        </ul>
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">Sidebar-Menu</t-tag>: 打开菜单栏时页面不会自动收缩
                                (<a href="#0011">#0011</a>)</li>
                        </ul>
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">More-Menu</t-tag>: 错位 (<a
                                    href="#0011">#0011</a>)</li>
                        </ul>
                    </li>
                    <!---->
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Error</t-tag>: 异常报错
                        (<a href="#0010">#0010</a>)
                    </li>
                    <!---->
                    <li>
                        <t-tag size="small" theme="danger" variant="light">Function</t-tag>:
                        <ul>
                            <li>
                                <t-tag size="small" theme="danger" variant="light">Popup</t-tag>: 弹窗无法关闭以及疯狂弹窗
                                (<a href="#0009">#0009</a>)
                            </li>
                        </ul>
                        <ul>
                            <li>
                                <t-tag size="small" theme="danger" variant="light">Style</t-tag>: Body边缘空出一段距离
                                (<a href="#0008">#0008</a>)
                            </li>
                        </ul>
                        <ul>
                            <li>
                                <t-tag size="small" theme="danger" variant="light">Login</t-tag>: 登陆后需要刷新页面
                                (<a href="#0007">#0006</a>)
                            </li>
                        </ul>
                        <ul>
                            <li><t-tag size="small" theme="danger" variant="light">Login</t-tag>: 账户密码正确但是验证失败
                                (<a href="#0006">#0006</a>)
                            </li>
                        </ul>
                        <ul>
                            <li>
                                <t-tag size="small" theme="danger" variant="light">Theme</t-tag>: 深色模式颜色异常
                                (<a href="#0005">#0005</a>)
                            </li>
                        </ul>
                    </li>

                </ul>
            </t-timeline-item>
            <t-timeline-item dot-color="primary" class="blueline">
                <h2>🌈 2.0.1 <t-tag theme="primary" variant="light"
                        style="background-color: var(--td-brand-color-2);color: var(--td-brand-color-7);margin: 0px;font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;padding: 0px 8px;">Alpha</t-tag>
                    <t-tag size="large">2022-11-01</t-tag>
                </h2>
                <h3 id="💎-features">💎 Features </h3>
                <ul style="list-style-type: disc;">
                    <li>
                        新版本发布
                    </li>
                </ul>
            </t-timeline-item>
            <t-timeline-item dot-color="primary" class="blueline">
                <h2>🌈 2.0.0 <t-tag theme="warning" variant="light"
                        style="background-color: var(--td-warning-color-2);;margin: 0px;font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;padding: 0px 8px;">Build</t-tag>
                    <t-tag size="large">2022-10-10</t-tag>
                </h2>
                <h3 id="🚀-features">📌 Webpack</h3>
                <ul style="list-style-type: disc;">
                    <li>
                        构建初始形态【Vue.js/ElementUI/TDesign/npm】
                    </li>
                </ul>
                <div style="height: 28px;"></div>
            </t-timeline-item>
        </t-timeline>
    </t-drawer>

    <!--Info dialog-->
    <t-dialog v-model:visible="showpageinfodialog"
        class="ran-remove-dialog-body-padding--infodialog ran-dialog-body-textalgin-center--infodialog" width="50%"
        :header="null" :footer="null" :confirm-on-enter="true" :on-cancel="onCancel" :on-esc-keydown="onEscKeydown"
        :on-close-btn-click="onCloseBtnClick" :on-overlay-click="onOverlayClick" :on-close="close"
        :on-confirm="onConfirmAnother">
        <template #body>
            <t-avatar shape="round" size="70px">媒</t-avatar>
            <h4
                style="margin: 8px 0px 0px;color: var(--td-text-color-primary);font: 600 19px / var(--td-line-height-title-medium) var(--td-font-family);">
                媒体部 设备管理系统</h4>
            <h1
                style="margin: 0px;color: var(--td-text-color-primary);font: 400 13px / var(--td-line-height-title-small) var(--td-font-family)">
                Version {{ version }}</h1>
            <!--button-->
            <div style="margin-bottom: 6px;">
                <t-button size="small" @click="clearcache">清除缓存</t-button>
            </div>
            <div style="font-size: 12px;line-height: 16px;margin-top: 6px;">
                <div>
                    <span>登录状态: </span>
                    <span v-if="this.getck('key') && this.getck('username') && this.getck('usercode')">
                        {{ logstate ? (isadmin ? '已登录(管理员账户)' : '已登录') : '未登录' }}
                    </span>
                    <span style="color: var(--td-error-color-6)" v-else>伪登录{{
                        this.getQueryVariable('devmode') ==
                        'yes' ? '【开发模式】' : ''
                    }}</span>
                </div>
                <!--develop mode-->
                <div>
                    <span>Debug: </span>
                    <span>{{ getQueryVariable('devmode') ? '已开启' : '未开启' }}</span>
                </div>
                <div
                    v-if="this.getQueryVariable('skipe') == 'yes' || this.getQueryVariable('skipe') == 'true' || this.getQueryVariable('skipe') != false">
                    <span>登录跳过错误: </span>
                    <span>已开启</span>
                </div>
                <div>
                    <span>超级管理模式: </span>
                    <span>{{ getQueryVariable('system_admin_mode') ? '是' : '否' }}</span>
                </div>
            </div>
            <footer class="t-layout__footer"
                style="display: flex;margin: 0px auto;font: var(--td-font-body-small);flex-direction: column;align-items: center;padding-bottom: 0px;">
                <span style="font-size: 12px;transform: scale(0.9);"><a class="ran-remove-a-underline ran-link-color"
                        href="javascript:void(0)" @click="showMessage('question', 3000, '正在建设')">《使用手册》</a></span>
                <!---->
                <span>顺德中专媒体部 版权所有</span>
                <!---->
                <span>
                    Copyright @ 2023 MTB
                    <!-- <span>
                        <t-popup>
                            MTB.
                            <template #content>
                                <div>前端：<a href="https://www.ipv4-ran7.top/" target="_blank">Randosmeven</a><br />后端：<a
                                        href="https://ddos-ling.top/" target="_blank">DDos_ling</a></div>
                            </template>
                        </t-popup>
                    </span> -->
                    All Rights Reserved.
                </span>
                <span>
                    Make By Wesley With ❤️
                </span>
            </footer>
        </template>
    </t-dialog>
</template>


<script>
//Page Import
import LoginPage from '../../components/LoginPage.vue'
import UserPage from '../../components/UserPage.vue'
import EquipmentPage from '../../components/EquipmentPage.vue';
import Lend from '../lend/index.vue';
import Issue from '../Task/issue.vue';
import Dashboard from '../dashboard/dashboard.vue'
import Record from '../../components/Record.vue'

import '../../assets/css/footers_go.css';
import { reactive, ref } from 'vue';

import { useDark, useToggle } from '@vueuse/core';

//import VueApexCharts from "vue3-apexcharts";

import { MessagePlugin } from 'tdesign-vue-next';

export default {
    name: 'App',
    components: {
        LoginPage,
        UserPage,
        EquipmentPage,
        Lend,
        Issue,
        Dashboard,
        Record,
        //apexchart: VueApexCharts,
    },
    data() {
        return {
            version: '2.1.4 RC',
            loginpage_show: true,
            userpage_show: false,
            timer: null,
            check_keyareok: null,
            showmask: false,
            footershowloading: false,
            showsonmenu: false,
            showmenu: false,
            header_title: '顺德中专团委学生会媒体部 设备借出/归还系统',
            mini_menu_choose: 'l2',
            lastchoose: 'l2',
            showlend: true,
            visible: false,//退出登录
            iiiid: '',
            showchangepasswordia: false,//修改密码
            changepwsformdata: reactive({
                oldpassword: '',
                newpassword: '',
                new2password: '',
            }),
            changepwsrule: reactive({
                oldpassword: [{ required: true, message: '旧密码必填', type: 'error', trigger: 'blur' }],
                newpassword: [{ required: true, message: '新密码必填', type: 'error', trigger: 'blur' }, { validator: this.passwordValidator, message: '两次密码不一致', trigger: 'blur' },],
                new2password: [{ required: true, message: '确认密码必填', type: 'error', trigger: 'blur' }, { validator: this.passwordValidator, message: '两次密码不一致', trigger: 'blur' },],
            }),
            inclick: false,//检测空闲
            timeouttimer: null,
            chaoshibiaojidengchu: false,
            loading: false,
            updatashow: false,
            //是不是管理员
            isadmin: false,
            //info
            showpageinfodialog: false,
            //
            logstate: false,
            //
            showissue: false,
            issuepagedata: {},
            //
            showdashboard: false,
            //
            handlechange: false,
            //第一次登录
            firsttimelogin: false,
            change_password_dialog_cancelbtn_show:true,
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
        console.log(
            "                      _oo0oo_                      \n" +
            "                     o8888888o                     \n" +
            "                     88\" . \"88                     \n" +
            "                     (| -_- |)                     \n" +
            "                     0\\  =  /0                     \n" +
            "                   ___/‘---’\\___                   \n" +
            "                 .' \\|       |/ '.                 \n" +
            "                / \\\\|||  :  |||// \\                \n" +
            "               / _||||| -卍-|||||_ \\               \n" +
            "              |   | \\\\\\  -  /// |   |              \n" +
            "              | \\_|  ''\\---/''  |_/ |              \n" +
            "              \\  .-\\__  '-'  ___/-. /              \n" +
            "            ___'. .'  /--.--\\  '. .'___            \n" +
            "         .\"\" ‘<  ‘.___\\_<|>_/___.’>’ \"\".          \n" +
            "        | | :  ‘- \\‘.;‘\\ _ /’;.’/ - ’ : | |        \n" +
            "        \\  \\ ‘_.   \\_ __\\ /__ _/   .-’ /  /        \n" +
            "    =====‘-.____‘.___ \\______/___.-’___.-’=====     \n" +
            "                                                    \n" +
            "................佛祖保佑 ,永无BUG...................");
        console.log('Copyright 2023 © Wesley All Rights Reserved')
        //
        var that = this
        //页面加载参数 FROM
        var pagefrom = this.getQueryVariable('from')
        //开发模式检测
        var dev = this.getQueryVariable('devmode')
        //获取登录态
        var login_yes = this.getck('login')
        //页面加载参数 TYPE
        var loadtype = this.getQueryVariable('type')
        //获取cookie的key
        var key = this.getck('key')
        //admin
        this.$data.isadmin = this.getck('admin') == 1 ? true : false
        console.log(this.$data.loginpage_show || this.$data.isadmin)
        //CHANGELOG
        var changelog = this.getQueryVariable('changelog')
        var changelog2 = this.getQueryVariable('update')
        //Console Start
        console.log('有关详细信息，请参阅 https://www.chromestatus.com/feature/5629709824032768。')
        console.group('%c系统状态：', "background: #07c160;color: #fff;border-radius: 3px;padding: 5px;font-family:'PingFang SC, Microsoft YaHei, Arial Regular';")
        console.log('Time：' + new Date())
        console.warn('登陆状态：' + this.getck('login'))
        console.log('登录封禁状态：' + this.getck('ban'))
        console.log('%c开发模式：' + dev, "background: #ffc300;color: #000;border-radius: 3px;padding: 3px;font-family:'PingFang SC, Microsoft YaHei, Arial Regular';")
        if (pagefrom) {
            console.log('%cFROM：' + pagefrom, "background: #c87d2f;color: #fff;border-radius: 3px;padding: 3px;font-family:'PingFang SC, Microsoft YaHei, Arial Regular';")
        }
        console.groupEnd()
        //Console End

        //Function Start
        window.onload = () => {
            //BAN 检测
            this.timer = setInterval(() => {
                var that = this
                //登陆了不再检测
                if (this.getck('login') == 'true' && this.getck('key')) {
                    clearInterval(this.timer);
                    that.$data.loginpage_show = false
                    that.$data.userpage_show = true
                    document.cookie = "ban=false;path=/;expires=0";
                }
                else {
                    that.$data.loginpage_show = true
                }
            }, 100)
        };
        //开发者模式下跳过超时检测
        if (dev == 'yes') {
            console.log('%c【Develop MODE】【Skip Login Timeout Check】：开发模式已启用，关闭超时检测', "background: #fa5151;color: #fff;border-radius: 3px;padding: 5px;font-family:'PingFang SC, Microsoft YaHei, Arial Regular';")
        }
        else {
            if (login_yes == 'true' && !that.chaoshibiaojidengchu) {
                document.body.onclick = function () {
                    that.$data.inclick = true
                }
                this.ifnotclick_logout()
            }
        }

        //参数加载更新日志
        if (changelog == 'show' || changelog2 == 'show') {
            this.$data.updatashow = true
        }

        //无论是否登录都检测type
        if (loadtype == 'dashboard') {
            this.changeminimenuchoose('l7')
        }
        //验证登录态
        if (this.getck('login') == 'true') {
            this.$data.logstate = true
            //关闭登录页
            this.$data.loginpage_show = false
            //dev模式不检测key失效
            if (dev != 'yes') {
                if (this.$data.showdashboard == true) {
                    return false
                }
                else {
                    //验证key时效
                    this.check_keyareok = setInterval(() => {
                        const xhr = new XMLHttpRequest()
                        xhr.open('post', 'http://10.3.146.103/json/key/check', true)
                        //正经返回数据
                        //{"data":{"admin":0,"class":"\u57ce\u8f68221","login":"yes","name":"\u8d75\u6dd1\u83b9","password":"123456","usercode":"cg22150"},"errcode":0,"errmsg":"ok"}
                        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
                        xhr.da
                        xhr.timeout = 3000;
                        xhr.ontimeout = () => {
                            xhr.abort()
                            this.showMessage('warning', 3000, '刷新key状态失败！请检查网络状态')
                        }
                        xhr.onload = () => {
                            if (this.getck('login') != 'true' || this.$data.showdashboard == true) {
                                clearInterval(this.check_keyareok)
                            }
                            else {
                                //去除回车、空格等一些空的占位符
                                var result = JSON.parse(xhr.response.replace(/\r|\n/ig, ""));
                                if (result.status != 0) {
                                    //key无效
                                    if (result.status == -1003) {
                                        //key超时
                                        MessagePlugin.error({ content: "登录超时，请重新登陆。", duration: 9000 })
                                        setTimeout(() => {
                                            this.logout()
                                        }, 2000);
                                        //自杀
                                        clearInterval(this.check_keyareok)
                                    }
                                    else {
                                        //请求错误，缺少参数
                                        this.$data.showmsg = true
                                        MessagePlugin.error({ content: '验证登录态失败，请联系管理员。。', duration: 9000 })
                                        setTimeout(() => {
                                            this.logout()
                                        }, 2000);
                                    }
                                }
                            }
                        }
                        xhr.send('key=' + key)
                    }, 3500)
                }

            }
            //参数加载对应页面
            //issue页【暂无该功能】
            // if (loadtype == 'issue') {
            //     //var wdo = this.getQueryVariable('do')//要做啥
            //     var why = this.getQueryVariable('why')//为啥
            //     var aaa = {
            //         from: pagefrom,
            //         why: why,
            //     }
            //     this.$data.issuepagedata = aaa
            //     this.changeminimenuchoose('l6')
            // }
            //lend页
            if (loadtype == 'lend') {
                this.changeminimenuchoose('l2')
            }
        }
        else {
            this.$data.logstate = false
            //没有登录
            this.$data.mini_menu_choose = 'l1'
            this.$data.header_title = '顺德中专团委学生会媒体部 系统登录'
            if (loadtype == 'lend') {
                MessagePlugin.error('【加载错误】请登录后再试一次！', 5000)
            }
        }


        //Theme自动切换
        setInterval(() => {
            //如果手按了以后就不再检测了
            if (!this.$data.handlechange) {
                var nowtime_Hours = new Date().getHours()
                if (nowtime_Hours >= 19) {
                    if (!this.isDark) {
                        this.toggleDark()
                    }
                }
                else if (nowtime_Hours > 6 && nowtime_Hours < 19) {
                    if (this.isDark) {
                        this.toggleDark()
                    }
                }
            }
        }, 1000);

        //登陆改密码
        if (this.getck('login') == 'true' && this.getck("need_change_password") == "need") {
            this.$data.showchangepasswordia = true
            this.$data.firsttimelogin = true
            this.$data.change_password_dialog_cancelbtn_show = null
            this.$refs.old_password.focus()
        }
    },

    methods: {
        //回车聚焦下一个输入框
        tonext_input(e){
            this.$refs[e].focus()
        },
        //120秒无操作退登
        ifnotclick_logout() {
            //开始120秒倒计时
            var that = this
            this.$data.timeouttimer = setInterval(() => {
                if (this.getck('login') != 'true' || this.$data.showdashboard == true) {
                    clearInterval(this.check_keyareok)
                    return false
                }
                if (that.$data.inclick == true) {
                    //存在点击事件
                    that.$data.inclick = false
                    clearInterval(that.$data.timeouttimer)
                    this.ifnotclick_logout()
                }
                else {
                    //无点击 退出登录
                    this.showMessage('warning', 0, '超过 120 秒没有操作，已自动退出登录')
                    this.$data.inclick = false
                    this.$data.chaoshibiaojidengchu = true
                    this.logout()
                    console.log('%c【Logout】【Timeout】', "background: #fa5151;color: #fff;border-radius: 3px;padding: 5px;font-family:'PingFang SC, Microsoft YaHei, Arial Regular';")
                }
            }, 120000);
        },

        pagereload() {
            location.reload()
        },
        showinfodialog() {
            this.$data.showpageinfodialog = true;
            this.showandclose()
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
        //子菜单
        togglesonmenu() {
            var that = this
            this.$data.showsonmenu = !this.$data.showsonmenu
            //显示仪表盘时调用刷新图表方法
            if (this.$data.mini_menu_choose == 'l7') {
                let b = 0
                let a = setInterval(() => {
                    if (b >= 28) {
                        clearInterval(a)
                    }
                    else {
                        b++
                        this.$refs.dashboard_son.refresh_charts()
                    }
                }, 10);
            }
        },
        //打开/关闭more菜单
        showandclose() {
            if (this.$data.showmenu) {
                this.$data.showmenu = false
            }
            else {
                this.$data.showmenu = true
            }
        },
        //更改菜单时 title的文字
        changeminimenuchoose(a) {
            if (a == 'l1') {
                this.$data.showlend = false
                this.$data.showissue = false
                this.$data.showdashboard = false
                this.$data.mini_menu_choose = 'l1'
                this.$data.lastchoose = 'l1'
                if (this.getck('login') == 'true') {
                    this.$data.header_title = '顺德中专团委学生会媒体部 后台管理系统'
                }
                else {
                    this.$data.header_title = '顺德中专团委学生会媒体部 系统登录'
                }
            }
            else if (a == 'l2') {
                this.$data.showlend = true
                this.$data.showissue = false
                this.$data.showdashboard = false
                this.$data.mini_menu_choose = 'l2'
                this.$data.lastchoose = 'l2'
                this.$data.header_title = '顺德中专团委学生会媒体部 设备借出/归还系统'
            }
            else if (a == 'l6') {
                this.$data.showlend = false
                this.$data.showissue = true
                this.$data.showdashboard = false
                this.$data.mini_menu_choose = 'l6'
                this.$data.lastchoose = 'l6'
                this.$data.header_title = '顺德中专团委学生会媒体部 任务发布'
            }
            else {
                //其他选项还原为上次选择的
                if (this.lastchoose == 'l6') {
                    this.$data.showlend = false
                    this.$data.showissue = true
                    this.$data.showdashboard = false
                }
                else if (this.lastchoose == 'l1') {
                    this.$data.showlend = false
                    this.$data.showissue = false
                    this.$data.showdashboard = false
                    this.$data.showlend = false
                }
                else if (this.lastchoose == 'l2') {
                    this.$data.showlend = true
                    this.$data.showissue = false
                    this.$data.showdashboard = false
                }
                else {
                    this.showMessage('danger', 5000, '出现了一个错误，请重载页面！')
                }
            }
            //更新日志
            if (a == 'l5') {
                this.$data.updatashow = true
                if (this.lastchoose == 'l6') {
                    this.$data.showlend = false
                    this.$data.showissue = true
                    this.$data.showdashboard = false
                }
                else if (this.lastchoose == 'l1') {
                    this.$data.showlend = false
                    this.$data.showissue = false
                    this.$data.showdashboard = false
                    this.$data.showlend = false
                }
                else if (this.lastchoose == 'l2') {
                    this.$data.showlend = true
                    this.$data.showissue = false
                    this.$data.showdashboard = false
                }
                else {
                    this.showMessage('danger', 5000, '出现了一个错误，请重载页面！')
                }
            }
            if (a == 'l7') {
                this.$data.showissue = false
                this.$data.showdashboard = true
                this.$data.showlend = false
                this.$data.mini_menu_choose = 'l7'
                this.$data.lastchoose = 'l7'
                this.$data.header_title = '顺德中专团委学生会媒体部 设备管理系统概览'
            }
            setTimeout(() => {
                this.$data.showsonmenu = false
                if (this.$data.lastchoose == 'l7') {
                    document.getElementById("headmenu").style.top = '-56px'
                }
            }, 1);
        },
        //点击退出登录
        loginoutt() {
            this.$data.visible = true;
            this.showandclose()
        },

        //退登操作
        logout(refload_) {
            var key = this.getck('key')
            const xhr = new XMLHttpRequest()
            xhr.open('post', 'http://10.3.146.103/json/logout', true)
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
            xhr.da
            xhr.onload = () => {
                var result = JSON.parse(xhr.response.replace(/\r|\n/ig, ""));
                console.log(result)
            }
            xhr.send('key=' + key)
            document.cookie = "login=false;path=/;expires=86400";
            document.cookie = "key=;path=/;expires=86400"
            document.cookie = "username=;path=/;expires=86400"
            document.cookie = "usercode=;path=/;expires=86400"
            document.cookie = "userclass=;path=/;expires=86400"
            document.cookie = "logintime=;path=/;expires=86400"
            document.cookie = "keytimeout=;path=/;expires=86400"
            document.cookie = "admin=;path=/;expires=86400"
            if (refload_ == true) {
                console.log('已阻止登出刷新')
            }
            else {
                console.log('%c【Logout】【Click】', "background: #fa5151;color: #fff;border-radius: 3px;padding: 5px;font-family:'PingFang SC, Microsoft YaHei, Arial Regular';")
                //登出刷新
                location.reload()
            }
        },

        //点击more菜单防止选项出现
        changeiiiid() {
            this.$data.iiiid = ''
        },
        //更改密码的一系列操作
        showchangepwsdia() {
            this.$refs.old_password.focus()
            this.$data.showchangepasswordia = true;
            this.showandclose()
        },
        //验证密码自定义操作
        passwordValidator(val) {
            if (this.$data.changepwsformdata.new2password != this.changepwsformdata.newpassword && this.changepwsformdata.newpassword && this.$data.changepwsformdata.new2password) {
                return { result: false, message: '两次密码不一致', type: 'error' };
            }
            else {
                return { result: true };
            }
        },
        //验证密码内容
        changepws() {
            this.$refs['changepwsform'].submit()
        },
        //开始改密码
        change_password_main(e) {
            if (e.validateResult == true) {
                this.$data.loading = true
                var key = this.getck('key')
                var old_pws = this.changepwsformdata.oldpassword
                var new_pws = this.changepwsformdata.newpassword
                //【主操作】
                const xhr = new XMLHttpRequest()
                xhr.open('post', 'http://10.3.146.103/json/changepassword', true)
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
                xhr.da
                xhr.timeout = 3000;
                xhr.ontimeout = () => {
                    xhr.abort()
                    this.$data.loading = false
                    this.showMessage('warning', 3000, '【更改密码】请求超时')
                }
                xhr.onerror = () => {
                    this.$data.loading = false
                    console.error(xhr)
                    this.showMessage('warning', 3000, '【更改密码】请求出错')
                }
                xhr.onload = () => {
                    this.$data.loading = false
                    var result = JSON.parse(xhr.response)
                    console.group('【更改密码】')
                    if (result.errcode == 0) {
                        console.log('【更改成功】')
                        this.showMessage('success', 5000, '更改成功')
                        //【复位操作】关闭更改密码的弹窗
                        this.$data.showchangepasswordia = false;
                        //【复位操作】还原修改密码表单内容
                        this.$refs['changepwsform'].reset()
                        if (this.$data.firsttimelogin == true) {
                            this.$data.firsttimelogin = false
                            document.cookie = "need_change_password=dontneed;path=/;expires=86400"
                            this.$data.change_password_dialog_cancelbtn_show = true
                            setTimeout(() => {
                                location.reload()
                            }, 500);
                        }
                    }
                    else if (result.errcode == -1003) {
                        //【弹窗】
                        this.showMessage('error', 5000, '更改失败：登陆失效，请重新登录')
                        console.error('【更改失败：Key失效】')
                    }
                    else if (result.errcode == -1001) {
                        //【弹窗】
                        this.showMessage('error', 5000, '更改失败：缺少参数')
                        console.error('【更改失败：数据为空】')
                    }
                    else if (result.errcode == -2004) {
                        //【弹窗】
                        this.showMessage('error', 5000, '更改失败：无法加密密码信息')
                        console.error('【更改失败：无法加密密码信息】')
                    }
                    else if (result.errcode == -2003) {
                        //【弹窗】
                        this.showMessage('error', 5000, '更改失败：找不到用户')
                        console.error('【更改失败：找不到用户】')
                    }
                    else if (result.errcode == -2002) {
                        console.error('【更改失败：旧密码错误】')
                        //【弹窗】
                        this.showMessage('error', 5000, '更改失败：原密码错误')
                        //【复位操作】还原修改密码表单内容
                        this.$refs['changepwsform'].reset({ fields: ['oldpassword'] })
                        //提示
                        this.$refs['changepwsform'].setValidateMessage({
                            oldpassword: [
                                {
                                    type: 'error',
                                    message: '旧密码错误',
                                },
                            ]
                        })
                    }
                    else {
                        console.error('【更改失败：未知错误：】', xhr)
                        this.showMessage('error', 5000, '更改失败：' + result.errmsg)
                    }
                    console.groupEnd()
                }
                xhr.send("key=" + key + "&oldpassword=" + old_pws + "&newpassword=" + new_pws)
            }
        },

        //ClearCache
        clearcache() {
            this.showMessage('success', 5000, '清除缓存成功')
        },

        dianjimengbantuichudenglu() {
            this.logout()
        },

        shou_dong_qie_huan_le() {
            this.$data.handlechange = true
        },


        headmoveout() {
            var can_look_height = window.innerHeight
            if (can_look_height <= 1080 && !this.$data.showsonmenu && this.$data.mini_menu_choose == 'l7') {
                document.getElementById("headmenu").style.top = "-56px"
            }
        },
        headmoveover() {
            var can_look_height = window.innerHeight
            if (can_look_height <= 1080) {
                document.getElementById("headmenu").style.top = "0px"
            }
        },


        delParam(paramKey) {
            var url = window.location.href;    //页面url
            var urlParam = window.location.search.substring(1);   //页面参数
            var beforeUrl = url.substring(0, url.indexOf("?"));   //页面主地址（参数之前地址）
            var nextUrl = "";

            var arr = new Array();
            if (urlParam != "") {
                var urlParamArr = urlParam.split("&"); //将参数按照&符分成数组
                for (var i = 0; i < urlParamArr.length; i++) {
                    var paramArr = urlParamArr[i].split("="); //将参数键，值拆开
                    //如果键雨要删除的不一致，则加入到参数中
                    if (paramArr[0] != paramKey) {
                        arr.push(urlParamArr[i]);
                    }
                }
            }
            if (arr.length > 0) {
                nextUrl = "?" + arr.join("&");
            }
            url = beforeUrl + nextUrl;
            return url;
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
            if (time) {
                time = 3000
            }
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
    },

}
</script>
  
<style>
body {
    background: var(--td-bg-color-page) !important;
}

.t-tooltip {
    display: flex !important;
    justify-content: center !important;
}

/*菜单*/
.big_menu {
    z-index: 2 !important;
    box-shadow: 0 2px 4px -1px rgb(0 0 0 / 20%), -20px -5px 20px 0 rgb(0 0 0 / 14%), -20px -10px 10px 0px rgb(0 0 0 / 12%);
}

.t-menu__item:hover:not(.t-is-active):not(.t-is-opened):not(.t-is-disabled)[showchangerrrrr] {
    background-color: var(--td-brand-color-7) !important;
}

.t-menu__operations-icon {
    width: 30px !important;
    height: 30px !important;
}

.son_menu {
    z-index: 1 !important;
    position: fixed !important;
    top: 0px !important;
    transition: transform 0.28s cubic-bezier(0.645, 0.045, 0.355, 1) !important;
}

.t-default-menu__inner .t-menu__logo {
    border-bottom: none !important;
}

.menu {
    position: fixed;
    top: -131px;
    right: 0px;
    margin: 0px;
    transition: .5s all ease;
    z-index: 1;
}

.menushow {
    transform: translate(0px, 190px);
    box-shadow: 0 2px 4px -1px rgb(0 0 0 / 20%), 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%);
}

.t-menu__content[showchangerrrrr] {
    color: var(--td-text-color-primary);
}

.t-menu__item:hover[showchangerrrrr] .t-menu__content {
    color: var(--td-font-white-1);
}

html[theme-mode="dark"] .t-menu__content {
    color: var(--td-font-white-1);
}

.mar8 {
    margin-right: 8px;
}

.t-menu__operations-icon {
    margin-right: 0px !important;
}

.t-default-menu {
    background: var(--td-bg-color-container) !important;
}

/**菜单打开时的让位 */
.t-tabs,
.toggle_menu_animation__function {
    transition: 0.28s cubic-bezier(0.645, 0.045, 0.355, 1) !important;
}

.mdui-appbar-fixed {
    z-index: 6000;
}

.t-button__text {
    display: flex !important;
    align-items: center !important;
}

#mask {
    display: block;
    opacity: 1;
    position: fixed;
    top: 0px;
    width: 100%;
    height: 100%;
    z-index: 5999;
    background-color: rgba(0, 0, 0, .5);
    transition: .3s all ease;
}

.mdui-typo-title {
    width: 700px;
}

.blueline>.t-timeline-item__wrapper .t-timeline-item__tail {
    border-color: var(--td-brand-color);
}

.t-timeline-item__content>h2 .t-tag {
    padding: 2px 12px;
    border-radius: 3px;
    margin-left: 24px;
    font-size: 20px;
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
}

ul,
dl,
ol {
    margin: 0;
    padding: 0 0 0 1.2em;
    line-height: 22px;
}

ul ul {
    list-style-type: circle;
    margin-block-start: 0px;
    margin-block-end: 0px;
}

.t-timeline-item__content>ul {
    list-style-type: disc;
}

ul>li>.t-tag {
    color: var(--td-error-color-8) !important;
    margin: 0 2px !important;
    border-radius: 3px;
    padding: 2px 6px !important;
    font-size: 12px !important;
}

ul>li>.t-tag.tagblue {
    color: var(--td-brand-color-7) !important;
    margin: 0 2px !important;
    border-radius: 3px;
    padding: 2px 6px !important;
    font-size: 12px !important;
}

html[theme-mode="dark"] ul>li>.t-tag {
    color: var(--td-error-color-6) !important;
}

li ul>li {
    font-size: 14px;
}

li>a {
    line-height: 24px;
    text-decoration: none;
    color: var(--td-text-color-link)
}

h2 {
    margin-top: 0px !important;
}

.t-timeline-item__dot .t-loading__gradient-conic {
    background: conic-gradient(from 90deg at 50% 50%, var(--td-text-color-disabled) 0deg, var(--td-text-color-primary) 360deg) !important;
}

.randrawerfoot {
    height: 88px;
    position: fixed;
    right: 0px;
    bottom: 0px;
    width: 800px;
    background-image: linear-gradient(top, hsla(0, 0%, 100%, 0), var(--td-bg-color-container));
    background-image: -webkit-linear-gradient(top, hsla(0, 0%, 100%, 0), var(--td-bg-color-container));
    padding: 0px;
    background-color: transparent;
    z-index: 9999;
    transform: translateX(100%);
    transition: transform 0.28s cubic-bezier(0.38, 0, 0.24, 1), visibility 0.28s cubic-bezier(0.38, 0, 0.24, 1);
    pointer-events: none;
}

.showrandrawer {
    transform: translateX(0px);
}

.t-popup__content>div a {
    text-decoration: none;
    color: var(--td-text-color-primary)
}

.t-message__list {
    display: flex;
    flex-direction: column;
    align-items: center;
}





/**Randomseven ui !important*/

.ran-more-menu-ul-padding-8>div>ul {
    padding: var(--td-comp-paddingLR-s) !important;
}

a.ran-remove-a-underline {
    text-decoration: none !important;
}

a.ran-remove-a-underline:hover {
    text-decoration: none !important;
}

.ran-link-color {
    color: rgb(125, 144, 169);
}

.ran-remove-dialog-body-padding--infodialog .t-dialog__body {
    padding: 0px !important;
}

.ran-dialog-body-textalgin-center--infodialog .t-dialog__body {
    text-align: center;
}
</style>