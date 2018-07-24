import scala.collection.mutable.ListBuffer

/**
  * Created by Administrator on 2018/7/20.
  */
object WyScala1 {
  def main(args:Array[String]){
    var b =List(37,28,19,30,15,26,34)
    for (i<-Range(0,7)){
      if(i == 2){
        println("周三："+b(i))}
      else{
        println(b(i))
      }
    }
  }
}



object WyScala2 {
  def main(args:Array[String]){
    ///for和if搭配
    for(i<-Range(0,10) if(i>5)){////////if成立则执行
      println(i)
    }
    ///for和yield搭配
  val fun2 =for(i<-Range(0,10)) yield i*10-1
    println("fun2:"+fun2)

  }
}
/////////////函数
object WyScala3{
  def main(args:Array[String]) {
    def sum(a: Int, b: Int) = {
      a + b
    }
    println(sum(3, 4))
  }
  ////////////////匿名函数（lambda函数   一句话函数） 闭包
  val add=(a: Int, b: Int)=>a+b    ////////lambda函数
  println(add(4,5))
  /////指令的集合只有一条指令的函数
  def ad(a: Int, b: Int):Int=a+b
  println(ad(2,6))

///////含有默认值的函数参数
  def abc(a: Int, b: Int,opt:String="+"):Int={
  print(opt)
  a+b
}
  abc(5,6)
  abc(5,6,"-")
}

object WyScala4 {
  def main(args: Array[String]) {
    def abc(a: Int, b: Int,opt:String="+"):Int={
      print(opt)
      a+b
    }
    abc(5,6)
    abc(5,6,"-")
  }
}


/**
  * 1.读取文件textFile
  * 2.过滤"status":0}的数据 filter
  * 3.将 "data":Array[5]转变成多行  flatMap   抚平
  * 4.获取 "school":"华南师范大学",  "plan":"2",
  * 4.获取 "school":"华南师范大学",  "plan":"2",  reduce 缩减
  * 5.学校和招生人数 排序， 按照招生人数排序 。sort
  *
  */
object YaSpark1{
  def main(args: Array[String]) {
    import org.json.JSONObject//导入str转json工具包
    import org.apache.spark.SparkConf//
    import org.apache.spark.SparkContext
    //sparkcontext的配置，运行在本地，名称为cala
    val conf = new SparkConf().setAppName("cala").setMaster("local")
    val sc = new SparkContext(conf)//Spark运行环境,,本地电脑，集群
    //使用spark读取文本文件
    sc.textFile("F:\\大数据实训\\河南数据.txt")
      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{//line str===>List line  抚平
        val  json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        //        jsonlist.getJSONObject(0)
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))
  }
}





//测试
object YaSparkTest{
  def main(args: Array[String]) {
    println("status\":1}")
    println("aaa@qq.com".endsWith("qq.com"))
    //    new JsonObject
    //    import json    将字符串转换为json（字典）
    import org.json.JSONObject
    val json = new JSONObject("{\"data\":{\"city_name\":\"\\u6e56\\u5357\"},\"info\":\"\",\"status\":0}")
    println(json.getInt("status"))
    println(json.getJSONObject("data"))
    val list = List[Int](1,1,1)//大小不变的固定列表
    //    list(2) = 3
    val list2 = ListBuffer[Int]()
    list2.append(3)
    list2.append(4)
    println(list2)
  }
}


