---
title: "Gobeeshan's Work"
layout: post
published: true
categories: showcase
---

> Gobeeshan has enjoyed making websites at programming club, demonstrating his ability to use HTML and CCS.

{% for post in site.posts %}
{% if post.categories contains "gobeeshan" %}[{{ post.title }}]({{ post.url }}){% endif %}
{% endfor %}
