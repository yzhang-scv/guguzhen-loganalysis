# guguzhen-loganalysis

咕咕镇战斗记录转计算器PC数据工具

由于目前不分析具体的战斗记录只是脑补对面的装备以及大致根据图标推断点数，**会与实际产生极大的误差**

本项目基于pycharm开发，建议环境python 3.9，并根据requirements安装依赖

更新日志： https://kf.miaola.work/read.php?tid=976407&sf=aa2

关于压缩包内计算器的说明:

b大计算器：https://kf.miaola.work/read.php?fid=86&tid=807309&sf=407

解压release的压缩包，将压缩包内的newkf_64.exe覆盖至b大计算器的目录里

装备 彩金对剑 COLORFUL 猎魔耳环 HUNT 清澄长杖 LIMPIDWAND 折光戒指 REFRACT 凶神耳环 FIERCE

天赋 不动如山 SHAN

樱桃 全属性 AAA 暴击抵抗 CRTR 技能抵抗 SKLR

卡片雅名称YA，用M=指定雅的模式 0白天1黑夜，表示白天的雅例子 YA M=0 850 1100 7 11

野怪 史莱姆 SHI

使用方法：

收割机脚本：https://kf.miaola.work/read.php?fid=5&tid=1000914&sf=823

解压release的压缩包，由于新装备的存在，暂时需要配合压缩包内的计算器使用

更新最新的咕咕镇剩余价值收割机脚本，点击咕咕镇页面左侧脚本下拉处的导出历史按钮，将文件复制到项目source目录中

如果有多个号将多个导出历史文件一并复制进解压后的source目录中（文件名不能为pc.txt），程序运行后会自动整合多个文件的记录

最后根据自身需求修改config.yaml配置，运行main.exe，会在source目录下生成pc.txt文件

注意，通过主题插件自定义装备图片的情况下程序无法获取装备品质，此时默认对手全为非红装，请尽量使用插件默认主题或不使用插件

最后，感谢五神、熊大、Mulexe、kizunahitotsu为本项目提供建议与测试数据

Q:能读取战斗记录吗，误差太大了

A:不能，这是要搞死我，也没那么多时间，如果pc出现过于离谱加点的情况请提供pc和相关战斗记录的截图提交issue

Q:写的啥玩意，什么垃圾代码

A:python没咋学过，这很正常，你骂的对

Q:**咕咕镇垃圾游戏，请不要氪金咕咕镇，氪金不会变强还会被PUA！**

A:附议
