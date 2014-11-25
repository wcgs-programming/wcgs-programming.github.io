---
title: Showcase
permalink: /showcase/
layout: post
description: A shocase of all the projects completed by programmers at WCGS.
published: true
---

{% for post in site.posts %}
{% if post.categories contains "showcase" %}[{{ post.title }}{{ post.categories | size }}]({{ post.url }}){% endif %}
{% endfor %}
