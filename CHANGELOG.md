<!--
 * @Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @Date: 2023-03-31 13:54:14
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2023-04-04 12:21:06
 * @FilePath: \MTB-Equipment-Management-System\CHANGELOG.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->

---

title: 更新日志
spline: explain
toc: false
docClass: timeline

---

## 🌈 2.1.230322 `2023-03-22`
### ❗ BREAKING CHANGES

- 无操作登出时间延长至 120 秒
- 大部分输入框都禁止输入空格
- `Dashboard`:Head头部由切换打开/关闭改为点击（按屏幕尺寸决定是否启用）
- dashboard接口更新 (<a href="https://github.com/OpenSourceSDZZ/MTB-Equipment-Management-System/issue/2">issue #2</a>) @Wesley0808(<a href="https://github.com/OpenSourceSDZZ/MTB-Equipment-Management-System/pull/22">#22</a>)

### 💎 Features

-`数据管理`: 借出数据管理[修改、删除] (未实现)
- `Guide`: 引导层
- `Input`: 禁止输入空格
- `借出、归还`:
    - 设备code输入框自动focus
    - 显示借出人与操作人

### 🚀 Update

- 超时弹窗规则更新

### 🐞 Bug Fixes

- `修复已知问题`:

-借出/归还后输入框未清空
-帮借(转借)/帮还失败
-超时未退出登录 (<a
    href="https://github.com/OpenSourceSDZZ/MTB-Equipment-Management-System/issue/12">issue
    #12</a>) @Wesley0808(<a
    href="https://github.com/OpenSourceSDZZ/MTB-Equipment-Management-System/pull/13">#13</a>)

-超时蒙层导致无法使用
-找不到设备但仍然借出成功 @Wesley0808(<a
    href="https://github.com/OpenSourceSDZZ/MTB-Equipment-Management-System/pull/22">#22</a>)


## 🌈 2.1.0 `2023-03-03`

### 💎 Features

- `设备借出、归还`: 功能上线
- `Page/Server`: 概览 (<a href="?type=dashboard">Dashboard</a>)
- `API`:
   - 设备借出
   - 设备归还
   - 设备管理-3个
   - 账号管理-3个
   - 仪表盘接口-5个

### 🚀 Update

-`设备管理`:
- 鉴权系统
- `账户管理`:
- 鉴权系统
- `Index`: 
   - `Footer`内容更改


### 🐞 Bug Fixes
- `Theme`: 自动与手动冲突

## 🌈 2.0.5 `2023-01-05`

### ❌ Unrealized

- `后台管理`:
   - `设备管理`新增与删除【包括批量删除】
   - `用户管理`全部功能
   - `任务管理`全部功能



### 💎 Features

- `Theme`: 样式根据时间自动切换


### 🚀 Update

- `Menu`:
-`选项`重载页面按钮
- `Console`:
   - Cosole添加样式方便定位与查看


## 🌈 2.0.4 `2022-12-17`

### 🚀 Update

- `Function`:
   -请求超时提示
   -修改账户密码
   -设备借出与归还
- `Console`:
   -逐步console，方便随时Debug
- `Timeout`:
   - 60内页面没有`点击事件`自动退出登录
- `Menu`:
   - `Header-Menu`: 顶部菜单栏
   - `Sidebar-Menu`: 侧边可以打开的菜单栏
   - `More-Menu`: More菜单栏

### 🐞 Bug Fixes

- `Xhr(Axios)`: 请求设置3s超时
- `Menu`:
   - `Header-Menu`: 图标错位
   - `Sidebar-Menu`: 打开菜单栏时页面不会自动收缩
   - `More-Menu`: 错位 
- `Error`: 修复异常报错
- `Function`:
   - `Popup`: 弹窗无法关闭以及疯狂弹窗
   - `Style`: Body边缘空出一段距离
   - `Login`: 登陆后需要刷新页面
   - `Login`: 账户密码正确但是验证失败
   - `Theme`: 深色模式颜色异常

## 🌈 2.0.1 `2022-11-01`

### 💎 Features

- 新版本发布


## 🌈 2.0.0 `2022-10-10`

###  id="🚀-features">📌 Webpack

- 构建初始形态【Vue.js/ElementUI/TDesign/npm】