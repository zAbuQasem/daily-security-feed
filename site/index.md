---
layout: default
title: Feed
---

{% assign posts = site.posts | sort: "date" | reverse %}

{% if posts.size == 0 %}
_No articles yet. The pipeline runs daily — check back soon._
{% endif %}

{% assign current_date = "" %}
{% for post in posts %}
  {% assign post_date = post.date | date: "%B %d, %Y" %}
  {% if post_date != current_date %}
    {% assign current_date = post_date %}

### {{ current_date }}

  {% endif %}

<div style="background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 12px 16px; margin-bottom: 8px;">
  <a href="{{ post.url | relative_url }}" style="font-weight: 600;">{{ post.title }}</a>
  {% if post.priority %}<span class="badge badge-{{ post.priority }}">P{{ post.priority }}</span>{% endif %}
  {% if post.feed %}<span style="color: var(--muted); font-size: 0.8rem;"> · {{ post.feed }}</span>{% endif %}
</div>

{% endfor %}
