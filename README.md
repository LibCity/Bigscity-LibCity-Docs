基于[Sphinx](http://sphinx-doc.org/)的项目文档

两种部署的方式：

（1）[Read the Docs](https://readthedocs.org/)

访问：https://bigscity-trafficdl-docs.readthedocs.io/zh_CN/latest/

更新方法：每次将修改推送到github后，Read the Docs会自动拉取最新的提交，自动更新最新版网站。

（2）[Github Page](https://pages.github.com/)

访问：https://aptx1231.github.io/Bigscity-TrafficDL-Docs/

更新方法：每次修改后，需要在本地手动`make html`以得到最新版网页内容，内容存储于`/build`目录，之后将`/build/html/`目录下的内容复制到`docs/`目录下，之后将`docs/`目录下的内容也要提交到Github，之后Github Page会自动更新为最新版内容。



Sphinx简明使用：

安装：

```
pip install Sphinx==3.3.1
```

> 注意版本号，不要使用3.4及以上

安装样式主题：

```
pip install sphinx_rtd_theme
```

项目初始化

```shell
mkdir Bigscity-TrafficDL-Docs
cd Bigscity-TrafficDL-Docs
sphinx-quickstart
> Separate source and build directories (y/n) [n]: y    # source与build分离
> Project name: Bigscity-TrafficDL-Docs         # 项目名
> Author name(s): aptx1231                      # 作者名
> Project release []:                           # 回车                 
```

目录结构

```shell
├── build           # 输出文件夹
├── make.bat
├── Makefile        # 编译文件
└── source          # 源文件夹
    ├── conf.py     # Sphinx的配置文件
    ├── index.rst
    ├── _static
    └── _templates
```

