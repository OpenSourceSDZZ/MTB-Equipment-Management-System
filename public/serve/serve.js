//import
const axios = require('axios');
var express = require('express');
var app = express();
var mysql = require('mysql');
var ws = require("nodejs-websocket")
const dayjs = require('dayjs')
var weekOfYear = require('dayjs/plugin/weekOfYear')
dayjs().format()
dayjs.extend(weekOfYear)
var thisweekofyear = dayjs().week()
var dayofweek = dayjs().day()
process.on('uncaughtException', function (err) {
    //打印出错误
    console.log(err)
});

//variable
var mysqlzm = {
    host: '192.168.68.100',
    user: 'mtb',
    password: 'admin@sdzz_mtb_mysql2109',
    port: '3306',
    database: 'mtb'
}
// PS：
// 全部接口内容不会返回敏感信息以及可操控性
// 全部返回数据均脱敏返回

//index
app.get('/', function (req, res) {
    //默认标头
    res.setHeader("Content-Type", "application/json")
    res.setHeader('Access-Control-Allow-Origin', '*')
    res.end("Not Allow Address")
})

//API LIST

//weather Updata date:20230216
app.get('/api/weather', function (req, res) {
    //默认标头
    res.setHeader("Content-Type", "application/json")
    res.setHeader('Access-Control-Allow-Origin', '*')

    axios.get('https://amap.com/service/weather?adcode=440600')
        .then(resu => {
            res.end(JSON.stringify(resu.data))
        })
        .catch(err => {
            res.end(JSON.stringify({ "errcode": -1, "errmsg": "后端请求失败", "desc": err.message }));
        });
})

//获取周借出次数列表,[0]为上周 [1]为本周 Write date:20230220 Fix date:20230223
app.get('/api/getinfo/lenddata', function (req, res) {
    //默认标头
    res.setHeader("Content-Type", "application/json")
    res.setHeader('Access-Control-Allow-Origin', '*')
    // if (req.method == 'POST') {
    try {
        var dashboardconn = mysql.createConnection(mysqlzm);
        dashboardconn.connect(function (err) {
            if (err) {
                res.end(JSON.stringify({ "errcode": -1, "errmsg": err.code, "desc": err.sqlMessage }));
            }
        });
        var sql = 'SELECT * FROM dashboardDATA';
        dashboardconn.query(sql, function (err, result) {
            if (err) {
                res.end('[SELECT ERROR] - ', err.message);
            }
            //直接返回数据↓
            // res.end(JSON.stringify(result));
            //处理完在返回
            //非空结果
            if (result) {
                var lastweekdata = [0, 0, 0, 0, 0, 0, 0]
                var thisweekdata = ['-', '-', '-', '-', '-', '-', '-']
                //处理数据
                for (let i = 0; i < result.length; i++) {
                    const element = result[i];

                    //lastweek
                    if (thisweekofyear - 1 == element.week) {
                        if (element.day == 0) {
                            //周日
                            lastweekdata[6]++
                        }
                        else if (element.day == 1) {
                            //周一
                            lastweekdata[0]++
                        }
                        else if (element.day == 2) {
                            //周二
                            lastweekdata[1]++
                        }
                        else if (element.day == 3) {
                            //周三
                            lastweekdata[2]++
                        }
                        else if (element.day == 4) {
                            //周四
                            lastweekdata[3]++
                        }
                        else if (element.day == 5) {
                            //周五
                            lastweekdata[4]++
                        }
                        else if (element.day == 6) {
                            //周六
                            lastweekdata[5]++
                        }
                    }
                    //thisweek
                    else if (thisweekofyear == element.week) {
                        if (element.day == 0) {
                            //周日
                            if (thisweekdata[6] == '-') {
                                thisweekdata[6] = 1
                            }
                            else {
                                thisweekdata[6]++
                            }
                        }
                        else if (element.day == 1) {
                            //周一
                            if (thisweekdata[0] == '-') {
                                thisweekdata[0] = 1
                            }
                            else {
                                thisweekdata[0]++
                            }
                        }
                        else if (element.day == 2) {
                            //周二
                            if (thisweekdata[1] == '-') {
                                thisweekdata[1] = 1
                            }
                            else {
                                thisweekdata[1]++
                            }
                        }
                        else if (element.day == 3) {
                            //周三
                            if (thisweekdata[2] == '-') {
                                thisweekdata[2] = 1
                            }
                            else {
                                thisweekdata[2]++
                            }
                        }
                        else if (element.day == 4) {
                            //周四
                            if (thisweekdata[3] == '-') {
                                thisweekdata[3] = 1
                            }
                            else {
                                thisweekdata[3]++
                            }
                        }
                        else if (element.day == 5) {
                            //周五
                            if (thisweekdata[4] == '-') {
                                thisweekdata[4] = 1
                            }
                            else {
                                thisweekdata[4]++
                            }
                        }
                        else if (element.day == 6) {
                            //周六
                            if (thisweekdata[5] == '-') {
                                thisweekdata[5] = 1
                            }
                            else {
                                thisweekdata[5]++
                            }
                        }
                    }
                    //循环结束
                    if (i == result.length - 1) {
                        for (let index = 1; index < thisweekdata.length; index++) {
                            if (thisweekdata[dayofweek - index] == '-' && dayofweek != 0) {
                                thisweekdata[dayofweek - index] = 0
                            }
                        }
                        //延时防止并发
                        setTimeout(() => {
                            var a = []
                            a.push(lastweekdata)
                            a.push(thisweekdata)
                            var data = { "errcode": 0, "errmsg": "ok", "data": a }
                            res.end(JSON.stringify(data));
                        }, 200);
                    }
                }
            }
            else {
                var lastweekdata = [0, 0, 0, 0, 0, 0, 0]
                var thisweekdata = ['-', '-', '-', '-', '-', '-', '-']
                var disc = { "errcode": -2, "errmsg": "数据库数据为空" }
                var a = []
                a.push(lastweekdata)
                a.push(thisweekdata)
                a.push(disc)
                res.end(JSON.stringify(a));
            }
        });
        dashboardconn.end();
    }
    catch {
        throw new Error()
    }
    // }
    // else {
    //     res.end("Not Allow Methods")
    // }
})

//获取借出设备次数列表 Updata date:20230221
/*type [1,2] [1] [返回结果模式]*/
app.get('/api/getinfo/recentlist', function (req, res) {
    //默认标头

    res.setHeader("Content-Type", "application/json")
    res.setHeader('Access-Control-Allow-Origin', '*')
    //Get Query
    var get_type = req.query.type
    var post_type = ''
    if (req.body) {
        post_type = req.body.type
    }
    // if (req.method == 'POST') {
    try {
        var recentlistconn = mysql.createConnection(mysqlzm);
        recentlistconn.connect(function (err) {
            if (err) {
                res.end(JSON.stringify({ "errcode": -1, "errmsg": err.code, "desc": err.sqlMessage }));
            }
        });
        var sql = 'SELECT * FROM record';
        recentlistconn.query(sql, function (err, result) {
            if (err) {
                res.end('[SELECT ERROR] - ', err.message);
            }
            //直接返回数据↓
            //res.end(JSON.stringify(result));
            //处理完在返回
            for (let index = 0; index < result.length; index++) {
                var c = []
                let obj = {}
                //计算出现次数
                for (let i = 0; i < result.length; i++) {
                    var key = result[i].equipment_code
                    if (obj[key]) {
                        obj[key] += 1
                    } else {
                        obj[key] = 1
                    }
                }
                //重组数据
                for (const keys in obj) {
                    if (Object.hasOwnProperty.call(obj, keys)) {
                        const element99 = obj[keys];
                        var d = {
                            name: '设备名称出错！！！',
                            code: keys,
                            time: element99,
                        }
                        c.push(d)
                    }
                }
            }
            //获取设备信息
            for (let il = 0; il < c.length; il++) {
                var element66 = c[il];
                var recentlist2conn = mysql.createConnection(mysqlzm);
                recentlist2conn.connect();
                var sql2 = "SELECT *  FROM `equipment` WHERE `code` LIKE '" + element66.code + "'";
                recentlist2conn.query(sql2, function (err, result2) {
                    if (err) {
                        res.end('[SELECT ERROR] - ', err.message);
                        return;
                    }
                    //直接返回数据↓
                    //res.end(JSON.stringify(result));
                    //处理完在返回
                    if (result2[0]) {
                        c[il].name = result2[0].name
                        if (il == c.length - 1) {
                            //防止设备名称出不来
                            setTimeout(() => {
                                //第二种返回方式
                                //返回为排名结果
                                if (get_type == '2' || post_type == '2') {
                                    //临走前排个序
                                    function sortIdDesc(a, b) {
                                        return b.time - a.time
                                    }
                                    var returndata = c.sort(sortIdDesc)
                                    /**
                                     * 再次格式化
                                     * @param {[type]} arr [数据源]
                                     * @param {[type]} field [字段名]
                                    */
                                    function groupingData(data, filed) {
                                        // map用来保存存过的字段 为下边添加新对象或者将相同字段的数据保存到同一个list中
                                        let map = {};
                                        // dest主要保存分组后的数据
                                        let dest = [];
                                        // 循环遍历传入的data
                                        data.forEach(item => {
                                            // 判断map对象中是否有遍历时data的key 如果没有则向dest数组中推入一个新的对象(包含两个属性，一个要分组的字段名，一个保存相同字段名数据的数组)
                                            if (!map[item[filed]]) {
                                                dest.push({
                                                    [filed]: item[filed],
                                                    list: [item]
                                                });
                                                // 进行一次新添对象的记录
                                                map[item[filed]] = item;
                                                // 如果在map中有data遍历的key(字段相同) 则向dest数组里面的相同字段的list下推入数据
                                            } else {
                                                dest.forEach(dItem => {
                                                    if (dItem[filed] == item[filed]) {
                                                        dItem.list.push(item);
                                                    }
                                                });
                                            }
                                        })
                                        return dest;
                                    }
                                    let resddd = groupingData(returndata, 'time');
                                    //送走！！
                                    res.end(JSON.stringify(resddd));
                                }
                                //第一种返回方式
                                //返回为数据结果
                                else {
                                    //临走前排个序
                                    function sortIdDesc(a, b) {
                                        return b.time - a.time
                                    }
                                    var returndata = JSON.stringify(c.sort(sortIdDesc))
                                    //送走！！
                                    res.end(returndata);
                                }
                            }, 300);
                        }
                    }
                });
                recentlist2conn.end();
            }
        });
        recentlistconn.end();
    }
    catch {
        throw new Error()
    }
    // }
    // else {
    //     res.end("Not Allow Methods")
    // }
})

//获取用户活跃列表 Updata date:20230222
app.get('/api/getinfo/useractive', function (req, res) {
    //默认标头
    res.setHeader("Content-Type", "application/json")
    res.setHeader('Access-Control-Allow-Origin', '*')

    var a = []
    var b = []
    if (req.body) {
        post_type = req.body.type
    }
    // if (req.method == 'POST') {
    try {
        var recentlistconn = mysql.createConnection(mysqlzm);
        recentlistconn.connect(function (err) {
            if (err) {
                res.end(JSON.stringify({ "errcode": -1, "errmsg": err.code, "desc": err.sqlMessage }));
            }
        });
        var sql = 'SELECT * FROM dashboardDATA2';
        recentlistconn.query(sql, function (err, result) {
            if (err) {
                res.end('[SELECT ERROR] - ', err.message);
            }
            //直接返回数据↓
            //res.end(JSON.stringify(result));
            //处理完在返回
            //返回结果 [0]为原始数据 [1]为以周为单位的数据 [2]为以天为单位的数据
            //计算周数
            if (result) {
                //一次分类
                var tttime = 0
                var tttime2 = 0
                //二次分类
                var abc = 0
                var abc2 = 0
                for (let index = 0; index < result.length; index++) {
                    const element = result[index];
                    b.push(element)
                    //计算出现次数
                    if (result[index].week == thisweekofyear) {
                        tttime++
                    }
                    else if (result[index].week == thisweekofyear - 1) {
                        tttime2++
                    }
                    if (index == result.length - 1) {
                        //[0]本周[1]上周
                        var c = [tttime, tttime2]
                        a.push(b)
                        a.push(c)
                        for (let i = 0; i < result.length; i++) {
                            //计算出现次数
                            if (result[i].week == thisweekofyear) {
                                if (result[i].day == dayofweek) {
                                    abc++
                                }
                                if (result[i].day == dayofweek - 1) {
                                    abc2++
                                }
                            }
                            if (i == result.length - 1) {
                                //[0]今天[1]昨天
                                var d = [abc, abc2]
                                a.push(d)
                                res.end(JSON.stringify(a))
                            }
                        }
                    }
                }
            }
            else {
                var e = [{ "errcode": -2, "errmsg": "数据库数据为空" }]
                res.end(JSON.stringify(e));
            }

        });
        recentlistconn.end();
    }
    catch {
        throw new Error()
    }
    // }
    // else {
    //     res.end("Not Allow Methods")
    // }
})

function errorHandler(err, req, res, next) {
    res.end(JSON.stringify({ "errcode": -1, "errmsg": err.stack }));
}
app.use(errorHandler);

// HTTP
var server = app.listen(7775, function () {
    // var host = server.address().address
    var port = server.address().port
    console.log("HTTP服务加载成功，服务地址 127.0.0.1:%s", port)
})

// Websocket
var wsserver = ws.createServer(connect => {
    var path = connect.path
    //默认发什么过来返回什么
    connect.on("text", data => {
        //获取系统运行状态
        if (path == '/ws/getinfo/getsystemstate' && data == 'get') {
            var zhengchang = 90.2
            var yichang = 9.8
            var a = {
                normal: zhengchang,
                unusual: yichang,
            }
            connect.send(JSON.stringify(a))
        }
        else {
            connect.send(data)
        }
    })

    //监听websocket断开链接
    connect.on("close", () => {
        console.log("websocket连接断开....")
    })

    //监听websocket异常信息
    connect.on("error", () => {
        console.log("websocket连接异常....")
    })
})
wsserver.listen(7776, () => {
    console.log("WebSocket服务加载成功，服务地址 127.0.0.1:7776")
})