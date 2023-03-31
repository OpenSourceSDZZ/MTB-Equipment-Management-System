<!--
 * @Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @Date: 2023-03-31 13:54:14
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2023-03-31 13:59:02
 * @FilePath: \MTB-Equipment-Management-System\CHANGELOG.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
---
title: 更新日志
spline: explain
toc: false
docClass: timeline
---

## 🌈 2.1.6 `2023-03-31` 
### 🚀 Features
- `Table`: 
  - 支持使用 `filterIcon` 支持不同列显示不同的筛选图标，[tdesign-vue#2088](https://github.com/Tencent/tdesign-vue/issues/2088) @chaishi ([#2590](https://github.com/Tencent/tdesign-vue-next/pull/2590))
  - 支持横向滚动到固定列，[tdesign-vue#1992](https://github.com/Tencent/tdesign-vue/issues/1992) @chaishi ([#2590](https://github.com/Tencent/tdesign-vue-next/pull/2590))
- `Tabs`: 标签页选项卡可配置禁止拖拽 @liweijie0812 ([#2457](https://github.com/Tencent/tdesign-vue-next/pull/2457))
- `TimePicker`: 支持`size`属性 @uyarn ([#2597](https://github.com/Tencent/tdesign-vue-next/pull/2597))
### 🐞 Bug Fixes
- `Login`: 修复登录页卡错误

  - 单行选中功能，修复 `allowUncheck: false` 无效问题，[issue#2561](https://github.com/Tencent/tdesign-vue-next/issues/2561) @chaishi ([#2590](https://github.com/Tencent/tdesign-vue-next/pull/2590))
  - 修复 `lazyload` 重置 `bug` @yanxugong ([#2580](https://github.com/Tencent/tdesign-vue-next/pull/2580))
  -  修复 `getSortIcon is not a function` 在webpack中的报错 ([issue#2538](https://github.com/Tencent/tdesign-vue-next/issues/2538)) @chaishi ([#2592](https://github.com/Tencent/tdesign-vue-next/pull/2592))
- `TreeSelect`: 
  - 修复树选择组件，在表格组件里面时，显示两个 `Tips` 问题 @chaishi ([#2590](https://github.com/Tencent/tdesign-vue-next/pull/2590))
  - 修复`1.2.0`版本后初始值为空时报错的问题 @uyarn ([#2597](https://github.com/Tencent/tdesign-vue-next/pull/2597))
- `Dropdown`: 支持`v-for`渲染下拉选项，支持`v-for`与普通插槽混用 @uyarn ([#2594](https://github.com/Tencent/tdesign-vue-next/pull/2594))
- `Menu`: 修复重新展开后，`normal` 模式的子菜单就是空的。([issue #2557](https://github.com/Tencent/tdesign-vue-next/issues/2557)) @Ericleungs ([#2589](https://github.com/Tencent/tdesign-vue-next/pull/2589))
