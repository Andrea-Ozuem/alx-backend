0x03. Queuing System in JS
==========================

Back-endJavaScriptES6RedisNodeJSExpressJSKue

-   By: Johann Kerbrat, Engineering Manager at Uber Works
-   Weight: 1

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/1486e02a78cdf7b4557c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220815T195509Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=35ec3a36d25c73a134fb0de3065010e6c5f93cba917db5eebd0ee999f3a10511)

Resources
---------

**Read or watch**:

-   [Redis quick start](https://alx-intranet.hbtn.io/rltoken/8xeApIhnxgFZkgn54BiIeA "Redis quick start")
-   [Redis client interface](https://alx-intranet.hbtn.io/rltoken/1rq3ral-3C5O1t67dbGcWg "Redis client interface")
-   [Redis client for Node JS](https://alx-intranet.hbtn.io/rltoken/mRftfl67BrNvl-RM5JQfUA "Redis client for Node JS")
-   [Kue](https://alx-intranet.hbtn.io/rltoken/yTC3Ci2IV2US24xJsBfMgQ "Kue") *deprecated but still use in the industry*

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/7yh7c3Zyy1RyUsdwlfsyDg "explain to anyone"), **without the help of Google**:

-   How to run a Redis server on your machine
-   How to run simple operations with the Redis client
-   How to use a Redis client with Node JS for basic operations
-   How to store hash values in Redis
-   How to deal with async operations with Redis
-   How to use Kue as a queue system
-   How to build a basic Express app interacting with a Redis server
-   How to the build a basic Express app interacting with a Redis server and queue

Requirements
------------

-   All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
-   All of your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `js` extension

Required Files for the Project
------------------------------

### `package.json`

Click to show/hide file contents

### `.babelrc`

Click to show/hide file contents

### and...

Don't forget to run `$ npm install` when you have the `package.json`

Tasks
-----

### 0\. Install a redis instance
### 1\. Node Redis Client

mandatory

Install [node_redis](https://alx-intranet.hbtn.io/rltoken/mRftfl67BrNvl-RM5JQfUA "node_redis") using npm

Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

-   It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly
-   It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work

**Requirements:**

-   To import the library, you need to use the keyword `import`

### 2\. Node Redis client and basic operations

..
