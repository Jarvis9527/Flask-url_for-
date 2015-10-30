一，Flask 框架中路由函数url_for()的具体定义   redirect(url_for('index'))

1，注：因为在刚接触Flask框架时候，写了验证用户登录程序，但是不知道处理完数据，如何让其他路由处理数据，
Python Flask Web框架的url链接问题：
在模板中，直接编写简单路由的URL链接不难，但对于包含可变部分的动态路由，在模板中构建正确的URL就很困难。
而且，直接编写URL会对代码中定义的路由产生不必要的依赖关系，如果重新定义路由，模板中的链接可能会失效。
为了避免一些问题，Flask提供了url_for()辅助函数，它可以使用程序URL映射中保存的信息生成URL。

url_for()函数最简单的用法是以视图函数名(或者app.add_url_route()定义路由时使用的端点名)作为参数，返回对应的URL，
例如：当前版本的hello.py程序中调用url_for('index')得到的结果是/。 调用url_for('index', _external=True)返回的则是绝对地址
这个地址示例中是http://localhost:5000

提示：生成连接程序内不同路由的链接时，使用相对地址就足够了，如果要生成在浏览器之外使用的链接，则必须使用绝对地址，例如在
电子邮件中发送链接。

使用url_for()生成动态地址时，将动态部分作为关键字参数传入，例如，url_for('user', name='john', _external=True)的返回结果是
http://localhost:5000/user/john

传入url_for()的关键字参数不仅限于动态路由中的参数，函数能将任何额外参数添加到查询字符串中，例如，url_for('index', page=2)
的返回结果是/?page=2



