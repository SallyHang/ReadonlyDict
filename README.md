# ReadonlyDict

Hello Python，Hello everyone.

This is my first python app in GitHub. I'm super excited.

这个小功能主要实现的是读取json文件，将其转变为只读字典，不允许增删改。



## DictObj 类

变量：__init 初始值为False，初始化后变为Ture。作用：对象初始化后，禁止增删改

方法：DictObj.readDict(filename) 

- 入参：filename： json文件的路径
- 返回：dict类型

异常：

- 当增加或者修改dict数据时，抛出异常

  ```python
  AttributeError: DictObj is READ ONLY.You can update nothing!
  ```

- 当删除dict数据时，抛出异常

  ```python
  AttributeError: DictObj.db is READ ONLY.You can delete nothing!
  ```

  

## 使用方法

```python
if __name__ == '__main__':
    m = DictObj.readDict('config.json')
  	print(m)
  	book = DictObj(m)
  	print(book.dbname)
```

运行：

```python
PS D:\ProgramFiles\python\Miniconda\Lib\site-packages\recommend\readonly_dict> python .\readonly_dict.py
{'dbname': 'emir', 'dbaddr': '10.0.0.1', 'dbuser': 'root', 'dbpsword': 'root'}
emir
```



