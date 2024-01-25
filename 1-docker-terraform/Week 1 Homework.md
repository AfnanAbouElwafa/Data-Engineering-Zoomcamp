# Module 1 Homework

## Docker & SQL

### Q1: Which tag has the following text: "Automatically remove the container when it exits"
- --delete
- --rc
- --rmc
- **--rm** (highlighted)
  
  The answer is `--rm`

### Q2: What is the version of the package wheel?
- **0.42.0** (highlighted)
- 1.0.0
- 23.0.1
- 58.1.0

  The answer is `0.42.0`

```shell
docker run -it python:3.9 bash
root@532b222df6a5:/# pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 58.1.0
wheel      0.42.0
```

## Prepare Postgres