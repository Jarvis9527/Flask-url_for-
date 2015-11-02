一，Flask 框架中路由函数url_for()的具体定义   redirect(url_for('index'))
1，注：因为在刚接触Flask框架时候，写了验证用户登录程序，但是不知道处理完数据，如何让其他路由处理数据,吃过亏，在这里记录一下，希望能理解
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

2,静态文件：
Web程序不是仅由Python代码和模板组成，大多数程序还会使用静态文件，例如HTML代码中引用的图片，JavaScript源码文件和CSS
hello.py程序的URL映射时，其中一个static路由，这是因为对静态文件的引用被当成一个特殊的路由，
即/static/<filename>，例如，调用url_for('static', filename='css/styles.css', _external=True)得到的结果是http://localhost:5000
/static/css/styles.css

默认设置下，Flask在程序根目录中名为static的子目录中寻找静态文件，如果需要，可在static文件夹中使用子文件夹存放文件，服务器收到前面那个URL后，会生成一个响应，包含文件系统中static/css/styles.css文件的内容。

3,在程序中基模板中放置favicon.ico图标，这个图标会显示在浏览器的地址栏中.
tmplates/base.html:
{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename = 'favicon.ico' )}}"
    type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
    type="image/x-icon">
{% endblock %}

4，
