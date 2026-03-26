# User Rules

1. **ANSWER IN CHINESE!**
2. **.trae/reference/ref.txt**（如果没有请新建）里面是需要参考的github地址或接口文档，如果你认为有哪些可以参考，在网上搜索（用agent skill）补充到该文件中;
3. **global参数前置**到py文件最上边，并且有具体使用位置精确到行的注释;
4. **灵活使用agent skill和mcp**来完成任务;
5. **完成所有任务清单**，完成之前不要退出;
6. **TDD模式**，每个任务开始前先写测试脚本，测试必须有超时机制，脚本必须通过测试才算完成任务;
7. **将user_rules.md文件中的所有规则都保存在**：.trae/rules/user_rules.md中;
8. **如果有git仓库**，先暂存本地修改，然后git pull，然后再继续下面的步骤;
9. **Create python venv environment**(use command: uv), and install python packages in requirements.txt;
10. **每次对话后都要确保python的import不缺失**，requirements.txt里的模块不缺失，requirements.txt里面不要写版本号，requirements_{python version}.txt里面是带版本号的模块;
11. **每次对话后都要git push to origin:main**，commit内容就是我说的那句话。user.email="939342547@qq.com", user.name="qq939", remote=https://github.com/qq939/{projectName}, branch=main, when push to this remote, maybe you need to create remote repository(use: gh repo create {projectName} --public);
12. **git add .trae/rules/project_rules.md**
13. **git add .trae/rules/user_rules.md**
14. **如果git推送到远端失败**，rebase并且push --force-with-lease
