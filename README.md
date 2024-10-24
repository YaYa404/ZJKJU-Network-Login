## ZJKJU-Network-Login
苦恼于校园网老是把设备踢下线导致网络波动，故制作此脚本，理论上锐捷登录是通用的，使用于新湖校区升级后的校园网，麻章校区网络没测速过

## 使用
请先搭建好python运行环境

1. 连接上校园网

2. 用编辑器打开ZJKJU_Login.py的修改里面的CONFIG配置参数，参数对应如图

![Image](https://raw.githubusercontent.com/YaYa404/ZJKJU-Network-Login/refs/heads/main/config.png)

3. 运行<code>pip install -r requirements.txt</code>

4. 运行ZJKJU_Login.py脚本

## docker
如果想用docker请自行构建，<code>Dockerfile</code>文件已经准备好了

但是没有把config参数分离出来，仍然需要根据上面的步骤配置

配置完成后运行<code>docker build -t zjkju-login .</code>

如果人要用的人多的话我可以考虑弄一下这docker容器

## 碎碎念
悄悄告诉你如果想把校园网接上路由器的话修改TTL和NTP就行了

如果需要请自行百度，网上教程实在多得数不过来，最简单的是用openwrt系统进行修改
