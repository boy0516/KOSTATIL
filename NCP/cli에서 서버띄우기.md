```
{"createServerInstancesResponse": {
  "requestId": "ec6c8b53-2b12-4216-b373-f115f35e64c4",
  "returnCode": "0",
  "returnMessage": "success",
  "totalRows": 1,
  "serverInstanceList": [
    {
      "serverInstanceNo": "8002546",
      "serverName": "s17bbdefd647",
      "serverDescription": "",
      "cpuCount": 1,
      "memorySize": 1073741824,
      "baseBlockStorageSize": 53687091200,
      "platformType": {
        "code": "LNX64",
        "codeName": "Linux 64 Bit"
      },
      "loginKeyName": "ncp2021",
      "isFeeChargingMonitoring": false,
      "publicIp": "",
      "privateIp": "10.41.196.126",
      "serverImageName": "centos-6.6-64",
      "serverInstanceStatus": {
        "code": "INIT",
        "codeName": "Server init state"
      },
      "serverInstanceOperation": {
        "code": "NULL",
        "codeName": "Server NULL OP"
      },
      "serverInstanceStatusName": "init",
      "createDate": "2021-09-07T10:46:58+0900",
      "uptime": "2021-09-07T10:46:59+0900",
      "serverImageProductCode": "SPSW0LINUX000044",
      "serverProductCode": "SPSVRSTAND000056",
      "isProtectServerTermination": false,
      "portForwardingPublicIp": "101.101.164.235",
      "zone": {
        "zoneNo": "3",
        "zoneName": "KR-2",
        "zoneCode": "KR-2",
        "zoneDescription": "평촌 zone",
        "regionNo": "1"
      },
      "region": {
        "regionNo": "1",
        "regionCode": "KR",
        "regionName": "Korea"
      },
      "baseBlockStorageDiskType": {
        "code": "NET",
        "codeName": "Network Storage"
      },
      "baseBlockStorageDiskDetailType": {
        "code": "HDD",
        "codeName": "HDD"
      },
      "internetLineType": {
        "code": "PUBLC",
        "codeName": "PUBLC"
      },
      "serverInstanceType": {
        "code": "MICRO",
        "codeName": "Micro Server"
      },
      "userData": "",
      "initScriptNo": "",
      "accessControlGroupList": [],
      "instanceTagList": []
    }
  ]
}}
```

8002546

101.101.164.235

* getAccessControlGroupList [ 현재 보유하고있는 ACG리스트를 출력합니다 ]
* getAccessControlGroupServerInstanceList [ ACG가 적용되어있는 서버인스턴스리스트를 출력합니다 ]
* getAccessControlRuleList [ 특정 ACG의 Rule을 조회합니다 ]





# cli에서 띄우기

- VPC 생성

```
ncloud vpc createVpc --regionCode KR --vpcName main --ipv4CidrBlock 10.0.0.0/24
```

반환값

```
{"createVpcResponse": {
  "requestId": "84e********************2ef2",
  "returnCode": "0",
  "returnMessage": "success",
  "totalRows": 1,
  "vpcList": [
    {
      "vpcNo": "1***7",
      "vpcName": "main",
      "ipv4CidrBlock": "10****4,
      "vpcStatus": {
        "code": "INIT",
        "codeName": "init"
      },
      "regionCode": "KR",
      "createDate": "2021-09-07T12:29:47+0900"
    }
  ]
}}
```

- 생성한 VPC의 Default Network ACL 조회(Network ACL 번호 가지고 조회)

```
ncloud vpc getNetworkAclList --vpcNo 1***7
```

반환값

```
{"getNetworkAclListResponse": {
  "requestId": "bdac9ffe-********-***-**3287ea",
  "returnCode": "0",
  "returnMessage": "success",
  "totalRows": 1,
  "networkAclList": [
    {
      "networkAclNo": "1***6",
      "networkAclName": "main-default-network-acl",
      "vpcNo": "13047",
      "networkAclStatus": {
        "code": "RUN",
        "codeName": "run"
      },
      "networkAclDescription": "VPC [main] default Network ACL",
      "createDate": "2021-09-07T12:29:47+0900",
      "isDefault": true
    }
  ]
}}
```



- 서브넷 생성

```
ncloud vpc createSubnet --zoneCode KR-1 --vpcNo 1***4 --subnetName subnet1 --subnet 10.0.1.0/24 --networkAclNo 1***0 --subnetTypeCode PUBLIC
```



- 서버 생성 시 실행할 init 스크립트 생성(init 스크립트 번호)

```
ncloud vserver createInitScript --initScriptContent "#!/bin/sh'$'\n''yum install -y httpd'$'\n''service httpd start'$'\n''echo '\''Hello World'\'' > /var/www/html/index.html'$'\n''chkconfig --level 2345 httpd on"
```



```
ncloud vserver createServerInstances --vpcNo 1*** --subnetNo 2****81 --serverImageProductCode "SW.VSVR.OS.LNX64.CNTOS.0606.B050" --networkInterfaceList "networkInterfaceOrder="0", accessControlGroupNoList=['']"
```



- 서버 이미지 조회

```
ncloud vserver getServerImageProductList
```



- 생성한 VPC의 Default ACG조회

```
ncloud vserver getAccessControlGroupList --vpcNo *****
```



- 서버 이미지로 최소 사양의 서버 인스턴스 생성

```
ncloud vserver createServerInstances --vpcNo 1***54 --subnetNo 2***1 --serverImageProductCode "SW.VSVR.OS.LNX64.CNTOS.0708.B050" --networkInterfaceList "networkInterfaceOrder='0', accessControlGroupNoList=['23955']" --initScriptNo **90
```



- 서버에 공인 IP 주소 생성 및 할당

```
ncloud vserver createPublicIpInstance --serverInstanceNo ***182
```



- 서버의 Network Interface에 적용된 ACG에 80번 포트 허용 규칙 설정

```
ncloud vserver addAccessControlGroupInboundRule --vpcNo 1***4 --accessControlGroupNo 2**** --accessControlGroupRuleList "protocolTypeCode='TCP', ipBlock='0.0.0.0/0', portRange = '80'"
```



