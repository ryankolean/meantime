# Competitive scan - Detroit beer bars

- **Reviewed:** 2026-09-16
- **Scope:** direct comparables, meaning Detroit bars whose product is other people's beer, plus the two breweries in Meantime's own lineage. Verified entries were loaded and read. Entries marked *to verify* came out of search results only and have not been audited.

## Verified

### Cøllect Beer Bar - collect-beerbar.com
- Squarespace. Nav is Home, About, cart. Hamburger, minimal.
- Beer list is **described, not published**: "draft beers + bottles + cans + wine + ciders + seltzers + gatorade on tap". No live feed, no list, no image.
- Hours and address present, email `hello@collect-beerbar.com`, no phone.
- Minimal, whitespace-forward, sans-serif, casual.
- **Read:** the closest peer to Meantime in both scene position and web maturity (Annonson came from here). It concedes the beer list entirely. Meantime already beats it by publishing a live Untappd menu, and that lead is the thing to press.

### meantimeoncass.com (the incumbent, for reference)
See `meantimeoncass-com-design-spec.md`. Three pages, live Untappd embed, stale PNG for everything else, empty store, no story.

## To verify

| Site | Why it matters |
|---|---|
| Eastern Market Brewing Co. | Hoffman's former employer. Brewery-with-taproom pattern: events calendar, beer finder, merch store that is actually stocked |
| Florian East Lagers & Ales | Collaborator on the house pilsner Midwest Leisure. Lager-forward positioning is the nearest thing to Meantime's own |
| HopCat Detroit | The big-room incumbent. Worth reading only for how a large tap list is presented and filtered |
| Temple Bar, Old Miami, and other Cass Corridor neighbors | Neighborhood-bar web presence in the same few blocks, and the local search set Meantime competes in |

## Patterns worth taking

1. **A live tap list is a differentiator in this market, not table stakes.** The nearest peer does not publish one at all. Meantime already has the Untappd feed; the rebuild should make it the centerpiece rather than a page you click into.
2. **Nobody in this set publishes a phone number.** Email or Instagram DM is the accepted contact path for Detroit beer bars, which lowers the pressure on the phone question but raises it on having a real contact route at all.
3. **Hours and address are universally present and universally unstructured.** Shipping correct `LocalBusiness` JSON-LD with real `openingHours` is a cheap, uncontested local-search win.
4. **Merch stores are usually either stocked or absent.** An empty published store, which is what Meantime has now, is the worst of the three states.
5. **Nobody is telling a story.** Meantime has three owners with a real origin, a Czech side-pull program, a membership club, and a magic 8 ball. An about page with actual copy would put it ahead of everything in this set.

## Patterns worth avoiding

- Squarespace default titles leaking into search results (Meantime's own "Homepage" problem, and a common one in this set).
- Menus as flat images.
- Nav reduced so far that there is nowhere to put the story, the events, or the membership.
