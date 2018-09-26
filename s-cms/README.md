官网 https://www.s-cms.cn/

s-cms有两个版本，一个是asp+access\mssql版本，一个是php+mysql版本。两者除了语言本身的差异外，没有其他的差异。

这里以php版本为例子。

下载地址 https://shanlingtest.oss-cn-shenzhen.aliyuncs.com/file/2.mall.php.zip

问题出在/bank中的几个callback文件，以callback1.php为例：
![Alt text](/s-cms/img/1.png)

第36行拼接的sql语句没有任何过滤：

    $sql="select * from SL_list where L_no like '".$P_no."'";

那么整个程序的逻辑就是

    $json_string=file_get_contents("php://input");
    $obj=json_decode($json_string);
    $P_no = $obj->P_no;
    $sql="select * from SL_list where L_no like '".$P_no."'";
执行sql语句有个前提条件：

    if(strtolower(MD5("P_address=".$P_address."&P_attach=".$P_attach."&P_city=".$P_city."$xxxxx)))==strtolower($sign))
左边是我们提交的json值的数据的md5值，右边是$sign,
    $sign =$obj->sign;

即$sign也可控，也就是说提交的json值只需要满足

    sign==md5('P_address=xxx&P_attach=xxx+....')
    
为了方便看提交参数的md5值，改了下服务端代码，将其echo出来（加密是可以自己实现的，这里是为了方便看，后面有完整的poc）
![Alt text](/s-cms/img/2.png)
成功之后会返回success,代表已经执行了下面的sql

    select * from SL_list where L_no like '1' and sleep(5)#';
    
讲道理这样就行了，但是在实际测试过程中并没有等待，研究了下是因为sql语句中，当前面查询的是个空表的时候，and后面的语句不会执行。

![Alt text](/s-cms/img/3.png)

由于后面还有正常的inset操作，所以我们只需要传几个类型正确的参数过去让其插入一条语句即可，这样就可以继续盲注了。
![Alt text](/s-cms/img/4.png)

注意一些参数是数值型，一些是字符。

poc运行截图：

![Alt text](/s-cms/img/poc.png)
