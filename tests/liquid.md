---
layout: draft
title: Liquid testing page
squares: [1,4,9,16]
---
Can I use liquid inside markdown pages?

{% for square in squares %}
  {{ square }}
{% endfor %}


