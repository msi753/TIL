# 자바 15버전 릴리즈, 이클립스 2020-09 새 버전 릴리즈
<br> Oracle OpenJDK 15 
<br> Oracle JDK 15
- Record
<br>레코드(record)란 "데이터 클래스"이며 순수하게 데이터를 보유하기 위한 특수한 종류의 클래스이다. 코틀린의 데이터 클래스와 비슷한 느낌이라고 보면 된다.
<br>Entity 혹은 DTO 클래스를 생성할때 사용되면 굉장히 좋을 듯하다.
```
public class SampleRecord {
   private final String name;
   private final Integer age;
   private final Address address;
 
   public SampleRecord(String name, Integer age, Address address) {
      this.name = name;
      this.age = age;
      this.address = address;
   }
 
   public String getName() {
      return name;
   }
 
   public Integer getAge() {
      return age;
   }
 
   public Address getAddress() {
      return address;
   }
}
```
```
public record SampleRecord(
   String name,
   Integer age,
   Address address
) {}
```

<br> 해당 record 클래스는 final 클래스이라 상속할 수 없다.
<br> 각 필드는 private final 필드로 정의된다.
<br> 모든 필드를 초기화하는 RequiredAllArgument 생성자가 생성된다.
<br> 각 필드의 getter는 getXXX()가 아닌, 필드명을 딴 getter가 생성된다.(name(), age(), address())

```
//json serialize
public record SampleRecord(
   @JsonProperty("name") String name,
   @JsonProperty("age") Integer age,
   @JsonProperty("address") Address address
) {}
```

```
======================================================================================
 
public record SampleRecord(
   @JsonProperty("name") String name,
   @JsonProperty("age") Integer age,
   @JsonProperty("address") Address address
) {
   
   static String STATIC_VARIABLE = "static variable";
   
   @JsonIgnore
   public String getInfo() {
      return this.name + " " + this.age;
   }
 
   public static String get() {
      return STATIC_VARIABLE;
   }
}
 
======================================================================================
 
public record Address(
    @JsonProperty("si") String si,
    @JsonProperty("gu") String gu,
    @JsonProperty("dong") String dong
) {}
 
======================================================================================
 
@Service
public class SampleRecordService {
    public Mono<SampleRecord> sampleRecordMono(SampleRecord sampleRecord) {
        return Mono.just(sampleRecord);
    }
}
 
======================================================================================
 
@RestController
public record SampleController(SampleRecordService sampleRecordService) {
    @PostMapping("/")
    public Mono<SampleRecord> sampleRecord(@RequestBody SampleRecord sampleRecord) {
        System.out.println(sampleRecord.getInfo());
        return sampleRecordService.sampleRecordMono(sampleRecord);
    }
}
 
======================================================================================
```

- Text Blocks
<br> String str = """ 문자열 """;
```
String textBlock = """
		This
		is
		a
		new
		feature,
		Text
		Block!""";
System.out.println(textBlock);
String inline = "\nThis\nis\anew\nfeature,\nText\nBlock!";
System.out.println(textBlock.equals(inline));
```
```
This
is
a
new
feature,
Text
Block!
true
```

<br> hidden class
<br> ZGC(Garbage Collect)가 Production Ready됨
<br> 자바 8에서 기본으로 쓰고 있는 Parallel GC부터
<br> https://blog.jetbrains.com/idea/2020/09/a-picture-of-java-in-2020/
<br> 자바 8을 가장 많이 사용한다 75%
<br> LTS Long Term Service 버전 release 주기가 6개월이다
<br> 스프링부트
<br> maven 70 vs gradle30

<br>오라클이 Tribuo라는 오픈소스 라이브러리를 공개했습니다. 자바로 만든 ML머신러닝 라이브러리

<br> 이클립스 2020-09
<br> preference> Code Mining기능
<br> 메서드를 어디 어디에서 사용하는지 보여준다
<br> 인텔리J
<br> Code Vision
<br> vsc코드에도 있음

<br> 깃허브에서 branch가 어감때문에 master->main으로 변경되었다

<br> 스프링부트
<br> 자바15 지원
<br> Docker Authentication
<br> Coding data import improvements
<br> Spring Boot 2.4.0.M3 마일스톤... 마이너하게 중요하다
<br> 2.1 
<br> 2.2
<br> 2.3 ... 이런 식의 버전업은 버그 수정

<br> https://medium.com/javarevisited/java-concurrency-java-memory-model-96e3ac36ec6b

<br> 프로젝트 Loom: 비동기 프로그래밍
<br> Reactive Stream류 (WebFlux, R2DBC, RSocket) 
<br> http://jdk.java.net/loom/
<br> light weight thread
<br> Java의 동시성 개선을 위한 Project Loom은 reactive streams를 대체할 것인가?
<br> 하나의 서버에서 수백만 개의 소켓을 다룰 수 있지만 OS 스레드를 직접적으로 사용하는 자바에서는 동시에 수천 개 이상의 요청을 효율적으로 다루기 어렵다. 이를 극복하기 위해 최근 수년 간 많은 비동기 라이브러리들이 탄생하였는데 이는 작성하고 이해하고 디버깅하기 편해서가 아니라 단지 <u>자바의 스레드가 성능면에서 효율적이지 못하기 때문이다.</u>
<br> Loom의 목표는 수백만 개를 생성할 수 있는 파이버라고 불리는 경량 스레드를 제공하여 어플리케이션 개발자들이 (이 환경에서 비용이 거의 무료인) <u>동기 블로킹 코드를 마음껏 사용</u>하고 라이브러리 개발자들이 더 이상 동기 / 비동기 API를 둘 다 제공할 필요가 없게 하는 데 있다.
<br> 비동기 프로그래밍의 단점 ex) 콜백 헬
https://www.infoq.com/presentations/continuations-java/  14분 20초
<br> 제어 흐름을 잃는다
컨텍스트를 잃는다(스택 트레이스가 유용하지 않다)
전염성이 있다
<br> 비동기 프로그래밍의 단점 극복
<br> async / await 또는 suspend function 
손실된 스택 트레이스의 의도적 보완
