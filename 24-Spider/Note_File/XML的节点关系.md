## XML的节点关系

#### 1. 父(Parent)

> 每个元素以及属性都有一个父

示例：book元素是title、author、year以及price元素的父

```xml
<?xml version="1.0" encoding="utf-8"?>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```



#### 2. 子(Children) 

> 每个元素节点可以有零个、一个或多个子

示例：title、author、year 以及 price 元素都是 book 元素的子

```xml
<?xml version="1.0" encoding="utf-8"?>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```



#### 3. 同胞(Sibling) 

> 拥有相同父的节点

示例：title、author、year 以及 price 元素都是同胞

```xml
<?xml version="1.0" encoding="utf-8"?>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```



#### 4. 先辈(Ancestor) 

> 某节点的父、父的父等等

示例：title 元素的先辈是 book 元素和 bookstore 元素

```xml
<?xml version="1.0" encoding="utf-8"?>

<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```



#### 5. 后代(Descendant) 

>  某个节点的子、子的子等等

示例：bookstore 的后代是 book、title、author、year 以及 price 元素

```xml
<?xml version="1.0" encoding="utf-8"?>

<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>


```

