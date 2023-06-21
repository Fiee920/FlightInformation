# 航班价格变动监控

`Auth：Fiee`

## 项目简介

通过Python脚本，从携程旅行网，获取指定日期和城市之间的航班信息，并升序显示两条航班信息及价格。配合GitHub中的Action，可实现每日定点自动运行，并推送到微信。

## demo

[<img src="https://s1.ax1x.com/2023/06/21/pCGoxGq.jpg" alt="pCGoxGq.jpg" style="zoom:25%;" />](https://imgse.com/i/pCGoxGq)

## 配置

在`config.py`中，需要修改以下信息确保脚本正确运行

- dCity 表示出发城市
- aCity 表示到达城市
- date1 - date3 支持三天的查询预设
- `app_id` `app_secret` `user_id` `template_id` 均需要从微信公众平台进行获取并正确填写
- main.yml文件需要手动进行配置，自动运行需要正确书写`cron表达式`

> https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login
>
> 以上链接为微信公众平台测试号申请地址，使用微信扫码登陆即可正常使用

## About

⚠ 忽略屎山代码

`out`类预留了控制台输出，对象属性`message`会输出到控制台

目前仅完成微信推送，`sendEmail.py`未开发

查询接口具有时效性，不保证长期可用。最终解释权归©携程旅行所有