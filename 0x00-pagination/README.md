0x00. Pagination
================

Back-end

-   By Emmanuel Turlay, Staff Software Engineer at Cruise
-   Weight: 1

### Concepts

*For this project, we expect you to look at this concept:*

-   [Back-end concepts](https://alx-intranet.hbtn.io/concepts/557)

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/3646eb02de6527ca5d83.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220709%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220709T120201Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f7de581aeb1eab7f2158274123c0315890bfc0f06e394514436e8d908bf403ff) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/746187b76bea1f46030e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220709%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220709T120201Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f52bb33e4c7773095f0b4e9a7aa62b8f2d63f13db20a4d09225837d91fb944c0) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/665ce871c2ecc66a8e71.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220709%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220709T120201Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ba97b20e4725605cde543ba9ac70b6b6cf7ed70c9b220e0943c4ec5c33fa11cc)

Resources
---------

**Read or watch:**

-   [REST API Design: Pagination](https://alx-intranet.hbtn.io/rltoken/7Kdzi9CH1LdSfNQ4RaJUQw "REST API Design: Pagination")
-   [HATEOAS](https://alx-intranet.hbtn.io/rltoken/tfzcEbTSdMYSYxsspJH_oA "HATEOAS")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/zQ78qQVUjaPExupXQpAaHw "explain to anyone"), **without the help of Google**:

-   How to paginate a dataset with simple page and page_size parameters
-   How to paginate a dataset with hypermedia metadata
-   How to paginate in a deletion-resilient manner

Requirements
------------

-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/env python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `pycodestyle` style (version 2.5.*)
-   The length of your files will be tested using `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
-   A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
-   All your functions and coroutines must be type-annotated.

Setup: `Popular_Baby_Names.csv`
-------------------------------

[use this data file](https://alx-intranet.hbtn.io/rltoken/NBLY6mdKDBR9zWvNADwjjg "use this data file") for your project

Tasks
-----

### 0\. Simple helper function

mandatory

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$

```

**Repo:**

-   GitHub repository: `alx-backend`
-   Directory: `0x00-pagination`
-   File: `0-simple_helper_function.py`

 Done? Help Check your code Get a sandbox

### 1\. Simple pagination

mandatory

Copy `index_range` from the previous task and the following class into your code

```
import csv
import math
from typing import List

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass

```

Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.

-   You have to use this [CSV file](https://alx-intranet.hbtn.io/rltoken/NBLY6mdKDBR9zWvNADwjjg "CSV file") (same as the one presented at the top of the project)
-   Use `assert` to verify that both arguments are integers greater than 0.
-   Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
-   If the input arguments are out of range for the dataset, an empty list should be returned.

```
bob@dylan:~$  wc -l Popular_Baby_Names.csv
19419 Popular_Baby_Names.csv
bob@dylan:~$
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$
bob@dylan:~$  cat 1-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")

print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

bob@dylan:~$
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
bob@dylan:~$

```
