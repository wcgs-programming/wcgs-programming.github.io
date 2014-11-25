---
title: "Vithurun Vasanthakumar"
layout: post
published: true
categories: showcase
---

> Vithurun from 7Ma makes Python programs with GUIs in Mr Joyce's lessons, and experiments with the Raspberry Pi robots on Wednesdays.

> On Monday, Vithurun came to programming to continue some big work-in-progress projects from CS class, like the chatbot:

{% for post in site.posts %}
{% if post.categories contains "vithurun-vasanthakumar" %}[{{ post.title }}]({{ post.url }}){% endif %}
{% endfor %}
