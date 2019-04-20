# Deep Learning
Reference from O'REILLY Japan 「ゼロから作る Deep Learning」

## Get started 
```shell
$ sh open_python_default.sh  ## start with python image
### or ###
$ docker build -t tkkrr/deep:latest .  ## Build docker image
$ sh open_python_custom.sh  ## Start with custom python image
```

## Environment
### Infrastructure
+ MacOS - 10.14.4
+ Docker - 2.0.0.2 ( Docker Engine - 18.09.1 )

### Docker Image
+ Python - 3.7.3-stretch
+ Pip - 19.0.3


## Tips
### `plt.show()`が実行できない
これはDockerから提供されるものが仮想環境であるため，ホストでは表示されないからです．この問題を解決するためには仮想デスクトップ等の設定を行い，外部接続によってdocker環境上のGUIをホストで受け取るようにします．Docker環境上では正しく`plt.show()`が動作していることがわかります．
