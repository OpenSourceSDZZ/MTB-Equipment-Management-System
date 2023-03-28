<template>
  <div class="margintop56" style="transition: all 0.5s ease 0s;"></div>
  <div style="height: 56px;width: 100%;position: fixed;top: 0;" @click="headmoveover"></div>
  <!--list 1-->
  <div style="flex-direction: row;justify-content: space-around;" ran-list-big ran-list-big-1 ran-list-big-xmhyygz>
    <!--item 1-->
    <div ran-top-card-item>
      <t-card ran-bg-color-green ran-card>
        <template #header>
          <div class="t-card__header-wrapper">
            <div><span class="t-card__title">借出次数</span></div>
          </div>
        </template>
        <div class="item-right">
          <span>{{ topdata.lendtime }}</span>
        </div>
        <div class="item-top">
          <t-avatar size="56px">
            <template #icon>
              <t-icon name="logout"></t-icon>
            </template>
          </t-avatar>
        </div>
        <template #footer>
          <div class="t-card__footer-wrapper">
            <div class="dashboard-item-bottom">
              <div class="dashboard-item-block"> {{ Math.floor(Math.random() * 2) == 1 ? '是个不错的数字！' : '芜芜芜芜芜芜芜芜湖~~' }}
                <!-- <span class="trend-container trend-container__down dashboard-item-trend"><span
                      class="trend-icon-container"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M11.5 8L8 11.5L4.5 8" stroke="currentColor" stroke-width="1.5"></path>
                        <path d="M8 11L8 4" stroke="currentColor" stroke-width="1.5"></path>
                      </svg></span><span>20.33333%</span></span> -->
              </div>
              <!-- <t-icon name="chevron-right"></t-icon> -->
            </div>
          </div>
        </template>
      </t-card>
    </div>
    <!--item 2-->
    <div ran-top-card-item>
      <t-card ran-bg-color-blue ran-card>
        <template #header>
          <div class="t-card__header-wrapper">
            <div><span class="t-card__title">总设备数量</span></div>
          </div>
        </template>
        <div class="item-right">
          <span>{{ topdata.total }}</span>
        </div>
        <div class="item-top">
          <t-avatar size="56px">
            <template #icon>
              <t-icon name="laptop"></t-icon>
            </template>
          </t-avatar>
        </div>
        <template #footer>
          <div class="t-card__footer-wrapper">
            <div class="dashboard-item-bottom">
              <div class="dashboard-item-block"> 上次设备采购
                <span class="trend-container trend-container__down dashboard-item-trend">
                  <span class="trend-icon-container">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"
                      style="transform: rotate(180deg)">
                      <path d="M11.5 8L8 11.5L4.5 8" stroke="currentColor" stroke-width="1.5"></path>
                      <path d="M8 11L8 4" stroke="currentColor" stroke-width="1.5"></path>
                    </svg>
                  </span>
                  <span>64件新设备</span>
                </span>
              </div>
            </div>
          </div>
        </template>
      </t-card>
    </div>
    <!--item 3-->
    <div ran-top-card-item>
      <t-card ran-bg-color-red ran-card>
        <template #header>
          <div class="t-card__header-wrapper">
            <div><span class="t-card__title">未还设备数</span></div>
          </div>
        </template>
        <div class="item-right">
          <span>{{ topdata.unreturned }}</span>
        </div>
        <div class="item-top">
          <t-avatar size="56px">
            <template #icon>
              <t-icon name="login"></t-icon>
            </template>
          </t-avatar>
        </div>
        <template #footer>
          <div class="t-card__footer-wrapper">
            <div class="dashboard-item-bottom">
              <div class="dashboard-item-block"> {{ Math.floor(Math.random() * 2) == 1 ? '用完设备记得还！' : '不还设备是会被斩的！' }}
                <!-- <span class="trend-container trend-container__down dashboard-item-trend">
                    <span class="trend-icon-container">
                      <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M11.5 8L8 11.5L4.5 8" stroke="currentColor" stroke-width="1.5"></path>
                        <path d="M8 11L8 4" stroke="currentColor" stroke-width="1.5"></path>
                      </svg>
                    </span>
                    <span>20.33333%</span>
                  </span> -->
              </div>
            </div>
          </div>
        </template>
      </t-card>
    </div>
    <!--item 4-->
    <div ran-top-card-item>
      <t-card ran-card ran-bg-color-primary>
        <template #header>
          <div class="t-card__header-wrapper">
            <div><span class="t-card__title">活跃用户（{{ onlineuser.stand }}/人）</span></div>
          </div>
        </template>
        <div class="item-right">
          <span style="color: var(--td-text-color-primary);">{{ onlineuser.data }}</span>
        </div>
        <div class="item-top">
          <t-avatar size="56px">
            <template #icon>
              <t-icon name="usergroup"></t-icon>
            </template>
          </t-avatar>
        </div>
        <template #footer>
          <div class="t-card__footer-wrapper">
            <div class="dashboard-item-bottom">
              <div class="dashboard-item-block"> 与{{ onlineuser.desc }}相比
                <span class="trend-container trend-container__down dashboard-item-trend">
                  <span class="trend-icon-container">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"
                      :style="onlineuser.preway ? 'transform: rotate(180deg)' : ''">
                      <path d="M11.5 8L8 11.5L4.5 8" stroke="currentColor" stroke-width="1.5"></path>
                      <path d="M8 11L8 4" stroke="currentColor" stroke-width="1.5"></path>
                    </svg>
                  </span>
                  <span>{{ onlineuser.pre }}%</span>
                </span>
              </div>
            </div>
          </div>
        </template>
      </t-card>
    </div>
    <!--Weather-->
    <t-card class="weatherbig">
      <div style="display: flex;flex-direction: column;align-items: center;">
        <div style="height: 100px;width: 100px;">
          <img style="width: 100%;height: 100%" :src="imgu" />
        </div>
        <span style="font: var(--td-font-title-large);">{{ tempdata.weather_name }} {{ tempdata.min_temp }} ~
          {{ tempdata.max_temp }}°C</span>
      </div>
    </t-card>
  </div>
  <!--list 2-->
  <div ran-list-big ran-list-big-2 ran-list-big-xmhyygz>
    <t-card style="margin: 0 9px;width: 80%;">
      <template #header>
        <div>
          <span class="t-card__title">借出量</span>
          <span class="t-card__subtitle">(次)</span>
        </div>
      </template>
      <div id="lendcharts"></div>
    </t-card>
    <t-card style="margin: 0 10px;width: 20%;">
      <template #header>
        <div>
          <span class="t-card__title">系统服务运行状态</span>
          <span class="t-card__subtitle"></span>
        </div>
      </template>
      <div style="cursor:default;" id="serverun"></div>
    </t-card>
  </div>
  <!--list 3-->
  <div ran-list-big ran-list-big-3 id="ran-list-3">
    <t-card style="margin: 0 9px;width: 50%;">
      <template #header>
        <div>
          <span class="t-card__title" @click="onclick_eqlist_title" ran-user-select-none>设备借出数据排行</span>
        </div>
      </template>
      <div style="width: 100%;max-height: 285px;min-height: 220px;margin-top: 24px;" id="eqlistsasbig" ref="eqlistsasbig">
        <t-table ref="eqlistsasitem" id="eqlistsasitem" row-key="index" :data="eqlistsas_data" :columns="eqlistsas_colums"
          :scroll="{ type: 'virtual', rowHeight: 48, bufferSize: 100, threshold: 1, }" :hover="true" table-layout="auto"
          max-height="100%" @row-click="handleRowClick">
        </t-table>
      </div>
    </t-card>
    <t-card style="margin: 0 10px;width: 50%;">
      <template #header>
        <div>
          <span class="t-card__title" ran-user-select-none>设备未还列表</span>
        </div>
      </template>
      <div
        style="width: 100%;max-height: 285px;min-height: 220px;cursor: default;display: flex;justify-content: center;margin-top: 24px;"
        id="recordbig">
        <t-table ref="recordlist" id="recordlist" :data="recordlist_data" :columns="recordlist_colums"
          :scroll="{ type: 'virtual', rowHeight: 48, bufferSize: 100, threshold: 1, }" :hover="true" table-layout="auto"
          max-height="100%" @row-click="handleRowClick">
        </t-table>
      </div>
    </t-card>
  </div>
</template>
  
<script setup>
const handleRowClick = (e) => {
  console.log(e);
};
</script>
  
<script>
import * as echarts from 'echarts';
import axios from 'axios';
import { MessagePlugin } from 'tdesign-vue-next';
import { throwStatement } from '@babel/types';
import '../../assets/js/jquery.min.js'
//
var Chart1
var Chart2

var url = 'http://10.3.146.103:7775'
// var url = 'http://localhost:7775'
var url2 = 'http://10.3.146.103'

export default {
  name: 'DashBoard',
  expose: ['refresh_charts'],
  data() {
    return {
      //各种奇奇怪怪的设置开关控制参数：
      setdata: {
        eqlistscrollnum: 0,//技术
        eqlistscroll: true,//设备排行列表自动滚动
      },
      //debug用的设置开关
      devmode: {
        request: true,//是否请求数据（所有） 
        http_req: true,//是否请求数据（http请求所有）
        ws_req: true,//是否请求数据（ws请求）
        auto_scroll_all: true,//此项等级高于setdata中的xxxlistscroll
        auto_scroll_eqlist: true,//此项等级高于setdata中的eqlistscroll
        scroll_eqlist_message: true,//是否开启设备排行的提示
      },
      //天气数据
      tempdata: {
        weather_name: 'null',
        min_temp: '0',
        max_temp: '0'
      },
      imgu: null,
      //图表数据
      lenddata_lastweek: [],
      lenddata_thisweek: [],
      firstgetdata:true,
      //顶部数据
      topdata: { lendtime: "null", total: "null", unreturned: "null" },
      onlineuser: {
        fromdata: {},
        stand: 'null',
        data: 'null',
        desc: 'null',
        pre: 0,
        preway: true,
      },
      //设备排行数据
      eqlistsas_colums: [
        { colKey: 'id', title: '排名', },
        { colKey: 'name', title: '设备名称', },
        { colKey: 'code', title: '设备Code' },
        { colKey: 'time', title: '借出次数' },
      ],
      eqlistsas_data: [],
      //系统运行状态数据
      socket: "",
      sys_normal: 100,
      sys_unusual: 0,
      chartslist: {
        c1: "",
        c2: "",
      },
      //设备借出未还列表
      recordlist_colums: [
        { colKey: 'id', title: '编号', },
        { colKey: 'user_name', title: '借出人', },
        { colKey: 'eq_name', title: '设备名' },
        { colKey: 'eq_code', title: '设备Code' },
        { colKey: 'date', title: '借出时间' },
      ],
      recordlist_data: [],
    }
  },
  mounted() {
    //定义代理
    // var that = this
    var thisdata = this.$data

    //DEVMODE参数
    var query0 = this.getQueryString("setting_mode")
    var query1 = this.getQueryString("request")
    var query2 = this.getQueryString("http_req")
    var query3 = this.getQueryString("ws_req")
    if (query0 == 'true') {
      if (query1 == 'false') {
        this.$data.devmode.request = false
      }
      else {
        this.$data.devmode.request = true
      }
      if (query2 == 'false') {
        this.$data.devmode.http_req = false
      }
      else {
        this.$data.devmode.http_req = true
      }
      if (query3 == 'false') {
        this.$data.devmode.ws_req = false
      }
      else {
        this.$data.devmode.ws_req = true
      }
    }
    //数据
    this.RequestDATA()
    setInterval(() => {
      this.RequestDATA()
    }, 30000);

    //自动滚动
    // if (thisdata.devmode.auto_scroll_all) {
    //   if (thisdata.devmode.auto_scroll_eqlist) {
    //     setTimeout(() => {
    //       //自动滚动
    //       var item = document.getElementById("eqlistsasbig").getElementsByClassName("t-table__content")[0]
    //       var index = 0
    //       var maxindex = item.scrollHeight
    //       var lastindex = 0
    //       var sameindex = 0
    //       var dingyizhizhixingyici = 0
    //       var zhixingyici = 0
    //       var zhitanyici = 0
    //       var djfijweif = 0
    //       // var a = document.getElementById("eqlistsasbig").getElementsByClassName("t-table__content")[0].getElementsByClassName("t-table__body")[0].getElementsByTagName("tr")
    //       if (this.$data.setdata.eqlistscroll) {
    //         setInterval(() => {
    //           //业务代码
    //           if (this.$data.setdata.eqlistscroll) {
    //             dingyizhizhixingyici = 0
    //             setTimeout(() => {
    //               if (djfijweif == 0) {
    //                 if (index == lastindex + 1 && index > 2000) {
    //                   sameindex++
    //                   if (sameindex > 40) {
    //                     item.scrollTop = 0
    //                     index = 0
    //                     lastindex = 0
    //                     djfijweif = 1
    //                   }
    //                 }
    //               }
    //             }, 50);
    //             if (index < maxindex) {
    //               //如果正常滚动
    //               if (item.scrollTop == lastindex) {
    //                 //官方方法 ↓，但是只能跳转到指定元素位置
    //                 // var r = this.$refs['ITEM'].scrollToElement({
    //                 //   index: index,
    //                 //   top: 47,
    //                 // })
    //                 item.scrollTop = index
    //                 lastindex = index
    //                 index++
    //                 djfijweif = 0
    //               }
    //               else if (item.scrollTop - lastindex > 10) {
    //                 //被手动了
    //                 if (zhixingyici == 0) {
    //                   zhixingyici = 1
    //                   setTimeout(() => {
    //                     if (zhitanyici == 0) {
    //                       zhitanyici = 1
    //                       MessagePlugin.info('连击5次标题可以暂停自动滚动哦！')
    //                     }
    //                     item.scrollTop = index
    //                     lastindex = index
    //                   }, 1500);
    //                 }
    //                 else {
    //                   setTimeout(() => {
    //                     zhixingyici = 0
    //                   }, 1500);
    //                 }
    //               }
    //             }
    //             else {
    //               item.scrollTop = 0
    //               index = 0
    //             }

    //           }
    //           else {
    //             //滚动途中关闭了
    //             if (dingyizhizhixingyici == 0) {
    //               dingyizhizhixingyici = 1
    //               item.scrollTop = 0
    //               index = 0
    //               lastindex = 0
    //               djfijweif = 1
    //             }
    //           }
    //         }, 50);
    //       }
    //     }, 2000);
    //   }
    // }

    //渲染图表

    setTimeout(() => {
      Chart1 = echarts.init(document.getElementById('lendcharts'), null, { renderer: 'svg' })
      Chart2 = echarts.init(document.getElementById('serverun'), null, { renderer: 'svg' })
      this.connws()
      
      this.echartsInit()

      //首次加载执行
      this.refreshview()
    }, 1000);

    //缩放自适应
    window.onresize = () => {
      this.refreshview()
    };
  },
  methods: {
    //初始化echarts
    echartsInit() {
      //借出数据折线图
      Chart1.setOption({
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        },
        yAxis: {
          type: 'value'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          padding: 0,
          bottom: '15px',
          textStyle: {
            color: 'var(--td-text-color-primary)'
          },
        },
        grid: { // 让图表占满容器
          top: "8px",
          left: "24px",
          right: "24px",
          bottom: "70px"
        },
        series: [
          {
            name: '本周借出量',
            type: 'line',
            stack: 'Total',
            color: '#0052d9',
            data: this.$data.lenddata_thisweek,
            symbolSize: 8,
            symbol: 'circle',
            lineStyle: {
              width: 2,
            },
            areaStyle: {
              color: 'rgba(0,82,217,0.2)'
            },
            emphasis: {
              disabled: false,
              lineStyle: {
                width: 3,
              },
            },
          },
          {
            name: '上周借出量',
            type: 'line',
            color: '#2ba471',
            data: this.$data.lenddata_lastweek,
            symbolSize: 8,
            symbol: 'circle',
            lineStyle: {
              width: 2,
            },
            emphasis: {
              disabled: false,
              lineStyle: {
                width: 3,
              },
            },
          },
        ]
      })
    },
    systemchartinit() {
      //服务运行图表
      Chart2.setOption({
        tooltip: {
          trigger: 'item'
        },
        legend: {
          selectedMode: false,
          bottom: '14px',
          left: 'center',
          itemHeight: 4,
          itemWidth: 13,
          textStyle: {
            color: 'var(--td-text-color-primary)'
          }
        },
        color: ['#0052d9', '#d54941'],
        series: [
          {
            top: -30,
            name: '系统服务运行状态',
            type: 'pie',
            radius: ['45%', '60%'],
            avoidLabelOverlap: false,
            selectedMode: false,
            cursor: 'default',
            tooltip: {
              show: false,
            },
            label: {
              show: true,
              fontSize: 20,
              color: 'var(--td-text-color-primary)',
              formatter: [
                '{a|{d}%}',
                '{b|{b}占比}'
              ].join('\n'),
              rich: {
                a: {
                  fontFamily: 'PingFang SC, Microsoft YaHei, Arial Regular',
                  fontSize: '28px',
                  fontWeight: '500',
                  lineHeight: 45,
                },
                b: {
                  margin: '10px',
                  fontFamily: 'PingFang SC, Microsoft YaHei, Arial Regular',
                  fontSize: '13px',
                  color: 'var(--td-gray-color-8)',
                },
              },
              position: 'center'
            },
            emphasis: {
              disabled: true,
            },
            labelLine: {
              show: false
            },
            data: [
              { value: this.$data.sys_normal, name: '服务正常' },
              { value: this.$data.sys_unusual, name: '服务异常' },
            ]
          }
        ]
      })
    },
    //关闭/开启设备排行滚动
    onclick_eqlist_title() {
      this.$data.setdata.eqlistscrollnum++
      if (this.$data.setdata.eqlistscrollnum == 5) {
        if (this.$data.setdata.eqlistscroll) {
          //要关闭
          this.$data.setdata.eqlistscroll = false
          MessagePlugin.success('关闭列表滚动成功！')
        }
        else {
          //要开启
          this.$data.setdata.eqlistscroll = true
          MessagePlugin.success('开启列表滚动成功！')
        }
        //还原
        this.$data.setdata.eqlistscrollnum = 0
      }
    },
    //ws连接
    connws() {
      var thisdata = this.$data
      if (thisdata.devmode.request) {
        if (thisdata.devmode.ws_req) {
          var that = this
          var socket = new WebSocket("ws://10.3.146.103:7776/ws/getinfo/getsystemstate")
          socket.onopen = function () {
            socket.send("get")
            setInterval(() => {
              socket.send("get")
            }, 30000);
          }
          var xiajibaluanxiedebianliangming = 0
          // 监听socket消息
          socket.onmessage = function (msg) {
            var res = JSON.parse(msg.data)
            that.$data.sys_normal = res.normal
            that.$data.sys_unusual = res.unusual
            if (xiajibaluanxiedebianliangming == 1) {
              Chart2.resize()
              // document.getElementById('serverun').removeAttribute('_echarts_instance_');
              // setTimeout(() => {
              //   document.getElementById('serverun').getElementsByTagName("div")[0].remove()
              //   document.getElementById('serverun').getElementsByTagName("div")[0].remove()
              // }, 1000);
            }
            else {
              xiajibaluanxiedebianliangming = 1
            }
            that.systemchartinit()
          }
          socket.onclose = function () {
            that.connws()
          }
        }
      }
    },
    RequestDATA() {
      var thisdata = this.$data
      if (thisdata.devmode.request) {
        if (thisdata.devmode.http_req) {
          //天气
          axios.get(url + '/api/weather', {}).then((res) => {
            if (res.data.errcode == -1) {
              var pattern = /\w+.js:\d+/
              MessagePlugin.error('请求出错：' + res.data.errmsg)
            }
            else {
              var a = {}
              a.temperature = parseInt(res.data.data.data[0].live.temperature)
              a.report_time = res.data.data.data[0].report_time
              a.weather_name = res.data.data.data[0].live.weather_name
              a.max_temp = res.data.data.data[0].forecast_data[0].max_temp
              a.min_temp = res.data.data.data[0].forecast_data[0].min_temp
              if (res.data.data.data[0].live.weather_name == "晴") {
                this.$data.imgu = require('../../assets/wea/w0.png')
              }
              else if (res.data.data.data[0].live.weather_name == "多云") {
                this.$data.imgu = require('../../assets/wea/w1.png')
              }
              else if (res.data.data.data[0].live.weather_name == "阴") {
                this.$data.imgu = require('../../assets/wea/w2.png')
              }
              else if (res.data.data.data[0].live.weather_name == "小雨") {
                this.$data.imgu = require('../../assets/wea/w7.png')
              }
              else if (res.data.data.data[0].live.weather_name == "中雨") {
                this.$data.imgu = require('../../assets/wea/w8.png')
              }
              else if (res.data.data.data[0].live.weather_name == "大雨") {
                this.$data.imgu = require('../../assets/wea/w9.png')
              }
              else if (res.data.data.data[0].live.weather_name == "暴雨") {
                this.$data.imgu = require('../../assets/wea/w10.png')
              }
              else if (res.data.data.data[0].live.weather_name == "雷阵雨") {
                this.$data.imgu = require('../../assets/wea/w10.png')
              }
              else if (res.data.data.data[0].live.weather_name == "雾") {
                this.$data.imgu = require('../../assets/wea/w11.png')
              }
              else {
                this.$data.imgu = require('../../assets/wea/w0.png')
              }
              this.$data.tempdata = a
            }
          })
          //借出数据折线图数据
          axios.get(url + '/api/getinfo/lenddata', {}).then((res) => {
            if (res.data.errcode == -1) {
              var pattern = /\w+.js:\d+/
              MessagePlugin.error('请求出错：' + res.data.errmsg)
            }
            else {
              var lenddata = res.data
              this.$data.lenddata_lastweek = lenddata[0]
              this.$data.lenddata_thisweek = lenddata[1]
              this.echartsInit()
            }
          })
          //设备借出量数据
          axios.get(url + '/api/getinfo/recentlist?type=2', {}).then((res) => {
            if (res.data.errcode == -1) {
              var pattern = /\w+.js:\d+/
              MessagePlugin.error('请求出错：' + res.data.errmsg)
            }
            else {
              var recentlist = res.data
              var a = []
              for (var index = 0; index < recentlist.length; index++) {
                const element = recentlist[index];
                var res = element.list
                var id = index + 1
                for (let key = 0; key < res.length; key++) {
                  const childer = res[key];
                  var b = {
                    id: id,
                    name: childer.name,
                    code: childer.code,
                    time: childer.time,
                  }
                  a.push(b)
                  //循环结束
                  if (key == res.length - 1 && index == recentlist.length - 1) {
                    this.$data.eqlistsas_data = a
                    this.$data.eqlistsas_data.length = 5
                  }
                }
              }
            }

          })
          //顶部数据
          axios.get(url2 + '/json/getinfo/topdata', {}).then((res) => {
            if (res.data.errcode == -1) {
              var pattern = /\w+.js:\d+/
              MessagePlugin.error('请求出错：' + res.data.errmsg)
            }
            else {
              this.$data.topdata = res.data.data
            }
          })
          //活跃用户
          axios.get(url + '/api/getinfo/useractive', {}).then((res) => {
            if (res.data.errcode == -1) {
              var pattern = /\w+.js:\d+/
              MessagePlugin.error('请求出错：' + res.data.errmsg)
            }
            else {
              //res.data[0]是原始数据
              //res.data[1]是以周为单位计算的数据
              //res.data[2]是以日为单位计算的数据
              //res.data[1][0]是本周
              //res.data[1][2]是上周
              //res.data[2][0]是今天
              //res.data[2][1]是昨天
              var result = res.data
              this.$data.onlineuser.fromdata = result
              this.$data.onlineuser.data = result[2][0]
              this.$data.onlineuser.desc = '昨天'
              this.$data.onlineuser.stand = '日'
              var lastday = result[2][1]
              var today = result[2][0]
              var pre_l_t = today - lastday
              var jisuan = pre_l_t / lastday
              var pre_res = ''
              var pre_desc = false
              //下降
              if (jisuan < 0) {
                pre_res = (Math.abs(jisuan) * 100).toFixed(2)
                pre_desc = false
                // this.$data.onlineuser.pre = pre_res
              }
              //上升
              else if (jisuan > 0) {
                pre_res = (Math.abs(jisuan) * 100).toFixed(2)
                pre_desc = true
                if (pre_res == 'Infinity') {
                  pre_res = 100
                }
                // this.$data.onlineuser.pre = pre_res
              }
              else if (jisuan == 0) {
                var pre_res = '0'
                pre_desc = true
              }
              else {
                var pre_res = '0'
              }
              this.onlineuser.pre = pre_res
              this.onlineuser.preway = pre_desc
            }
          })
          //借出列表
          axios.get(url2 + '/json/recordlist', {}).then((res) => {
            if (res.data.errcode == -1) {
              MessagePlugin.error('请求出错：' + res.data.errmsg)
            }
            else {
              res.data.data.length = res.data.length
              var a = []
              for (let index = 0; index < res.data.length; index++) {
                const element = res.data.data[index];
                a.push(element)
                if (index == res.data.length - 1) {
                  thisdata.recordlist_data = a
                }
              }
            }
          })
        }
      }
    },

    refreshview() {
      Chart1.resize()
      Chart2.resize()
      //可视区域
      var can_look_height = window.innerHeight
      //第三组头部位置
      var list3top = document.getElementById("ran-list-3").offsetTop
      if (can_look_height <= 1080) {
        let a = can_look_height - 770
        document.getElementById("recordbig").style.height = a + 'px'
        document.getElementById("eqlistsasbig").style.height = a + 'px'
        document.getElementById("eqlistsasitem").style.height = '235px'
        document.getElementById("headmenu").style.top = '-56px'
      }
      else {
        let a = can_look_height - 830
        document.getElementById("recordbig").style.height = a + 'px'
        document.getElementById("eqlistsasbig").style.height = a + 'px'
        document.getElementById("eqlistsasitem").style.height = ''
        document.getElementById("headmenu").style.top = '0px'
      }
    },

    //刷新图表
    refresh_charts: function () {
      Chart1.resize()
      Chart2.resize()
    },

    headmoveout() {
      document.getElementById("headmenu").style.top = "-56px"
    },
    headmoveover() {
      document.getElementById("headmenu").style.top = "0px"
    },
    //自定义函数
    getQueryString(name) {
      let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
      let r = window.location.search.substring(1).match(reg);
      if (r != null) {
        return decodeURIComponent(r[2]);
      };
      return null;
    },
  }
}
</script>
  
<style>
/**主要 */
body {
  margin: 0px;
  background: var(--td-bg-color-page);
  margin: 0 auto;
  height: 100%;
}

/**顶部5位的样式 */
/**蓝色的 */
[ran-bg-color-blue] {
  background-color: #0052d9 !important;
}

[ran-bg-color-blue]>div.t-card__body {
  background-color: #0052d9 !important;
}

[ran-bg-color-blue] .t-card__title {
  color: var(--td-text-color-anti) !important;
}

/**原来表格覆盖的css
[ran-bg-color-blue]>div>div>div>div>svg>g>text {
  display: none !important;
}

[ran-bg-color-blue]>div>div>div>div>svg>g>path {
  display: none !important;
}

[ran-bg-color-blue]>div>div>div>div>svg>g>g>path[fill-opacity="0.7"] {
  display: none !important;
}
 */

/**红色的 */
[ran-bg-color-red] {
  background-color: var(--td-error-color) !important;
}

[ran-bg-color-red]>div.t-card__body {
  background-color: var(--td-error-color) !important;
}

[ran-bg-color-red] .t-card__title {
  color: var(--td-text-color-anti) !important;
}

/**绿色的 */
[ran-bg-color-green] {
  background-color: var(--td-success-color) !important;
}

[ran-bg-color-green]>div.t-card__body {
  background-color: var(--td-success-color) !important;
}

[ran-bg-color-green] .t-card__title {
  color: var(--td-text-color-anti) !important;
}

/**普通 */
[ran-bg-color-primary] .t-avatar {
  color: var(--td-text-color-primary) !important;
}


/**卡片主要样式，覆盖tdesign默认的 */
.t-card--bordered {
  border: none !important;
}

[ran-card] {
  height: 160px;
  border-radius: 6px;
}

[ran-card] .t-card__title {
  /* color: var(--td-text-color-secondary) !important; */
  font: var(--td-font-body-medium) !important;
  font-size: 15px !important;
}

[ran-card] .t-avatar {
  background: var(--ran-card-primary-bg-color) !important;
  color: var(--ran-card-primary-text-color) !important;
}

[ran-card] {
  padding: var(--td-comp-paddingTB-xl) var(--td-comp-paddingLR-xxl) !important;
}

[ran-card] .t-card__header {
  padding: 0 !important;
}

[ran-card] .t-card__footer {
  padding-bottom: 0;
  padding-left: 0;
  padding-right: 0;
  padding-top: 17px;
}

[ran-card] .t-card__body {
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  flex: 1 !important;
  position: relative !important;
  padding: 0 !important;
  margin-top: var(--td-comp-margin-s) !important;
  margin-bottom: var(--td-comp-margin-xxl) !important;
}

[ran-bg-color-green] .dashboard-item-block,
[ran-bg-color-red] .dashboard-item-block,
[ran-bg-color-blue] .dashboard-item-block {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  color: #fff !important;
}

/**活跃用户图标覆盖样式 */
[ran-charts-lastweekuser]>div>svg>g>path[fill="none"] {
  display: none !important;
}

[ran-charts-lastweekuser]>div>svg>g>text {
  display: none !important;
}

/**组样式区域 */
[ran-list-big] {
  display: flex !important;
}

/**下面还有一个组（空出一段距离） */
[ran-list-big-xmhyygz] {
  margin-bottom: 16px !important;
}

/**第二组 */
[ran-list-big-2] .t-card__header {
  padding: 32px 32px 0px 32px !important;
}

[ran-list-big-2] .t-card__title {
  font: var(--td-font-title-large) !important;
  font-weight: 400 !important;
}

/**第三组 */
[ran-list-big-3] .t-card {
  padding: 30px 32px 32px 32px !important;
}

[ran-list-big-3] .t-card__header,
[ran-list-big-3] .t-card__body {
  padding: 0 !important;
}

[ran-list-big-3] .t-card__title {
  font: var(--td-font-title-large) !important;
  font-weight: 400 !important;
}

/**每个组的子组件 */
[ran-top-card-item] {
  width: 550px !important;
  height: 160px;
  padding: 0px 8px !important;
}

/**服务状态图表样式 */
#serverun>div {
  cursor: default !important;
}

/**禁止用户选中 */
[ran-user-select-none] {
  user-select: none !important;
}



:root {
  --ran-card-primary-bg-color: rgb(255 255 255 / 26%) !important;
  --ran-card-primary-text-color: #fff !important;
}

:root[theme-mode="dark"] {
  --ran-card-primary-bg-color: rgb(255 255 255 / 26%) !important;
  --ran-card-primary-text-color: #fff !important;
}

/**从TdesignStarter拿的样式 */
.dashboard-item-trend {
  margin-left: var(--td-comp-margin-s) !important;
}

.trend-container__down {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.trend-container .trend-icon-container {
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 16px !important;
  height: 16px !important;
}

.trend-container__down .trend-icon-container {
  background: rgb(255 255 255 / 20%) !important;
  margin-right: 8px !important;
}

.dashboard-item-bottom {
  display: flex !important;
  flex-direction: row !important;
  justify-content: space-between !important;
  align-items: center !important;
}

.dashboard-item-block {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  color: var(--td-text-color-placeholder) !important;
}

.item-right {
  display: flex !important;
  flex-direction: row !important;
  align-items: flex-start !important;
  padding-top: 6px !important;
}

.item-right>span {
  font-size: 40px !important;
  color: #fff;
}

.item-top {
  position: absolute !important;
  top: 0 !important;
  right: 0 !important;
}


.weatherbig {
  width: 265px;
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0px 8px;
}


.margintop56 {
  height: 56px;
}


#lendcharts,
#serverun {
  width: 100%;
  height: 300px;
  position: relative;
}

/* 按设备屏幕尺寸大小挤一挤*/
@media screen and (max-height: 1080px) {

  #lendcharts,
  #serverun {
    width: 100%;
    height: 220px;
    position: relative;
  }

  [ran-top-card-item],
  [ran-card] {
    height: 140px;
  }

  [ran-card] .t-card__footer {
    padding-top: 0px;
  }

  .weatherbig {
    height: 140px;
  }

  [ran-list-big-3] .t-card {
    padding: 28px 32px 32px 30px !important
  }

  .margintop56 {
    height: 0px;
  }

  .menu {
    top: -133px !important;
  }
}
</style>