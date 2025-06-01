# GitHub Pages
只要两步就能让网站运行:

1. Click *Use this template*, and create your repository as `<username>.github.io` on GitHub.
![Step 1](https://user-images.githubusercontent.com/5889006/156916624-20b2a784-f3a9-4718-aa5f-ce2a436b241f.png)

2. Open Settings -> Pages. Change the build branch from `master` to `gh-pages`.
![Build](https://github.com/namanh11611/hugo-theme-stack-starter/assets/16586200/12c763cd-bead-4923-b610-8788f388fcb5)


# 本地运行

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install hugo-extended
hugo server
```


加密解密插件是最弱最弱的加密，只能骗骗不懂的人，请不要依赖它！