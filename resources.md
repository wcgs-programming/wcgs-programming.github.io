---
title: Resources
permalink: /resources/
layout: post
description: A list of resources used by the WCGS Programming Society.
published: true
---

{% for post in site.posts %}
[{{ post.title }}]({{ post.url }})
{% endfor %}
