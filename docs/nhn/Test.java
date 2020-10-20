public class Test {
   public static void main(String[] args) {
      System.out.println("Hello world");
   }
}



// System.out.print를 사용하려고 했더니
// log4jExample를 쓰라고 하네...
// https://www.tutorialspoint.com/log4j/log4j_sample_program.htm
// 사용방법

// import org.apache.log4j.Logger;

// import java.io.*;
// import java.sql.SQLException;
// import java.util.*;

// public class log4jExample{

//    /* Get actual class name to be printed on */
//    static Logger log = Logger.getLogger(log4jExample.class.getName());
   
//    public static void main(String[] args)throws IOException,SQLException{
//       log.debug("Hello this is a debug message");
//       log.info("Hello this is an info message");
//    }
// }

// System.out.print를 운영환경에서 권장하지 않는다
// 테스트나 개발환경에서 사용하는 것은 문제가 없다
// 왜냐하면 사용자는 에러를 볼 필요가 없기 때문이다
// 따라서 log를 사용하는 것을 권장한다


// 지원하는 언어가 jdk14이상이다
// 8버전을 사용하고 있어서
// 파일>기본설정>설정
// java home 
// settings.json파일에서
// "java.home": "C:\\Program Files\\Java\\jdk-14.0.2",
// "java.configuration.runtimes": [

//     {
//         "name": "JavaSE-1.8",
//         "path": "C:\\Program Files\\Java\\jdk1.8.0_202", // 기존 1.8 JDK SE
//       },
//       {
//         "name": "JavaSE-14",
//         "path": "D:\\jdk-14.0.2", // Open JDK 14 SE
//         "default": true
//       }
// ]
// 이 내용을 추가해 주었다