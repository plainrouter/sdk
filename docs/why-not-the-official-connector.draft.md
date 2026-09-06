---
title: Why not the official connector?
description: The difference between accessing a platform's reporting and checking it against first-party evidence.
status: draft
publication_gate: DR-34-IMPL and Engineering item 1 arrival-semantics verification
---

# Why not the official connector?

Meta ships its own MCP connector. If you want an agent to work with Meta's reporting, the official connector is a natural place to start.

But connecting an agent to a report does not change where the report comes from. The official connector is the platform reporting on itself.

PlainRouter’s positioning asks a structural question: who supplies the evidence used to audit the platform’s report? Connecting to the platform’s own report does not, by itself, provide a separate source of evidence.

That distinction matters when deciding what to investigate and whether to change spend. Easier access to a platform's numbers is useful. A separate basis for checking those numbers serves a different purpose.

## Different evidence can answer different questions

Platform-reported clicks and spend are the platform’s claims. An arrival recorded from a document request and a server-observed conversion are observations of different events. A modeled estimate must be labeled as a model and kept distinct from those observations. Comparing them requires clear definitions, compatible scopes, and an explanation of what each source can observe. A difference alone does not establish that either source is wrong.

Target state, gated on DR-34-IMPL merging: a reader could inspect the arrival definition, the eligibility rule, and the provenance value behind an observed count, then compare that count with the platform’s claim. This is a target-state requirement, not a description of evidence PlainRouter currently exposes. Inspectability does not promise agreement on a number.

## Editorial hold: not for publication

This SDK docs draft and the related comparison page are held pending DR-34-IMPL merging and the arrival-semantics verification under Engineering item 1. Neither gate has been confirmed in this task. Do not publish either page until both are confirmed.

The structural claim concerns the source of the official connector’s reporting. This draft does not claim that PlainRouter currently shows independent evidence. Any sentence claiming that PlainRouter shows that evidence is a DR-34 claim and remains gated on DR-34-IMPL, including the working sentence.

After confirmation, align the copy with the verified definition of an arrival, its counting boundaries, and the limits of comparison with platform metrics. Do not imply that arrivals equal clicks or that discrepancies prove platform misreporting.

Positioning brief supplied by Robin: Wevion answers the official-connector question with breadth. PlainRouter’s proposed answer concerns the structure of an audit, rather than connector breadth. Verify current Meta and Wevion product claims against primary sources before publishing a named comparison.

This file is an unpublished SDK documentation draft. Keep it out of install navigation and published comparison content until the gates above are satisfied.
