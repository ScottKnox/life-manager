# Product Goals

## Vision

Life Manager delivers a single, concise **daily briefing** that tells you
everything you need to know to start your day — spoken aloud, hands-free.

The pipeline is **phone → cloud → voice**: a phone triggers a request, the cloud
backend aggregates data from every life module, and the result is delivered as
natural speech.

## Principles

- **One briefing, not many apps.** Consolidate scattered information into one
  summary instead of forcing the user to check multiple sources.
- **Incremental and low-risk.** Ship small, composable modules that each add a
  sentence or two to the briefing.
- **Voice-first.** Output is meant to be heard, so keep language natural and brief.
- **Personal, not general.** Optimize for a single user's real daily routine.

## Briefing Modules (Roadmap)

Each module plugs into `build_briefing()` and contributes to the spoken summary.

- [ ] Weather summary
- [ ] Calendar summary
- [ ] Bills due summary
- [ ] Medication reminders
- [ ] Birthday reminders
- [ ] Budget flags
- [ ] Voice delivery (phone → cloud → voice)

## Non-Goals

- No multi-tenant / general-purpose product yet — single user focus.
- No backward-compatibility guarantees while the data model evolves.
