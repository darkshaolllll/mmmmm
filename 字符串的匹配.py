html="""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="css/base.css"/>
<link rel="stylesheet" type="text/css" href="css/index.css"/>
  <title>百度一下，你就知道</title>
</head>
<body>
    <div class="nav">
    	<span id="nav-b">
      <a href=""class="nav-a">新闻</a>
      <a href=""class="nav-a">hao123</a>
      <a href=""class="nav-a">地图</a>
      <a href=""class="nav-a">视频</a>     
      <a href=""class="nav-a">贴吧</a>
      <a href=""class="nav-a">学术</a>
      <a style="font-weight:normal" href=""class="nav-a">登录</a> </span>
      <li id="zzr"class="huge lili"><span id="nav-b"><a style="font-weight:normal"  href="" class="nav-a">设置</a> </span>
      <ul>
        <li><a href="#" class="shezhi">搜索设置</a></li>
        <li><a href="#" class="shezhi">高级搜索</a></li>
        <li><a href="#" class="shezhi">关闭预测</a></li>
        <li><a href="#" class="shezhi">搜索历史</a></li>
      </ul></li>
      <a class="more" href="">更多产品</a>
      </div>       
     <div id="logo">
      <img src="img/bd_logo1.png" width="270" height="120">
      </div>     
      <form>  
      		  <input type="text">
    	<input type="submit" name="send" class="search_butt" value="百度一下" />
    	     <!--<button type="button">百度一下</button>-->
    </form>
  <div class="footer">
  	<div class="img"><img src="img/zbios_x2_9d645d9.png "width="60" height="60">
  	<br /><p><b>百度</b></p>
  	</div>
  	<div class="about">
  		<a href=""class="about-a">把百度设为主页</a>
  		<a href=""class="about-a">关于百度</a>
  		<a href=""class="about-a">About Baidu</a>
  		<a href=""class="about-a">百度推广</a>
  	</div>
  	<div class="foot">
©2019&nbsp;Baidu&nbsp;
  		<a href="">使用百度前必读</a>
  		<a href="">意见反馈 </a>&nbsp;
  		京ICP证030173号  <img src="img/icons_1.png"/>&nbsp;&nbsp;
  		<a href="">京公网安备11000002000001号</a><img src="img/icons_2.png"/>
  	</div> 
  </div>
    </div>
</body>
</html>
"""
from pyquery import PyQuery as pq
doc=pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))