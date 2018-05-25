# Github Trends

A script that provides information about the most popular projects in last 7 days from [Github](https://github.com/)
If the project from the list has open issues, issues list will be displayed also.

Script works with [Github API](https://api.github.com/search/repositories)

## Requirements
Python 3 should be already installed.
 Dependencies:

1.  [Requests library](http://docs.python-requests.org/en/master/)
 
Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:
```bash
pip install -r requirements.txt
```
For better interaction is recommended to use [virtualenv](https://github.com/pypa/virtualenv).

### Example input
```bash
python github_trending.py
```

### Example output

```bash
Repo: https://api.github.com/repos/mimecorg/vuido, stargazers count: 991
Issues count: 6
	Issue url: https://api.github.com/repos/mimecorg/vuido/issues/10
	Issue url: https://api.github.com/repos/mimecorg/vuido/issues/9
	Issue url: https://api.github.com/repos/mimecorg/vuido/issues/8
	Issue url: https://api.github.com/repos/mimecorg/vuido/issues/7
	Issue url: https://api.github.com/repos/mimecorg/vuido/issues/6
	Issue url: https://api.github.com/repos/mimecorg/vuido/issues/4
Repo: https://api.github.com/repos/eleme/UETool, stargazers count: 544
Issues count: 0
Repo: https://api.github.com/repos/1-Sisyphe/youCanCodeAGif, stargazers count: 298
Issues count: 0
Repo: https://api.github.com/repos/GoogleChromeLabs/css-paint-polyfill, stargazers count: 266
Issues count: 1
	Issue url: https://api.github.com/repos/GoogleChromeLabs/css-paint-polyfill/issues/2
Repo: https://api.github.com/repos/xiaomuzhu/vue-ts-daily, stargazers count: 258
Issues count: 0
Repo: https://api.github.com/repos/intuit/CardParts, stargazers count: 244
Issues count: 0
Repo: https://api.github.com/repos/beyondcode/laravel-credentials, stargazers count: 227
Issues count: 0
Repo: https://api.github.com/repos/sdras/night-owl-vscode-theme, stargazers count: 211
Issues count: 10
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/34
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/33
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/29
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/27
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/26
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/25
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/21
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/19
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/12
	Issue url: https://api.github.com/repos/sdras/night-owl-vscode-theme/issues/10
Repo: https://api.github.com/repos/youngdro/ConsoleCanvas, stargazers count: 179
Issues count: 3
	Issue url: https://api.github.com/repos/youngdro/ConsoleCanvas/issues/3
	Issue url: https://api.github.com/repos/youngdro/ConsoleCanvas/issues/2
	Issue url: https://api.github.com/repos/youngdro/ConsoleCanvas/issues/1
Repo: https://api.github.com/repos/jamiebuilds/react-performance-observer, stargazers count: 130
Issues count: 0
Repo: https://api.github.com/repos/spatie/laravel-event-projector, stargazers count: 127
Issues count: 0
Repo: https://api.github.com/repos/confuser/graphql-constraint-directive, stargazers count: 124
Issues count: 1
	Issue url: https://api.github.com/repos/confuser/graphql-constraint-directive/issues/1
Repo: https://api.github.com/repos/lemire/fastvalidate-utf-8, stargazers count: 106
Issues count: 2
	Issue url: https://api.github.com/repos/lemire/fastvalidate-utf-8/issues/6
	Issue url: https://api.github.com/repos/lemire/fastvalidate-utf-8/issues/5
Repo: https://api.github.com/repos/frankmcsherry/datafrog, stargazers count: 105
Issues count: 0
Repo: https://api.github.com/repos/florent37/Shrine-MaterialDesign2, stargazers count: 104
Issues count: 0
Repo: https://api.github.com/repos/awesome-tips/awesome-tips-wx-app, stargazers count: 104
Issues count: 0
Repo: https://api.github.com/repos/sakura-editor/sakura, stargazers count: 99
Issues count: 1
	Issue url: https://api.github.com/repos/sakura-editor/sakura/issues/6
Repo: https://api.github.com/repos/bigric3/cve-2018-8120, stargazers count: 98
Issues count: 1
	Issue url: https://api.github.com/repos/bigric3/cve-2018-8120/issues/1
Repo: https://api.github.com/repos/dstogov/php-tensorflow, stargazers count: 92
Issues count: 0
Repo: https://api.github.com/repos/unamer/CVE-2018-8120, stargazers count: 88
Issues count: 0
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


