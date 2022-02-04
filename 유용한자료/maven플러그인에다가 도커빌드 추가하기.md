`mvnw package`

package

이렇게 하면 프로젝트를 패키징한다. 

```
java -jar target/springdocker223-0.0.1-SNAPSHOT.jar
```



## maven플러그인에다가 도커빌드 추가하기

```
<plugin>
                <groupId>io.fabric8</groupId>
                <artifactId>docker-maven-plugin</artifactId>
                <version>0.38.0</version>
                <configuration>
                    <images>
                        <image>
                            <name>boy0516/springdocker223</name>
                            <build>
                                <dockerFileDir>${basedir}</dockerFileDir>
                            </build>
                        </image>
                    </images>
                </configuration>
            </plugin>
```

플러그인을 추가하고

```
 ./mvnw docker:build
```

이걸 실행해주면 도커 이미지가 생성된다. 



