---
title: "Prethessh's Work"
layout: post
published: true
categories: showcase
---

> Prethessh from 9W came to us wanting to make his own websites.

> On Wednesdays, Prethessh comes to programming to build up his knowledge so he can make his own websites:

{% for post in site.posts %}
{% if post.categories contains "prethessh" %}[{{ post.title }}]({{ post.url }}){% endif %}
{% endfor %}
