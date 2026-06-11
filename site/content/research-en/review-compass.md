---
title: "Review Compass"
date: 2026-06-11
summary: "LLM-assisted specification-driven development platform"
thumbnail: "/images/review-compass-en.jpg"
top_highlight: true
---

日本語版: [Review Compass (JP)](/research/review-compass/)

## ReviewCompass
ReviewCompass is a review and governance platform designed for LLM-assisted specification-driven development.

Recent advances in Large Language Models (LLMs) have dramatically accelerated software development. Developers can now generate code, designs, and documentation in minutes rather than days. However, as implementation becomes easier, a new challenge emerges: deciding how generated artifacts should be reviewed, managed, approved, and integrated into the development process.

In traditional software engineering, specifications primarily serve as documents for communication, agreement, and quality assurance among humans. In LLM-assisted development, specifications take on an additional role: they become operational boundaries that define what an AI agent is allowed to read, modify, decide, and execute.

As projects grow, developers spend increasing amounts of time making management-oriented decisions rather than focusing on domain knowledge and system design. Examples include determining which specification should be updated, whether an issue belongs to requirements or design, how changes propagate across features, and when human approval is required. We refer to this challenge as **arbitration load**.

ReviewCompass is designed to reduce this arbitration load.

The platform organizes development into a structured hierarchy:

**Intent → Feature Division → Requirements → Design → Tasks → Implementation**

and applies systematic reviews across all layers.

A key feature of ReviewCompass is its **three-role review model**:

- **Protagonist**: identifies issues and improvement opportunities
- **Adversary**: challenges assumptions and searches for alternative viewpoints
- **Judge**: classifies and prioritizes findings

Rather than simply detecting defects, ReviewCompass helps determine how each finding should be handled: fixed locally, escalated to higher-level specifications, propagated across features, or routed to human review.

The platform also supports multi-model evaluation, disagreement analysis, alternative proposal generation, escalation workflows, approval gates, and traceability management. By combining AI reviewers with human decision makers, ReviewCompass enables organizations to maintain quality and governance without sacrificing the productivity gains offered by modern LLMs.

Our goal is not to replace human judgment. Instead, ReviewCompass helps developers and architects focus on high-value decisions by making review processes transparent, traceable, and scalable.

ReviewCompass provides a foundation for trustworthy, auditable, and collaborative software development in the era of AI-assisted engineering.

<img src="/images/review-compass-en.jpg" alt="Review Compass" style="max-width:720px; width:100%; height:auto; display:block; margin:0.5rem auto;">
