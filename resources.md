---
title: Resources
permalink: /resources/
layout: post
description: A list of resources used by the WCGS Programming Society.
published: true
---

{% for post in site.posts %}
{% if post.categories == "resources" %}[{{ post.title }}]({{ post.url }}){% endif %}
{% endfor %}
