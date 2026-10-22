# SEO glossary

A working reference of SEO terms, each with one line of meaning and the words that were ruled out for it. Every SEO document, sheet, brief and skill run by an AI agent names things by the terms in this list. A term that is not here is checked with the owner before use; it is never invented.

How to read the tables:
- Do not use: words rejected in past sessions. They never come back.
- Sorted by area, then roughly by how often the term comes up.

## 1. Keywords and search demand

| English | Meaning | Do not use |
| --- | --- | --- |
| keyword | the phrase a page targets | kw, kwd |
| primary keyword | the one phrase a page is built for; lowercase, shortest searched form | pk, main kw, focus keyword |
| secondary keywords | the other phrasings with search volume that the same page targets | supporting keywords |
| keyword universe, semantic core | the full exported set of phrases around a seed, before any filtering | keyword pool |
| seed keyword | the bare phrase an export starts from |  |
| search volume | monthly searches per country database | SV |
| keyword difficulty (KD) | the Ahrefs or DataForSEO difficulty score |  |
| search intent, intent | what the searcher wants: informational, commercial, transactional, navigational |  |
| informational / commercial / transactional / navigational | the four intent classes |  |
| long-tail keyword | a longer, lower-volume phrase |  |
| query (Search Console), search query, search term | the phrase as reported by Search Console |  |
| branded / non-branded | contains the brand name or not |  |
| SERP | the search results page for a query |  |
| top 10 | the first page of organic results |  |
| SERP overlap | share of URLs two queries have in common in the top 10; 50% and above means one page |  |
| cannibalization | two of the site's own pages competing for one query |  |
| featured snippet | the answer box above the organic results |  |
| People Also Ask (PAA) | the question accordion in the results |  |
| AI Overview | Google's generated summary above the results |  |
| AI Mode | Google's conversational results tab |  |
| Google Discover | the feed surface in the Google app |  |
| impressions | times a URL appeared in results |  |
| clicks | clicks from results |  |
| CTR | clicks divided by impressions |  |
| position | average rank |  |
| organic traffic | visits from unpaid search results |  |
| ranking | how Google orders results |  |
| ranking factor | a signal Google uses to order results |  |
| search autocomplete | query predictions displayed in real time as a searcher types into the search box |  |
| keyword clustering | grouping semantically related search terms into target sets for a single page |  |
| keyword research | the process of discovering, analyzing, and selecting search queries to target with content |  |
| keyword stemming | reducing search query words to their root forms to match morphological variants |  |
| short-tail keyword | a brief, high-volume search term that has broad intent and high competition |  |
| sitelinks | additional subpage links displayed beneath a primary search snippet in search results |  |
| pogo-sticking | the behavior where a searcher rapidly bounces back and forth between a result and the SERP |  |
| dwell time | the duration between clicking an organic search result and returning to the results page |  |
| rich snippet | a search result decorated with extra visual details drawn from structured data on the page |  |
| search engine | a software program that crawls, indexes, and retrieves web documents matching search queries |  |
| 10 blue links | the traditional search result layout displaying ten plain organic text links per page |  |
| voice search | querying a search engine by speaking natural language into a device or virtual assistant |  |
| vertical search | a search index specialized in a single content type or niche, such as images, news, or jobs |  |
| personalization | altering search rankings based on an individual user's location, history, and search habits |  |
| serp volatility | the degree of ranking turbulence across search results, often signaling algorithm updates |  |
| organic search results | unpaid listings ranked by search engine algorithms based on relevance to the query |  |
| universal search | the blending of specialized media results like images, maps, and news into standard web listings |  |

## 2. Topical map and site structure

| English | Meaning | Do not use |
| --- | --- | --- |
| topical map | the Koray Gubur map: source context, central entity, Core and Outer sections, borders, nodes | five-layer map, spine |
| semantic SEO | optimising for entities, attributes and intents rather than single keywords |  |
| semantic content network | the whole set of pages built from one topical map, linked by context |  |
| topical authority | the standing Google gives a site on one topic; earned through topical coverage and historical data |  |
| topical coverage | how much of the central entity's attribute universe the site answers |  |
| historical data | the ranking and click record a site accumulates on a topic over time |  |
| cost of retrieval | the effort Google spends to crawl, render and understand a site; lower is rewarded |  |
| knowledge domain | the queries, entities, layouts and user segments of one field |  |
| contextual layer, contextual domain | the nested contexts a topic sits in, from field to sub-topic |  |
| macro context | the one main focus of a page: one entity + attribute pair, verbalised in the title |  |
| micro context | one heading-level sub-focus inside a page |  |
| contextual vector | the direction a page's headings take from the macro context through the micro contexts |  |
| contextual hierarchy | the order of micro contexts under a macro context (H1 to H2 to H3) |  |
| contextual flow | the logical order of sections and sentences inside a page |  |
| contextual bridge | the same thing as bridge below: the link and sentence that carry an Outer page into its Core cluster |  |
| information gain | what a page adds beyond what the top-ranking pages already say |  |
| query network | the set of related queries one topic generates; the map covers the network, not one keyword |  |
| query template | the query pattern a page template targets, written with placeholders: `{platform} migration`, `{hotel name}`, `events in {city}` |  |
| token insertion methodology | Koray's topic-generation step: words placed before, between and after the central entity; "token" is allowed only in this name |  |
| raw topical map | the entity + attribute pairs before they are verbalised into titles and slugs |  |
| document design template | Koray's name for the fixed format of pages of one type; our term for it is page template |  |
| vastness, depth, momentum | the three quality measures of a map: how many pairs, how fully each is answered, how fast it is published |  |
| publication frequency | the planned cadence that sets momentum |  |
| lexical semantics | synonyms, hypernyms and lexical variants used to phrase the raw map |  |
| ontology, taxonomy | the model of entity types and relations, and the classification tree built from it |  |
| head noun | the noun at the centre of the central entity; checked for polysemy |  |
| polysemous head noun | a head noun with several meanings in the results; forces disambiguation |  |
| SERP cohort, citation cohort | the class of results a query returns (for example citation guides instead of design agencies); an off-entity cohort rejects a node |  |
| node | one page position in the map; root node, raw node, quality node, trending node |  |
| sub-intent | a narrower intent inside a cluster that earns its own page |  |
| variation type | one way the central search intent is varied: platform, direction, data type, industry |  |
| proof rule | an industry or location hub ships only with a named case study or proof; otherwise it stays trend-watch |  |
| coverage gap | an entity + attribute pair in the map with no page |  |
| border violation | a live page that sits outside the topical borders |  |
| knowledge graph of the site | the current state: the entity types the site has pages for, each with its page template and query template; the topical map is the future state |  |
| entity definition | the map section: main entity, closely related entities, synonyms and lexical variants, entity types, critical attributes |  |
| highest-receiving pages | the pages the internal linking logic sends most links to |  |
| lateral link (Core-to-Core) | a link between two Core clusters, as opposed to the Outer-to-Core bridge |  |
| source context | what the business is and why it exists in the results |  |
| central entity | the entity the whole site is about; may be two entities paired |  |
| central search intent | the predicate + noun + locative sentence the site answers |  |
| Core Section | the part of the map where the business earns |  |
| Outer Section | the minor attributes that feed the Core through bridges |  |
| topical borders | the "do not write about" list |  |
| attribute universe | every attribute the central entity can take |  |
| entity + attribute pair | one coverage unit of the map |  |
| entity-attribute matrix | the table of pairs against pages |  |
| topical hierarchy | the URL tree derived from the map |  |
| quality node | a comprehensive, prominently linked page kept deep |  |
| trending node | a current-topic page linked back to the Core |  |
| bridge | the contextual link from an Outer page into its Core cluster |  |
| entity | a thing Google recognises as such |  |
| site architecture, URL structure, IA | how pages and folders are arranged | spine |
| pillar page, cornerstone content | the page that holds a cluster together | spine page, service spine |
| cluster, topic cluster | a group of pages sharing intent and supporting a pillar |  |
| hub, hub page, content hub | a top-level entry page: locations hub, industry hub, city hub |  |
| spoke, supporting page | a narrower page supporting a pillar |  |
| money page | a page that sells |  |
| page template | the fixed layout a page follows | archetype (except "site archetype" and "donor archetype" config keys) |
| entity type | one class of thing the site has pages for (event, host, city, platform, hotel); each entity type has one page template and one query template |  |
| programmatic pages, programmatic SEO | pages generated from a database through one page template |  |
| page type | the content-plan column: money page, hub, guide, template, tool, comparison |  |
| content plan | the ordered list of pages to publish | slate, shortlist |
| content brief | the writer-facing specification of one page |  |
| content gap, content gap analysis | a topic competitors cover and the site does not |  |
| thin content | a page with too little substance to rank |  |
| duplicate content | pages with the same content |  |
| topical authority | the site's standing on one topic |  |
| relevance | topical closeness of a page to a query |  |
| E-E-A-T | experience, expertise, authority, trust |  |
| AEO / GEO | optimisation for answer engines and generative search |  |
| local SEO | optimisation for city and region queries |  |
| 10x content | content created to be substantially better than any existing top-ranking result on the topic |  |
| article spinning | rewriting one piece of content into multiple variations to avoid duplicate content filters |  |
| article syndication | republishing original content across external sites with canonical tags or attribution |  |
| auto-generated content | text produced programmatically by software without human editorial oversight |  |
| co-occurrence | keywords and entities appearing together within content bodies across a topical domain |  |
| evergreen content | content that maintains search relevance and traffic value over time without expiring |  |
| content pruning | removing, consolidating, or redirecting low-performing and outdated pages to raise site quality |  |
| scraped content | third-party text republished without authorization or added value |  |
| seo silo | structuring site sections into isolated thematic directories linked strictly within each cluster |  |
| landing page | a dedicated webpage designed to receive targeted search traffic and convert visitors |  |
| search quality rater guidelines | the manual evaluation handbook used by human evaluators to assess website quality and trust signals |  |
| ymyl | pages covering topics that directly impact a reader's health, financial security, or personal safety |  |

## 3. On-page

| English | Meaning | Do not use |
| --- | --- | --- |
| Title, meta description, H1 (TDH), meta title, page title, title tag | the three on-page fields corgi extracts |  |
| meta description | the description tag |  |
| heading, header tags, heading tag | H1 to H6 |  |
| slug | the last path segment of a URL |  |
| URL | the page address |  |
| internal link | a link between two pages of the same site |  |
| interlinking, internal linking | the practice and the plan of internal links |  |
| anchor, anchor text, link text | the clickable text of a link | token |
| anchor variant | one surface form of an anchor for a target page | token |
| anchor repetition | the same anchor to the same page; max 3 per site, up to 10 for a quality node's main keyword |  |
| one anchor, one page | the same anchor never points at different pages |  |
| breadcrumbs, breadcrumb navigation | the path links at the top of a page |  |
| navigation | menus and footer links |  |
| orphan page | a page with no internal links to it |  |
| pagination | page 2, 3 ... of a list |  |
| filters, faceted navigation | parameter-driven list variants |  |
| structured data, schema markup | JSON-LD and the schema.org types |  |
| FAQ block | the question-answer section of a page |  |
| Q&A block | a question-and-answer section whose answers link out to supporting pages |  |
| bridge block, closing bridge section | the closing section of an article that links into the hub it supports |  |
| author bio, byline | the author identity on a page; named person with a live profile, never a role |  |
| freshness, content refresh, content decay | how recent a page is, the update that restores it, and the traffic loss that calls for it |  |
| TLDR | the short summary at the top of an article |  |
| call to action (CTA) | the conversion prompt |  |
| conversion | the action the page is meant to produce |  |
| alt text | an HTML attribute describing an image for screen readers and search crawlers |  |
| keyword density | the percentage of target keyword mentions relative to the total word count on a page |  |
| keyword stuffing | overloading webpage copy or meta tags with repetitive keywords to manipulate rank |  |
| meta tags | HTML head elements providing machine-readable metadata about a webpage to search engines |  |
| meta keywords | a deprecated HTML meta tag formerly used to declare keywords, now ignored by major search engines |  |
| open graph | metadata tags defining how page titles, images, and descriptions display when shared on social networks |  |
| outbound link | a hyperlink on a webpage pointing outward to a different domain |  |
| conversion rate | the percentage of page visits or clicks that result in a completed desired action |  |

## 4. Link-building and off-page

| English | Meaning | Do not use |
| --- | --- | --- |
| link-building (LB) | acquiring links from other sites; "LB" only in internal shorthand, written out on first use in any document |  |
| backlink, inbound link | a link from a page of one crawlable website to another website; never a link between task cards, documents or spreadsheets (those are links) |  |
| referring domain | a distinct root domain linking to the site; subdomains collapsed |  |
| donor, donor site | the site that hosts the placed link |  |
| target page | the page a link points at | acceptor |
| placement | one placed link or article on a donor |  |
| editorial placement | a placement inside the donor's own editorial content |  |
| guest post, guest blogging, guest posting | an article written for the donor |  |
| listicle | a "best of" list article |  |
| link insertion | a link added into an existing donor article |  |
| catalog, directory | a listing site |  |
| outreach | contacting donors |  |
| pitch, to pitch | the proposal sent to a donor |  |
| digital PR | earned coverage and links from media |  |
| paid placement / organic link / spam, natural link | the three classes every backlink falls into |  |
| paid velocity | median paid placements per month; the plan is sized from it, never from gross link count |  |
| anchor distribution, anchor diversity, anchor mix | the spread of anchors across types |  |
| anchor type: branded / naked URL / exact-match / partial-match / generic | the anchor classes | token |
| dofollow / nofollow / sponsored / UGC | the link attributes |  |
| DR (domain rating) | the Ahrefs domain strength score | DA (unless Moz is meant) |
| link spam | low-quality automated links |  |
| disavow | the Search Console rejection list |  |
| penalty, manual action | a Google-applied ranking penalty |  |
| subdomain hijack | spam hosted on a client's subdomain; signalled by gambling anchors pointing at it |  |
| tier-2 links, tiered link building | links to the pages that link to the site |  |
| PBN | a private blog network; a donor type to reject |  |
| spam score | a provider's spam estimate for a domain (Ahrefs is_spam is incomplete) |  |
| donor type | media, gov, professional association, edu, NGO, corporate, podcast platform, directory, forum |  |
| links-per-domain | the number of links one donor domain gives; sorted descending it exposes campaigns |  |
| brand mention, unlinked mention | the brand named on another site, with or without a link |  |
| citation | a reference to the site in a list, article or AI answer |  |
| campaign (backlink campaign) | a run of placements from one donor or partnership, read from first-seen dates and links-per-domain |  |
| first seen (backlink) | the date the index found the link, not the placement date |  |
| co-citation | two separate resources being cited together by a third-party webpage without directly linking |  |
| ego bait | content highlighting industry figures to encourage them to share and link back |  |
| link bombing | an organized backlink campaign using uniform anchor text to manipulate a page's rank for an unrelated term |  |
| link bait | high-value or provocative content created deliberately to attract spontaneous editorial backlinks |  |
| link equity | the ranking authority and search value transferred from one webpage to another through a link |  |
| link exchange | a reciprocal agreement between website owners to link to each other to manipulate rankings |  |
| link farm | a network of websites created solely to cross-link with each other and inflate search rankings |  |
| link profile | the overall makeup, diversity, authority, and quality of all backlinks pointing to a domain |  |
| link reclamation | identifying and reclaiming broken, modified, or lost backlinks pointing to a website |  |
| link rot | the natural decay over time where external hyperlinks break as destination pages disappear |  |
| link scheme | any manipulative link-building practice intended to deceive search algorithms in violation of guidelines |  |
| negative seo | malicious tactics by competitors intended to damage a rival website's organic search visibility |  |
| pagerank | an algorithm that evaluates page importance through the quantity and quality of inbound links |  |
| reconsideration request | an official appeal asking a search engine to lift a manual penalty after addressing guideline violations |  |
| resource pages | curated web pages that list helpful external links, commonly targeted for link-building outreach |  |
| sitewide link | a link that appears identically across every page of a website, such as in a footer or sidebar |  |
| trustrank | an algorithmic link analysis method that filters web spam based on proximity to trusted seed sites |  |
| unnatural links | artificial, paid, or manipulative links created to distort search engine rankings |  |

## 5. Technical SEO

| English | Meaning | Do not use |
| --- | --- | --- |
| crawl | a bot fetching pages |  |
| crawl budget | how much Googlebot fetches per period |  |
| crawl stats | the Search Console report |  |
| Googlebot logs, log analysis | server-log analysis of bot visits |  |
| indexing, indexed | inclusion in Google's index |  |
| noindex | the meta robots directive |  |
| robots.txt | the crawl rules file |  |
| sitemap | the XML list of URLs |  |
| canonical, canonical URL, rel=canonical, canonical tag | the preferred URL among duplicates |  |
| self-canonical | a page whose canonical points at itself; the SEODB base set |  |
| redirect, 301, 302 | one URL sending to another |  |
| redirect chain | two or more redirects in a row |  |
| redirect map / redirect rules | the old-to-new URL table / one rule per path, plain rows |  |
| status code, 404, soft 404 | the HTTP response |  |
| hreflang | the language-version annotation |  |
| language version, hreflang alternate | the same page in another language; never a cannibal |  |
| rendering, JS rendering | building the page in the browser |  |
| Core Web Vitals (CWV) | Google's page-experience metrics |  |
| page speed | load performance |  |
| mobile version | the page on phones |  |
| subdomain | host under the main domain |  |
| parameters, URL parameters | the ?key=value part |  |
| algorithm update, core update, spam update | a Google ranking change |  |
| technical SEO audit | the full technical review |  |
| seed list (audit) | the flat three-column issues list from a crawl |  |
| fix list | the prioritised task list for developers |  |
| acceptance criteria | how a developer proves a fix is done |  |
| root cause | the source fix, named before any symptom-hider |  |
| situation sentence | the one sentence from audit step 1 naming the situation: gradual decline, sudden date-bound drop, launch spike then decline, plateau, growing but behind a competitor, new low-authority domain, channel-specific weakness, never ranked |  |
| growth lever | what the domain lacks: backlinks, technical infrastructure, content, or fixes in the critical areas |  |
| growth hypotheses | the ranked causes drafted in audit step 2 |  |
| business type | news publisher, local business, SaaS, travel OTA, ecommerce, blog, service business, marketplace |  |
| page group | a set of URLs sharing one template or folder, used to split Search Console data |  |
| main template | a page template that carries a large share of pages, clicks or revenue; the unit the severity rule is measured on |  |
| break date | the day the traffic curve changed, overlaid with updates, releases and migrations |  |
| bot accessibility | whether content and links are in the HTML a bot receives |  |
| server-rendered | present in the HTML response, not added by JavaScript in the browser |  |
| hidden block | content present in the page but not visible or not in the HTML |  |
| parameter URL | a page addressed only through a query string, such as /listings?city={city} |  |
| crawl budget sink | a URL space that absorbs bot requests without value, found in the logs |  |
| critical issue | an issue on a main template, or above about 5% of indexable pages or 10% of clicks, that causes a sharp decline or a loss of potential |  |
| severity rule | the threshold above that decides critical versus ordinary |  |
| indexed though blocked | a URL blocked in robots.txt and still indexed, because the noindex can never be read |  |
| technical fix | one developer task from the fix list |  |
| 304 not modified | an HTTP status code indicating that a cached resource is still fresh and does not need retransmission |  |
| 410 gone | an HTTP status code signaling that a resource has been permanently removed and should be dropped from the index |  |
| 5xx status codes | HTTP server error response codes indicating that the host failed to fulfill a valid request |  |
| cached page | a saved snapshot of a webpage stored on search engine servers from its most recent crawl |  |
| cloaking | the deceptive practice of showing different content or URLs to search engines than to human visitors |  |
| crawlability | the ease with which search engine crawlers can discover, access, and read pages across a website |  |
| de-indexed | the complete removal of a URL or domain from a search engine index |  |
| doorway page | low-quality pages built solely to rank for search queries and immediately funnel visitors elsewhere |  |
| sandbox | an alleged filter that restricts new domains from achieving high search rankings during their early lifespan |  |
| webmaster guidelines | official documentation from search engines detailing quality standards, indexing rules, and prohibited practices |  |
| crawler | an automated program used by search engines to discover, fetch, and analyze pages across the web |  |
| https | an encrypted communications protocol securing browser-server traffic, serving as a lightweight ranking signal |  |
| index bloat | a situation where a search engine indexes an excessive volume of low-value, duplicate, or faceted URLs |  |
| indexability | the property of a webpage that allows a search engine to analyze it and include it in search results |  |
| image sitemap | an XML sitemap format specifically providing image URLs to assist visual media indexing |  |
| lazy loading | an optimization technique that defers loading offscreen images and assets until they enter the viewport |  |
| meta redirect | a client-side redirect executed in the browser using the HTML meta refresh tag rather than server headers |  |
| meta robots tag | an HTML head tag instructing search engine bots whether to index a page and follow its links |  |
| minification | stripping unnecessary whitespace, characters, and comments from source code to reduce download size |  |
| mirror site | an exact duplicate of an existing website hosted under a different domain or server |  |
| mobile-first indexing | the search engine indexing system that evaluates and ranks websites based primarily on their mobile version |  |
| render-blocking scripts | external scripts that stop a web browser from displaying page content until they are loaded and executed |  |
| responsive design | designing websites to dynamically resize and rearrange layouts across any screen resolution |  |
| root domain | the foundational domain hierarchy containing all subdomains, subfolders, and individual URLs |  |
| subfolder | a directory path following the main domain name separated by forward slashes |  |
| technical seo | optimizing site architecture, code, and server configurations to ensure bots can crawl and index pages smoothly |  |
| x-robots-tag | an HTTP response header that delivers crawler directives for non-HTML files or full pages |  |

## 6. Data, tools and reporting

| English | Meaning | Do not use |
| --- | --- | --- |
| Search Console (GSC) | Google's performance and indexing reports |  |
| Screaming Frog (SF) | the crawler |  |
| DataForSEO (DFS) | the SERP and keyword API |  |
| Ahrefs | backlink and keyword index |  |
| corgi | the in-house CLI (CorgiSEO) |  |
| SEODB | the per-page CSV: crawl + Search Console + summaries |  |
| SEO data layer | SEODB plus topical map plus provider data merged with Search Console |  |
| page summary | the 50-100 word per-page summary with primary and secondary keywords |  |
| content audit | per-page keyword assignment and cannibalization review |  |
| competitor analysis | organic competitors, content gap, backlink campaigns |  |
| before/after comparison | equal-length windows mirrored around the change date | period 2 / period 3, cohort codes |
| totals row | always the last row of a table |  |
| monthly report | the client reporting document |  |
| year over year | the same window one year earlier | YoY in client docs |
| brand versus non-brand split | Search Console data divided by branded queries |  |
| rank tracking, position tracking | recorded positions over time for a keyword set |  |
| SERP features | snippets, PAA, video, images, local pack, AI Overview and the rest |  |
| knowledge panel | the entity card on the right of the results |  |
| Google Business Profile (GBP), local pack | the business listing and the three-result map block |  |
| parent topic | the Ahrefs field naming the broader query a keyword belongs to |  |
| matching terms, related terms, keyword ideas | the Ahrefs and DataForSEO discovery endpoints; keep the English names |  |
| keyword mapping, keyword assignment | one primary keyword locked per page |  |
| share of voice, search visibility | the site's share of clicks or positions across a keyword set |  |
| AI visibility | how often the brand appears in AI answers (AI Overview, ChatGPT, Perplexity) |  |
| citation gap | prompts where competitors are cited in AI answers and the site is not |  |
| AI Instructions page, entity layer | a structured page that states what the entity is, for AI answer engines |  |
| web analytics | software platforms used to measure, collect, and report website traffic and user engagement data |  |
| tag manager | a web platform allowing site operators to manage and deploy analytics tracking scripts without modifying source code |  |
| webmaster tools | a search engine interface providing diagnostic reports on website crawl health, indexing status, and search queries |  |
| keyword alerts | an automated notification service tracking new web mentions of specified search terms or brand names |  |
| bounce rate | the percentage of single-page sessions where a user leaves without clicking or interacting further |  |
| time on page | the average duration a visitor spends viewing a single webpage before navigating to another URL |  |
| pages per session | the average number of pages viewed by a visitor during one browsing session |  |
| scroll depth | an engagement metric tracking how far down a webpage a user scrolls |  |
| clickstream data | aggregated user web browsing behavior data used by tools to estimate traffic and search volumes |  |
| direct traffic | website visits originating from users typing the URL directly, opening bookmarks, or clicking untracked links |  |
| referral traffic | website visitors arriving by clicking an external hyperlink on another website |  |
| social traffic | visitors arriving at a website by clicking links on social media platforms |  |
| tracking code | a snippet of JavaScript installed on a website to send visitor interaction data to analytics tools |  |
| not provided | the masking of organic search queries in web analytics platforms under a generic label |  |
| search operators | special command syntax typed into search boxes to filter, refine, and diagnose search results |  |
| local finder | the expanded local map view displaying the full directory of local business listings beyond the 3-pack |  |

## 7. Abbreviations in use

SEO, SERP, KD, GSC, SF, DFS, TDH, CTR, DR, LB (write out "link-building" on first use), CSI (central search intent), PAA, CWV, IA, UGC, PR, AEO, GEO, PBN, GBP, YMYL, E-E-A-T, AMP, NAP, ccTLD, TLD, LCP, CLS, TBT, TF-IDF, QDF, SSL, TLS, HSTS, JSON-LD, CDN, CMS, CPC, CPM, SEM, UTM, SAB, API, DOM, DNS, NLU, LSA.

## 8. Rejected terms (never reintroduce)

| Rejected | Use instead | Ruled |
|---|---|---|
| spine, new-spine, P3 spine pages, service spine | pillar page, site architecture, URL structure | 2026-05-11 |
| slate, final slate | content plan, shortlist, candidate list | 2026-05-11 |
| archetype (for a page layout) | page template | 2026-07-25 |
| token (backlinks, anchors) | anchor, anchor variant, anchor diversity | 2026-05-14 |
| token outside Koray's "token insertion methodology" | word, phrase, anchor | 2026-05-14 |
| brand-token concentration | branded anchor variant concentration | 2026-05-14 |
| microsites (for a set of small product sites) | minisites | 2026-05-26 |
| diaspora (Ukrainian-language users abroad) | Ukrainian-language audience, Ukrainian speakers abroad | PROJ memory |
| five-layer map | Koray map: Core and Outer sections | 2026-09-17 |
| period 2 / period 3, H5, cohort codes in client documents | plain words with dates | 2026-10-06 |
| green run (tests) | all tests pass | 2026-09-04 |
| kw, pk, any coined shorthand | the full term | global rule |
| backlink (for a link between task cards, Notion pages, Google Docs or Sheets) | link, link to the card | 2026-10-22 |

## 9. Change log

- 2026-10-17: v1 compiled from session rulings and Ukrainian-language working documents; Koray Gubur framework terms and technical-audit terms added the same day.
- 2026-10-17: reconciled against the Ahrefs, Moz and Semrush glossaries; 98 rows added, discrepancies listed in reconciliation-2026-10-17.md.
- 2026-10-17: rulings on the six reconciliation discrepancies (featured snippet renamed in Ukrainian, rich snippet row added, the other five keep the glossary meaning) and 15 vendor synonyms added to the English column.
- 2026-10-18: Ukrainian column, Ukrainian rejected-term rows and the loanwords section removed; the glossary is English only.
- 2026-10-22: backlink restricted to links between crawlable websites; links between task cards and documents are links.
