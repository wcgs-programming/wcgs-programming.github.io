---
title: "Future Projects"
layout: post
published: true
categories: showcase
---

> We'd like to show you some of the things that we have planned for you to try out: <br> If you want to try this out, feel free to let us know - we've written this up because we think you can do it.

> These future projects are here in case you want to skip ahead a little:

{% for post in site.posts %}
{% if post.categories contains "future-projects" %}[{{ post.title }}]({{ post.url }}){% endif %}
{% endfor %}