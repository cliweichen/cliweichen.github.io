---
permalink: /
title: " "
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

复旦大学社会学专业在读博士生，上海。

研究聚焦于网络传播、网络社会心态、计算社会科学与青年研究等领域。

致力于综合使用计算方法（如大数据文本分析、机器学习、网络爬虫）和传统社会科学研究方法（如田野实验、问卷调查）来探索复杂的社会问题。

您可以通过此网站了解我的研究成果、项目经历和学术动态。

## 部分成果

{% for post in site.publications limit:4 %}
  {% include archive-single.html %}
{% endfor %}

<p style="text-align: right;"><a href="/publications/">查看所有出版物...</a></p>
